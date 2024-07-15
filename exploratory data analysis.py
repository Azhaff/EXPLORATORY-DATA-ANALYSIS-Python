#import pandas and numpy as pd and np respectively
import pandas as pd
import numpy as np
#read the csv file
df = pd.read_csv('earth_surface_temperatures - earth_surface_temperatures.csv')
#Identify and rectify any missing values in the data using appropriate techniques.
#check for missing values
df.isnull().sum()
#replace missing values with the mean
df.fillna(df.mean(), inplace=True)
#Ensure that the data types of all columns are consistent with their values and make conversions where necessary.
#check the data types
df.dtypes
#Transform the Years and Month columns into a single column labeled "Date" in the MM-YYYY format, with a datetime64[ns] datatype. For example, the year 1848 and month 5 should be unified as a single value, such as 5-1848.
#convert the year and month columns to datetime
df['dt'] = pd.to_datetime(df['dt'])
#Detect and investigate extreme temperature values that might be regarded as outliers.
#check for outliers 
df.boxplot()
#Compute summary statistics for temperature, monthly variation, and anomaly values, including mean, median, standard deviation, and range. Also, compute the 25th, 50th, and 75th percentiles.
#compute the summary statistics
df.describe()
#Identify the countries included in the dataset and calculate their average temperature values.
#check the countries
df['Country'].unique()
#Determine the overall trend in global temperatures over the years and visualize this trend using a suitable chart.
#check the trend in global temperatures
df['LandAverageTemperature'].plot()
#Determine the months of the year that are warmest and coldest on average globally.
#check the warmest months
df['Month'].max()
#check the coldest months
df['Month'].min()
#Explore the variation in temperature anomalies on a monthly basis and identify any months with consistently high or low anomalies across the years.
#check the variation in temperature anomalies on a monthly basis
df['LandAverageTemperatureAnomaly'].plot()
#Choose five countries and compare the trends in their temperatures over the years, seeking any similar temperature patterns.


#Determine how many years back the data extends. Explore and compare the average temperatures for the first year recorded and the most recent year in the dataset.
#check the first year recorded
df['dt'].min()
#check the most recent year in the dataset
df['dt'].max()
#Determine the average temperature for each year over the period covered by the dataset.
#check the average temperature for each year over the period covered by the dataset
df.groupby('dt')['LandAverageTemperature'].mean()

#Determine the average temperature for each month over the period covered by the dataset.
#check the average temperature for each month over the period covered by the dataset
df.groupby('Month')['LandAverageTemperature'].mean()
#Explore the potential correlation between temperature and monthly variation or anomaly values. Calculate correlation coefficients and create scatterplots to investigate this relationship.

#Explore the seasonality in temperature values by creating a heat map of average temperatures by month and year. You may use the seaborn library to create the heat map.
#check the seasonality in temperature values by creating a heat map of average temperatures by month and year
import seaborn as sns
sns.heatmap(df.corr(), annot=True)