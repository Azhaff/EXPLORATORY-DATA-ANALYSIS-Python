# Exploratory Data Analysis

This project involves analyzing the Earth Surface Temperature dataset using Pandas and NumPy. The analysis includes handling missing values, ensuring data type consistency, exploring temperature trends and anomalies, and visualizing key insights.

## Features

1. **Data Loading and Preparation**:
    - Import and load the Earth Surface Temperature dataset.
    - Identify and rectify missing values by replacing them with the mean.
    - Ensure data types of all columns are consistent with their values.
    - Transform the Year and Month columns into a single "Date" column in MM-YYYY format.

2. **Outlier Detection**:
    - Detect extreme temperature values that might be regarded as outliers using box plots.

3. **Summary Statistics**:
    - Compute summary statistics for temperature, monthly variation, and anomaly values including mean, median, standard deviation, and range.
    - Compute the 25th, 50th, and 75th percentiles.

4. **Country Analysis**:
    - Identify the countries included in the dataset and calculate their average temperature values.

5. **Global Temperature Trends**:
    - Determine the overall trend in global temperatures over the years and visualize this trend using line charts.

6. **Monthly Temperature Analysis**:
    - Identify the warmest and coldest months on average globally.
    - Explore the variation in temperature anomalies on a monthly basis and identify any months with consistently high or low anomalies.

7. **Country Comparison**:
    - Compare the trends in temperatures for five selected countries over the years to find similar temperature patterns.

8. **Historical Data Analysis**:
    - Determine how many years back the data extends.
    - Compare average temperatures for the first and most recent years in the dataset.
    - Calculate the average temperature for each year and each month over the period covered by the dataset.

9. **Correlation and Seasonality**:
    - Explore the correlation between temperature and monthly variation or anomaly values using correlation coefficients and scatter plots.
    - Visualize seasonality in temperature values by creating a heat map of average temperatures by month and year using the Seaborn library.

## Prerequisites

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/earth-surface-temperature-analysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd earth-surface-temperature-analysis
    ```
3. Ensure the dataset is placed in the project directory with the filename `earth_surface_temperatures - earth_surface_temperatures.csv`.
4. Run the script:
    ```sh
    python analysis_script.py
    ```

## Code Explanation

- **Data Loading and Preparation**:
    ```python
    import pandas as pd
    import numpy as np
    df = pd.read_csv('earth_surface_temperatures - earth_surface_temperatures.csv')
    df.fillna(df.mean(), inplace=True)
    df['dt'] = pd.to_datetime(df['dt'])
    ```

- **Outlier Detection**:
    ```python
    df.boxplot()
    ```

- **Summary Statistics**:
    ```python
    df.describe()
    ```

- **Country Analysis**:
    ```python
    df['Country'].unique()
    ```

- **Global Temperature Trends**:
    ```python
    df['LandAverageTemperature'].plot()
    ```

- **Monthly Temperature Analysis**:
    ```python
    df.groupby('Month')['LandAverageTemperature'].mean()
    ```

- **Country Comparison**:
    ```python
    df[df['Country'] == 'CountryName1']['LandAverageTemperature'].plot.line(x='dt', y='LandAverageTemperature')
    df[df['Country'] == 'CountryName2']['LandAverageTemperature'].plot.line(x='dt', y='LandAverageTemperature')
    ```

- **Historical Data Analysis**:
    ```python
    df['dt'].min()
    df['dt'].max()
    df.groupby('dt')['LandAverageTemperature'].mean()
    df.groupby('Month')['LandAverageTemperature'].mean()
    ```

- **Correlation and Seasonality**:
    ```python
    df.corr()
    import seaborn as sns
    sns.heatmap(df.corr(), annot=True)
    ```

## Results

The analysis provides insights into global temperature trends, identifies outliers and anomalies, and explores correlations between temperature and other variables. The visualizations help in understanding the seasonality and long-term trends in Earth's surface temperatures.
