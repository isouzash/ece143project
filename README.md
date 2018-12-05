# ece143project

The notebook should be run as "Run all" at once.
We used a code to download the zip file from the url: https://www.kaggle.com/sogun3/uspollution/downloads/uspollution.zip/1
The code sometimes works, sometimes not. If the zip file is not downloaded when you run the code, please download it clicking in the url. 
The code for unzip and save csv to a dataframe is working fine in our notebook.
The notebook presents the code for data manipulation and how the the plots were generated.
The .py files correspond to functions to plot our graphs.

We used requests to upload the zip file in kaggle website. We used zipfile and pandas to load the csv file.
We used pandas for data visualization and to filter the data. We used numpy and pandas to insert a new column in our dataset (EPA classification). We used pandas and matplotlib to generate the plots.

Plots:
- Bar plot with top 10 states with highest AQI from 2011 to 2015
- Pie charts comparing EPA categories in California and USA
- Bar plot of the number of annual measurements per State
- EPA categories of air quality measurements per year
- Stack bar plot of EPA categories per year in California, top polluted cities in California, San Diego, Los Angeles and Fresno
- Annual average of pollutants AQI over time in San Diego, Los Angeles, Fresno and Long Beach (For O3, NO2, SO2 and CO)
- Pie chart with the % of pollutants in US air 
