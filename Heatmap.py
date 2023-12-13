# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:08:28 2023

@author: -
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from stats import skew, kurtosis

selected_countries = ['China','India','United States','United Kingdom', \
                      'Sweden','Canada']
selected_years = [str(year) for year in range(2012, 2019)]
selected_indicator_code= ['EG.FEC.RNEW.ZS','EN.ATM.CO2E.PC',\
                         'SP.URB.TOTL.IN.ZS','EN.ATM.GHGT.KT.CE', \
                            'AG.LND.FRST.ZS','EG.USE.ELEC.KH.PC','SH.DYN.MORT']


def read_world_bank_data(file_path):
    # Read the World Bank data into a DataFrame
    df = pd.read_csv(file_path, skiprows=4)
    selected_data = df[df['Country Name'].isin(selected_countries)][[ \
                        'Country Name', 'Indicator Code'] + selected_years]
    selected_data = selected_data[selected_data['Indicator Code'].isin(
                                             selected_indicator_code)]
    selected_data.set_index(['Country Name', 'Indicator Code'], inplace=True)
    return selected_data


def clean_transposed_df(df):
    # Transpose the DataFrame to have countries as columns
    df_transposed = df.transpose()

    # Drop rows with missing values
    df_transposed = df_transposed.dropna()

    return df_transposed


def create_heatmap(data, countries, indicators,country_name,indicator_name):
   
    #creating correlation matrix
    correlation_matrix = data.corr()

    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, cmap='inferno', annot=True, fmt=".2f", \
                cbar_kws={'label': 'Correlation'}, linewidths=.5)
    plt.title(f"Correlation Heatmap of "+country_name,fontsize =25)
    plt.xlabel('Indicators',fontsize =20)
    plt.ylabel('Indicators',fontsize =20)
    plt.yticks([i + 0.5 for i in range(len(indicator_name))], indicator_name)
    plt.xticks([i + 0.5 for i in range(len(indicator_name))], indicator_name)

    # Show the plot
    plt.show()
    
    plt.show()
    
    
def calculate_skewness_and_kurtosis(data):
    skewness_results = []
    kurtosis_results = []

    for column in data.columns:
        # Skip columns that are not numeric
        if pd.api.types.is_numeric_dtype(data[column]):
            # Calculate skewness and kurtosis using the provided functions
            column_data = data[column].dropna()
            skewness = skew(column_data)
            kurt = kurtosis(column_data)

            # Append results to the lists
            skewness_results.append((column, skewness))
            kurtosis_results.append((column, kurt))

            print(f"Column: {column}")
            print(f"Skewness: {skewness}")
            print(f"Kurtosis: {kurt}\n")

    return skewness_results, kurtosis_results
    

def main():
    file_path = 'world.csv'

    # Read World Bank data into a DataFrame
    world_bank_df = read_world_bank_data(file_path)

    # Clean and transpose the DataFrame
    transposed_df = clean_transposed_df(world_bank_df)
    df_years = transposed_df.copy()

    # Split the DataFrame into two DataFrames
    df_countries = world_bank_df.copy()
  

    # Assuming df_years is your existing DataFrame

    # give desired country name for heatmap
    country_name = 'United Kingdom'
    country_values_df = df_years[country_name]
    mean_country_values = country_values_df.mean()
   
    
    # Display the new DataFrame with only the values for country name
    print(country_values_df)
    indicator_name =  ['Renewable Energy Consumption',\
                       'Total Greenhouse Gas Emission','Urban Population',\
                'CO2 Emission','Forest Area','Electric power consumption', \
                       'Mortality Rate']

    
    create_heatmap(country_values_df, selected_countries, \
                   selected_indicator_code,country_name,indicator_name)


if __name__ == "__main__":
    main()
