
#Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Read CSV file
world_data = pd.read_csv('World.csv', skiprows=4)

# choose the countries and years
selected_countries = ['China','India','United States','United Kingdom',
                      'Sweden','Canada']
selected_years = [str(year) for year in range(2012, 2019)]

selected_data = world_data[world_data['Country Name'].isin(selected_countries)][['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + selected_years]

# Extracting data for each indicator
urban_population = selected_data[selected_data['Indicator Code'] == 
                                 'SP.URB.TOTL.IN.ZS']

CO2_emission = selected_data[selected_data['Indicator Code'] == 'EN.ATM.CO2E.PC']


# Assuming urban_population and CO2_emission are your datasets

# Plotting line graph for the first indicator
plt.figure(figsize=(12, 10))

# urban_population
for country in urban_population['Country Name'].unique():
    country_data = urban_population[urban_population['Country Name'] ==
                                    country]
    plt.plot(selected_years, country_data[selected_years].values.flatten(), 
             label=country, linestyle='--')

plt.xlabel('Year',fontsize=20)
plt.ylabel('Urban Population(% of total population)',fontsize=20)
plt.title('Urban Population (2012-2018)',fontsize=25)
plt.legend(title='Country')
plt.grid(True)

# Plotting line graph for the second indicator
plt.figure(figsize=(12,10))

# CO2_emission 
for country in CO2_emission ['Country Name'].unique():
    country_data = CO2_emission [CO2_emission ['Country Name'] == country]
    plt.plot(selected_years, country_data[selected_years].values.flatten(),
             label=country, linestyle='--')

plt.xlabel('Year',fontsize=20)
plt.ylabel('CO2 Emissions (metric tons per capita)',fontsize=20)
plt.title('CO2 Emission (2012-2018)',fontsize=25)
plt.legend(title='Country')
plt.grid(True)

plt.tight_layout()
plt.show()


