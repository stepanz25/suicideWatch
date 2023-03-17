import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash, html, dcc, dash_table


# Load data some data pre-processing
df = pd.read_csv('../data/master.csv')
#df = df.query('suicides_100k_pop != 0')


# Create app

external_stylesheets = [dbc.themes.YETI, '/assets/theme.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# Define layout
app.layout = dbc.Container([
    
    dbc.Row([
        dbc.Col(html.H1('Suicide Rates Dashboard', className='text-center'), width=12)
    ]),
    
    dbc.Row([
        html.H3('Cross-Country Comparisons'),
        html.H6('Select 4 countries to compare:'),
        dbc.Col([
            html.Label('Country 1', className='font-size: small'),
            dcc.Dropdown(
                id='country1-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df.country.unique())],
                value='Canada',
                clearable=False,
                className='mt-2'
            )
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            html.Label('Country 2', className='font-size: small'),
            dcc.Dropdown(
                id='country2-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df.country.unique())],
                value='Germany',
                clearable=False,
                className='mt-2'
            )
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            html.Label('Country 3', className='font-size: small'),
            dcc.Dropdown(
                id='country3-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df.country.unique())],
                value='Russian Federation',
                clearable=False,
                className='mt-2'
            )
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            html.Label('Country 4', className='font-size: small'),
            dcc.Dropdown(
                id='country4-dropdown',
                options=[{'label': country, 'value': country} for country in sorted(df.country.unique())],
                value='Thailand',
                clearable=False,
                className='mt-2'
            )
        ], width={'size': 3, 'offset': 0})
    ], className='mb-4 mt-4'),

    dbc.Row([
        dbc.Col([
            html.H6('Select year range:'),
            dcc.RangeSlider(
                id='year-slider',
                min=df.year.min(),
                max=df.year.max(),
                value=[df.year.min(), df.year.max()],
                marks={str(year): str(year) for year in range(df.year.min(), df.year.max()+1, 2)},
                className='mt-2'
            )
        ], width={'size': 12})
    ], className='mb-4 mt-4'),

    dbc.Row([
        dbc.Col([
            html.H6('Filter by sex:'),
            dcc.RadioItems(
                id='sex-radio',
                options=[
                    {'label': 'Both', 'value': 'both'},
                    {'label': 'Female', 'value': 'female'},
                    {'label': 'Male', 'value': 'male'}
                ],
                value='both',
                className='mt-2'
            )
        ], width={'size': 12, 'width': '100%'})
    ], className='mb-4 mt-4'),

    dbc.Row([
        dbc.Col([
            dcc.Store(id='data-store', data=df.to_dict('records')),
            dcc.Graph(id='results-graph')
     ], width={'size': 12})
    ]),
    
    dbc.Row([
        html.Hr(style={'border-width': '3px'}),
        html.H3('Distribution of Age Groups for Suicides in Each Country')
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='results-pie1')
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            dcc.Graph(id='results-pie2')
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            dcc.Graph(id='results-pie3')
        ], width={'size': 3, 'offset': 0}),

        dbc.Col([
            dcc.Graph(id='results-pie4')
        ], width={'size': 3, 'offset': 0})
    ], className='mb-4 mt-4'),

    dbc.Row([
    html.Div('If you or someone you know need help, you can call 1.800.SUICIDE (1.800.784.2433). If it\'s an emergency, call 9.1.1.')
    ], className='warning')


], fluid=True)

# Define the callback to update the data store
@app.callback(
    Output('data-store', 'data'),
    [Input('country1-dropdown', 'value'),
    Input('country2-dropdown', 'value'),
    Input('country3-dropdown', 'value'),
    Input('country4-dropdown', 'value'),
    Input('year-slider', 'value'),
    Input('sex-radio', 'value')]
)

def update_data_store(selected_country1, selected_country2, selected_country3, selected_country4, selected_year_range, selected_sex):
    filtered_dfs = []
    
    for selected_country in [selected_country1, selected_country2, selected_country3, selected_country4]:
        if selected_sex == 'both':
            filtered_df = df[(df['country'] == selected_country) & (df['year'].between(selected_year_range[0], selected_year_range[1]))]
            if filtered_df.empty:
                new_row = {'country' : selected_country, 'year' : selected_year_range[0]}
                filtered_df = filtered_df.append(new_row, ignore_index=True)
        else:
            filtered_df = df[(df['country'] == selected_country) & (df['year'].between(selected_year_range[0], selected_year_range[1])) & (df['sex'] == selected_sex)]
            if filtered_df.empty:
                new_row = {'country' : selected_country, 'year' : selected_year_range[0], 'sex' : selected_sex}
                filtered_df = filtered_df.append(new_row, ignore_index=True)
        
        filtered_dfs.append(filtered_df)
    
    df_combined = pd.concat(filtered_dfs)
    return df_combined.to_dict('records')


# Define the callback to update the graphs
@app.callback(
    [Output('results-graph', 'figure'),
    Output('results-pie1', 'figure'),
    Output('results-pie2', 'figure'),
    Output('results-pie3', 'figure'),
    Output('results-pie4', 'figure')
    ],
    Input('data-store', 'data')
)

def update_graphs(data):
    figures = []
    df = pd.DataFrame.from_dict(data)

    # Histogram for Suicide Comparisons Between Countries

    fig = px.histogram(df, x='year', y='suicides_100k_pop', color='country', barmode='group')
    
    fig.update_layout( 
        xaxis = dict(
            title = 'Year',
            dtick = 1,              # set the interval between x-axis labels
            tickangle = -60         # set the angle to x-axis labels
        ),
        yaxis_title = 'Number of suicides per 100K people',
        legend = dict(
            title = "", 
            orientation = "h",      # set the orientation to 'h'orizontal
            x = 0.5, 
            y = -0.4, 
            xanchor = "center", 
            yanchor = "bottom"
        ),
        title = {
            'text': 'Suicide Comparisons Between Countries',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    # Add the histogram chart to the list of figures
    figures.append(fig)


    # Update pie charts

    legend_order = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']

    # create a list of unique country names in the dataframe
    country_list = df['country'].unique()

    # loop through each country and create a pie chart
    for country in country_list:
        
        chart_data = df[df['country'] == country]
        if chart_data.empty:
            fig = px.pie(labels=["No data available for the selected year range"], values=[1])
        
        else:
            chart_data['age'] = pd.Categorical(chart_data['age'], categories=legend_order, ordered=True)  # add ordered categories to age column
            chart_data = chart_data.sort_values('age')  # sort by age column
            fig = px.pie(chart_data, values='suicides_100k_pop', names='age',
                labels={'suicides_100k_pop': 'Suicides per 100K Population', 'age': 'Age Group'},
                title=country)
            fig.update_traces(
                textposition='inside',               # set text position to inside of the slices
                sort=False
            )
            fig.update_layout(
                margin=dict(l=20, r=0, t=30, b=0),  # adjust margin to move the chart position
                #showlegend = False,
                legend=dict(
                    orientation='h'                 # horizontal orientation,          
                )
            )
        '''
        # Only show the legend for the last pie chart
        if (country_list[len(country_list)-1] == country):
            fig.update_layout(showlegend = True)
        '''

    
        # Add the pie chart to the list of figures
        figures.append(fig)

    return figures




# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
