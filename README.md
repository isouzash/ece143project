# ECE143project

The objective of this project is to create a system to analyze the air quality base on it location, time and level of gas contain in the air. The data that we use is “pollution in the US” open dataset from kaggle. The size of the csv file is 382mb.

The notebook should be run as "Run all" at once.
We used a code to download the zip file from the url: https://www.kaggle.com/sogun3/uspollution/downloads/uspollution.zip/1
If cannot read from URL, please ensure to download the zip file prior to run the code by clicking in the url. 
The code for unzip and save csv to a dataframe is working fine in our notebook.
The notebook presents the code for data manipulation and how the the plots were generated.
The .py files correspond to functions to plot our graphs (make_plots.py) and manupulate our dataset (my_methods).

We used requests to upload the zip file in kaggle website. We used zipfile and pandas to load the csv file.
We used pandas for data visualization and to filter the data. We used numpy and pandas to insert a new column in our dataset (EPA classification). We used pandas and matplotlib to generate the plots.

Plots (see details of the code in the .py files):
The inputs of the plot functions are filtered data using pandas.
- Bar plot with top 10 states with highest AQI from 2011 to 2015(make_bar_plot in make_plots.py)
- Pie charts comparing EPA categories in California and USA(plot32 in make_plots.py)
- Bar plot of the number of annual measurements per state(plot33 in make_plots.py)
- EPA categories of air quality measurements per year(plot34 in make_plots.py)
- Stack bar plot of EPA categories per year in California, top polluted cities in California, San Diego, Los Angeles and Fresno(plot34 in make_plots.py)
- Annual average of pollutants AQI over time in San Diego, Los Angeles, Fresno and Long Beach (For O3, NO2, SO2 and CO)(plot35 in make_plots.py)
- Pie chart comparison between top 4 pollutant gas,O3, NO2, SO2 and CO, with the % of pollutants contain in US air (plot36 in make_plots.py)
 
