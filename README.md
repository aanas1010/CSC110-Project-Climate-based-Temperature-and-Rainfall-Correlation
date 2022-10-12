## General Information

**Project Title:** Climate-based Temperature and Rainfall Correlation

**Authors:** Aabid Anas, Matthew Chan, Shayaan Khan, Markus Nimi

## Problem Description and Research Question

**What is the correlation between monthly temperature and monthly rainfall in different climate regions represented by the Köppen climate Model between 1901 and 2016?**

As a direct result of worldwide industrialisation, trends in global temperatures have been observed to be increasing at an alarming rate, a phenomenon described by scientists as global warming (Richards, 2019). However, opposed to a uniform increase in temperature worldwide, different regions on Earth experience different results as consequences of global warming; they display a wide range of weather pattern disruptions. In response to this local variation, the term Climate Change has been used to describe this discrepancy (Nunez, 2019).

We chose to research the correlation between temperature and rainfall to determine whether or not temperature factors into the increase or decrease in precipitation for a given climate region. Moreover, we particularly chose precipitation given its vitality to the success of a civilization, as it can dictate, among others, agricultural success, flooding, or ecosystem disruptions. Major flooding can have many negative impacts on a community, including the loss of property, destruction of crops, and the loss of life. Droughts result in the loss of crops and an undersupply of water, endangering the lives of many living things (Conservation in a Changing Climate, 2020). All of these examples come to show the severity of disruptions to a nation’s rainfall patterns.

We will explore the relationship, if any, between average monthly temperature and total monthly rainfall over time for five countries of varying Köppen Climate Model climate groups to gain a more holistic perspective that may apply more generally and accurately to the world’s countries (Beck et al., 2020). While many countries lie within multiple climate regions, the countries we’ve chosen belong to one sole region, making them ideal representatives of their respective groups. With the trends observed in our graphs, we should be able to determine whether or not changes in the amount of precipitation are caused by changes in temperature.

For example, conclusions from the program would have the following structure: “Regions that are of Köppen Climate Region _x_ experienced a [Strong / Weak / Negligible] [positive / negative] correlation between average temperature and monthly rainfall for the month of _y_ as seen over time.” In this format, we are able to record a change in both average monthly temperature and total monthly rainfall for each region for a specific month, and observe any possible correlations.

## Dataset Description

The World Bank is an international financial institution that provides many different datasets and statistics. Their website provides many different CSV files regarding climate change data, including data for monthly average temperature and cumulative rainfall by country for all years between 1901 and 2016 (5 datasets to encompass this entire year range per country). We will be selecting data for five different countries representing the five major classifications of the Köppen climate model. The countries and territories we have chosen are Malaysia - Tropical, Greenland - Polar, Great Britain - Temperate, Saudi Arabia - Arid, and Belarus - Continental. For both the rainfall and temperature data, each country will have their total of 10 datasets (downloaded from the website as .csv files), containing columns for the year, rainfall/temperature (depending on which file), statistics, country and ISO3. The dataset will be transformed in our program to be easier to handle. Below are the names of the datasets, the format, columns used and description.

**Datasets**

| Datasets | Format | Columns Used | Descriptions |
| --- | --- | --- | --- |
| pr\_1901\_2016\_BLR.csv | CSV | Rainfall - (MM), Year | Total rainfall per month for Belarus |
| tas\_1901\_2016\_BLR.csv | CSV | Temperature - (Celsius), Year | Average temperature per month for Belarus |
| pr\_1901\_2016\_GBR.csv | CSV | Rainfall - (MM), Year | Total rainfall per month for Great Britain |
| pr\_1901\_2016\_GBR.csv | CSV | Temperature - (Celsius), Year | Average temperature per month for Great Britain |
| pr\_1901\_2016\_GRL.csv | CSV | Rainfall - (MM), Year | Total rainfall per month for Greenland |
| pr\_1901\_2016\_GRL.csv | CSV | Temperature - (Celsius), Year | Average temperature per month for Greenland |
| pr\_1901\_2016\_MYS.csv | CSV | Rainfall - (MM), Year | Total rainfall per month for Malaysia |
| pr\_1901\_2016\_MYS.csv | CSV | Temperature - (Celsius), Year | Average temperature per month for Malaysia |
| pr\_1901\_2016\_SAU.csv | CSV | Rainfall - (MM), Year | Total rainfall per month for Saudi Arabia |
| pr\_1901\_2016\_SAU.csv | CSV | Temperature - (Celsius), Year | Average temperature per month for Saudi Arabia |


## Computational Overview

Our project comprises 3 primary computational sections, regarding data representation and manipulation, graphing and regression calculations, and a user interface. In tandem, these functionalities allow the user to easily select, view, and comprehend data for a given country and given month over time.

**Data Manipulation**

First, data from csv files in a designated folder is processed by the Pandas Python library. The __get_country_data__ function in the __dataframe_handling__ module is called by __main__ to obtain this data, and __get_country_data__ in turn calls many other functions in the module. Overall, __dataframe_handling__ makes heavy use of the Pandas Python library, which allows us to convert csv files into a coherent DataFrame object with relative ease. This object stores data in a column-like and row-like interpretation, using Pandas methods to write and read values from the table. Once these objects are stored, we manipulate them to display data relevant to the program. By means of __reformat_df__, the country code is removed and the year and month is combined, and later with __sort_by_month__, this data is separated by month using a dictionary, mapping month indexes to DataFrames. After doing this twice for a given country, once for rainfall data and once for temperature data, the two dictionaries are combined by creating a dictionary with new DataFrames with columns for both values for a given month over time. These calculations are done for every country, with values stored in a master dictionary in __main__ called __dict_of_countries__.

**Graphing and Correlation Calculations**

Once __dict_of_countries__ is created, we access this data and plot the points on a graph using SeaBorn, a data visualization library based on MatPlotLib. With this library, we transfer this data into a visual representation via scatterplot. In the module __graph_handling__, the function __graph_data__ is mainly used. SeaBorn’s library has support for twin axes, allowing us to graph both Average Monthly Temperatures and Monthly Rainfall on the same graph overlaid on each other with colour-coded points and axes for clarity. At the same time, with SeaBorn, degree 3 polynomial regression is used to form a line of best fit to identify any correlation between rainfall and temperature, regardless of time (which in this case is 1901 to 2016). Using the Python SciPy library in the function __get_correlations__, we can then calculate Pearson’s Correlation Coefficient, a decimal between -1 and 1 that represents the linear association between two variables – in this case, rainfall and temperature. -1 indicates a strong negative association and 1 indicates a strong positive association (with 0 being a negligible association).

**User Interface**

Lastly, a unified user interface allows the user to easily manage the data by enabling a selection of data to be plotted and for a correlation coefficient to be determined. In __main__, after __dict_of_countries__ is established, the __Tkinter__ library is used (in the class __MainMenu__) to create a convenient pop-up window that features two drop-down menus and two buttons. The drop-down menus give the user a selection of Köppen Climate Classifications (represented by corresponding countries that we’ve selected) and a selection of months, whose rainfall and average temperature is then plotted over time, as outlined previously, with the click of ‘Display Graph.’ Doing so opens another pop-up window with the aforementioned graph. Equally, the user can click on ‘Analyze Data’ to get the Pearson Correlation Coefficient, also mentioned above. For ease, this window also provides a short description of what this value represents, and how it may be interpreted. At any time, the user can change the selected Köppen classification and click either button, which replaces the current window with one displaying the updated selection.

## Instructions for Obtaining Data Sets and Running the Program

**Downloading the Data Sets**

* Create a new folder titled __datasets__ in the same directory as __main.py__
* Save the following 10 datasets in the __datasets__ folder (each link is an instant download of the respective dataset):
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/BLR/Belarus
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/BLR/Belarus
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/GRL/Greenland
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/GRL/Greenland
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/GBR/United%20Kingdom
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/GBR/United%20Kingdom
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/SAU/Saudi%20Arabia
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/SAU/Saudi%20Arabia
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/MYS/Malaysia
  - https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/MYS/Malaysia
  
**What to Expect when running main.py:**

* Before the interface opens, all of the datasets are processed. It may take up to 30 seconds. We do this so we don’t have to load the data every time a graph or analysis is done.
* The interface we designed is a graphical user interface. It can be seen in __Figure 1__ below.
* The first dropdown menu allows for the selection of a month and the second dropdown menu allows for the selection of a country.
* The __Display Graph__ button generates a graph showing how temperature and rainfall have changed over 115 years for that country. The graph is colour coded and shows two best fit lines for both temperature and rainfall data.
* The __Analyze Data__ button generates an analysis based on the Pearson correlation coefficient between temperature and rainfall for that month and country. There is also a brief description of the Pearson correlation coefficient as well as some analysis explaining the strength of the correlation between temperature and rainfall. An example graph and analysis based on January in Belarus is shown in __Figure 2__ and __Figure 3__.
* These windows will pop up for any combination that the user selects and each window will close when another combination in the menu is selected.
* An overall conclusion based on the coefficient calculated for every combination can be found in our analysis, as seen in __Figure 3__. As well, we used a function in __graph_handling__ to generate the histogram of all coefficients, though it is not included in our interface as it is not directly relevant to our research question. 

<p align="center">
<img src="https://user-images.githubusercontent.com/77357622/195244565-0341c566-be27-4907-a1e4-e3fa8ef59a6f.png" />
<br/>
Figure 1: Main Menu Interface
</p>

<br/>

<p align="center">
<img src="https://user-images.githubusercontent.com/77357622/195242636-4ac1a31f-6faf-4853-882b-498c26daf4cd.png" />
<br/>
Figure 2: Example of a Graph
</p>

<br/>

<p align="center">
<img src="https://user-images.githubusercontent.com/77357622/195241417-ec64d4ab-a85b-4a68-a615-543bde3e0e1e.png" />
<br/>
Figure 3: Example of an Analysis Window
</p>

## Project Changes

We made some changes to our initial project proposal for the final project submission, in accordance with feedback comments and improvements after further consideration. Firstly, we changed our research question to better suit our project and its outcome, as the initial question was conflicting with the ideas in the proposed computation. This new question is more general and points to correlation instead of causation, as there are many factors that contribute to both values changing over time (Akoglu, 2018). Furthermore, we decided to almost entirely change the way we approached and computed the data. We thought it was better to take the data as is, without any further aggregation, since statistically, taking the averages of existing averages may lead to inaccurate results and thus inaccurate conclusions (as the number of data points are not tracked, and each data point would have to have a different weight) (Akoglu, 2018). We also changed the structure of our computation, in that we added a GUI to allow the user to select which month and region for which they want to view the graphs and correlation. As well, upon further thought, we opted for SeaBorn and MatPlotLib instead of Plotly for added complexity. Along the same lines, we decided on using the Pandas library to store the large amounts of data that we would be manipulating. Initially, we considered using linear regression on each graph, but since this best-fit line may not be entirely accurate, we used polynomial regression. Even if this system is still not extremely accurate, it can display peaks and minimums in the graph that we can compare between the two variables, rainfall and temperature. Lastly, we cited our research as the problem was described.

## Discussion

As stated at the beginning of our project, the purpose of our program was to help us find out if there was a correlation between the monthly average temperature and monthly cumulative rainfall for all five major regions in the Köppen Climate Model. Our computation allowed us to extract the necessary data from ten datasets, which in this case was the Temperature, Rainfall and Data columns for each region, and display the distributions in a graph and also in terms of a numerical correlation coefficient. 

The graph distribution will display the temperature and rainfall axes on the left and right, respectively, and their data points are color-coded to indicate which data point belongs to which axis. Both axes are concurrently distributed over the time period - the month selected by the user for all years from 1901 to 2016. The graph also included lines of best fit for both temperature and rainfall, which helps us see the general trend of the variables over the time period - this also can help with identifying the patterns and correlation in the data. Should the lines generally follow the same trend or the inverse, then there may be a correlation present for that month for that region. As well as the graph, we also included a numerical Pearson’s correlation coefficient, which is a measure of the association between two variables. It is defined on a scale of 1 to -1, with 1 corresponding to a perfect positive relationship and -1 corresponding to a perfect negative relationship (with 0 meaning no relationship). The closer the coefficient is to 1 or -1, the stronger the relationship is. We have defined the regions for the strength of the relationship with regards to the coefficient as follows:

| Correlation Coefficient Value | Description |
| --- | --- |
| 1.0 to 0.7 | Strong Positive Correlation |
| 0.7 to 0.4 | Moderate Positive Correlation |
| 0.4 to 0.1 | Weak Positive Correlation |
| 0.1 to -0.1 | Negligible Correlation |
| -0.1 to -0.4 | Weak Negative Correlation |
| -0.4 to -0.7 | Moderate Negative Correlation |
| -0.7 to -1.0 | Strong Negative Correlation |

<p align="center">
<img src="https://user-images.githubusercontent.com/77357622/195243197-28625c40-b6cc-496d-b143-90a5622a250a.png" />
<br/>
Figure 4: Histogram
</p>

The histogram above is a distribution of the correlations for all of the different possible month and country combinations. There is a correlation between temperature and month but the magnitude and whether it is positive or negative depends on the region and the month. This is best illustrated with Great Britain. In February the correlation between temperature and rainfall was 0.43 while in August it was -0.58. This stark contrast shows how drastically the correlation can change in six months. With this being said, there does seem to be a small trend towards a negative correlation. Most of the values lie between 0 and -0.2 and there are 39 negative correlations and 21 positive correlations. Because these visualizations and numerical values were produced as a result of our computational exploration, therefore we can say that our program helped us arrive at this conclusion.

The datasets we used had some limitations. In the rainfall datasets, cumulative rainfall was recorded for each month which means a freak storm or some other factors could cause major outliers. This was best illustrated in Malaysia during January. In 2014 the rainfall was 583.79 mm and in 1979 the rainfall was 118.78. Both of these values are outliers but it helps to illustrate some of the limitations with the rainfall dataset. We can also say that Pearson’s correlation coefficient may not necessarily be the best measure to quantify correlation in this case, because if the relationship between temperature and rainfall is not linear then it is not certain we would get a correct value, and by extension interpretation. 

Moving forward, to explore this topic more we would like to look at more countries and the specific climate types within each of the Köppen Climate Model regions. This would help us gain more insight into the relationship between temperature and rainfall all over the world. We could also look at more variables than just rainfall to see what other environmental factors that temperature could affect, like natural disaster count, agricultural production, or sea level.

## References

Akoglu, Haldun. “User’s Guide to Correlation Coefficients.” PubMed Central (PMC), National Institutes of Health, 7 Aug. 2018,
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107969/

“Altered Precipitation - Conservation in a Changing Climate.” Conservation in a Changing Climate, Land Trust Alliance, 
https://climatechange.lta.org/climate-impacts/changing-water-regimes/altered-precipitation/. Accessed 12 Dec. 2020.
 
Beck, Hylke, et al. “Present and Future Köppen-Geiger Climate Classification Maps at 1-Km Resolution.” PubMed Central (PMC), National Institutes of Health, 17 Aug. 2020, 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6207062/.
 
“Download Data | World Bank Climate Change Knowledge Portal.” Homepage | World Bank Climate Change Knowledge Portal, 2016,
https://climateknowledgeportal.worldbank.org/download-data.
 
Nunez, Christina. “What Is Global Warming, Facts and Information?” National Geographic, 22 Jan. 2019, 
https://www.nationalgeographic.com/environment/global-warming/global-warming-overview/.
 
“Overview — Matplotlib 3.3.3 Documentation.” Matplotlib: Python Plotting — Matplotlib 3.3.3 Documentation, 
https://matplotlib.org/3.3.3/contents.html.
 
“Pandas.DataFrame — Pandas 1.1.5 Documentation.” Pandas - Python Data Analysis Library,
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html.
 
“Seaborn: Statistical Data Visualization — Seaborn 0.11.0 Documentation.” Seaborn: Statistical Data Visualization — Seaborn 0.11.0 Documentation,
https://seaborn.pydata.org/.
 
“Tkinter — Python Interface to Tcl/Tk — Python 3.9.1 Documentation.” 3.9.1 Documentation,
https://docs.python.org/3/library/tkinter.html.
