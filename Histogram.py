import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data the CSV file
df = pd.read_csv('world.csv', skiprows=4)

# Selecting data for the chosen countries and years
selected_years = [str(year) for year in range(2012, 2019)]
selected_countries = ['China','India','United States','United Kingdom',\
                      'Sweden','Canada']


selected_data = df[df['Country Name'].isin(selected_countries)][[\
              'Country Name', 'Country Code', 'Indicator Name', \
                  'Indicator Code'] + selected_years]

# Extracting data for each indicator
Total_Greenhouse_Gas_Emission = selected_data[selected_data['Indicator Code']\
                                              == 'EN.ATM.GHGT.KT.CE']
Renewable_Energy_Consumption = selected_data[selected_data['Indicator Code']\
                                             == 'EG.FEC.RNEW.ZS']

# Plotting bar graphs for the first two indicators
plt.figure(figsize=(10, 9))

# Total Greenhouse Gas Emission

sns.barplot(x='Country Name', hue='variable', y='value',palette='RdBu_r', \
        data=pd.melt(Total_Greenhouse_Gas_Emission, id_vars=['Country Name'],\
                     value_vars=selected_years))
plt.xlabel('Country')
plt.ylabel('Total Greenhouse Gas Emission(kt of CO2 equivalent)')
plt.title('Total Greenhouse Gas Emission (2012-2018)')
plt.legend(title='Year')


plt.figure(figsize=(10, 9))

# Renewable Energy Consumption

sns.barplot(x='Country Name', hue='variable', y='value',palette='PuOr', \
            data=pd.melt(Renewable_Energy_Consumption ,\
                         id_vars=['Country Name'], value_vars=selected_years))
plt.xlabel('Country')
plt.ylabel('Renewable Energy Consumption(% of total final energy consumption)')
plt.title('Renewable Energy Consumption (2012-2018)')
plt.legend(title='Year')

plt.tight_layout()
plt.show()


