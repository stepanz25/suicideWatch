# suicideWatch

# suicideWatch Dashboard

- [Overview](#overview)
- [Motivation and Purpose](#motivation-and-purpose)
- [Usage](#usage)
- [Description](#description)
- [App Sketch](#app-sketch)
- [Reference](#reference)
- [Contributing](#contributing)
- [License](#license)

## Overview

The `suicideWatch` Dash app provides visualizations and statistics on the number of suicides and suicide rates for different age groups and genders in various countries. The app is primarily targeted towards researchers, policymakers, mental health professionals, and anyone interested in exploring and analyzing suicide rates with interactive capabilities that allow them to study the trends to find measures to mitigate the detrimental effects of such phenomena.

## Motivation and Purpose

Engineering an app about suicide may have a significant impact on peoples lives who may be struggling with mental illnesses. This app could serve as a resource to bring more awareness to the society on what countries may struggle with increased suicide rates the most.

This Dash application is a little cuisine of our bigger [Shiny](https://github.com/UBC-MDS/suicide_indicator_r) application build upon the same data set.The target audience, persona and research question of this project are the same as the one in our Shiny application which proposal could be found [here](https://github.com/UBC-MDS/suicide_indicator_r/blob/main/proposal.md).

## Usage

The link to the app is [here](INSERT THE LINK)

To use the `suicideWatch` app, simply open the app following the guidelines under `Running the App locally` below and select the desired countries from the drop down menus. Then select the year range you are interested in querying your search results for by using the slider. You could also select or un-select the gender as "Male" or "Female" by selecting the appropriate tick box in the top selection pane. The app will display a visualization of the number of suicides and the corresponding suicide rate (per 100,000 population) for the selected age group and gender in selected countries by year. Users can use this information to gain insights into the factors that contribute to the suicide rates in the countries of interest. Additionally, the app provides information and resources for suicide prevention, as well as links to support organizations and hotlines.

More detailed information about each plot and its interactivity could be found in the `Description`section of this README.md file.

Usage examples:

- Select 4 countries to compare from the selection pane on the top to filter the plots by year.
- Select sex from the selection pane on the top below country and year selection to filter the plots by gender.

**INSERT THE USAGE GIF HERE**

### Running the App locally

To run the app locally using docker, first change the following lines in `src/app.py`:

```python
data = pd.read_csv("/app/data/master.csv")
country_codes = pd.read_csv("/app/data/country_codes.csv")
```

to this:

```python
data = pd.read_csv("data/master.csv")
```

Then, run the following command:

```bash
docker-compose up
```

## Description

The dashboard consists of one web page that shows statistics and 2 main reactive plots:

- The distribution of the number of suicides

The graph compares the number of suicides per 100,000 population in the selected countries on the y-axis and the year on the x-axis. The plot provides an intuition on how many suicide cases were there in each country and what was the general trend in the years of interest. It is also possible to compare the individual bars in the bar chart to get an idea of how other countries were doing in terms of their suicide rates. The displayed bar chart is interactive enabling users to get more granular information through tooltips by hovering over the visuals/data points. The user can also select and un-select the country by clicking on the title of the country they are interested in un-selecting in the legend below the plot which provides extra flexibility.

- The distribution of age groups for suicides

The pie chart compares the distirbution of age groups for suicides in each country selected in the dropdown menu by age group. The plot could potentially be useful in identifying high-risk age groups and evaluating the impact of suicide prevention interventions. The displayed pie chart is interactive enabling users to get more granular information through tooltips by hovering over the visuals/data points. The user can also select and unselect the age group by clicking on the on the age group they are interested in un-selecting in the legend below the chart which provides extra flexibility.

Additionally, the filters in the selection pane on the top allows users to filter the dataset by sex.

## App Sketch

**INSERT THE APP SKETCH**

## Reference

The dataset used in this project is the [Suicide Rates Overview (1985 to 2021)](https://www.kaggle.com/datasets/omkargowda/suicide-rates-overview-1985-to-2021) available on Kaggle. The data was originally sourced from the United Nations Development Program, World Bank and World Health Organization.

Please refer to the original data sources for more information on how the data was collected and processed.

## Contributing

Interested in contributing? Check out the contributing guidelines. We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/stepanz25/suicideWatch/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms outlined [here](https://github.com/stepanz25/suicideWatch/blob/main/CODE_OF_CONDUCT.md).

|  Author  |  Github Username |
|--------------|------------------|
|  Stepan Zaiatc |  @stepanz25 |

## License

The materials of this project are licensed under the [MIT license](https://github.com/stepanz25/suicideWatch/blob/main/LICENSE). If re-using/re-mixing please provide attribution and link to this webpage.
