import pandas as pd

# Reading the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Usuario/Desktop/Project 1/electricty_production.csv')

# Filtering the DataFrame based on specific conditions, calculating the total, and reshaping the data
df_filt = (df.query("PRODUCT in ['Solar', 'Net electricity production'] and YEAR > 2017 and COUNTRY not in ['Costa "
                    "Rica', 'Iceland','OECD Total','IEA Total', 'OECD Americas','OECD Europe','OECD Asia Oceania']")
           .groupby(['COUNTRY', 'PRODUCT'])['VALUE']
           .sum()
           .unstack('PRODUCT')
           .reset_index()
           .round(2)
           .sort_values('Net electricity production', ascending=False)
           )
# Removing the name of the columns' index
df_filt.columns.name = None

# Renaming the columns 'Solar' and 'Net electricity production'
df_filt.rename(columns={'Solar': 'Solar(GWh)', 'Net electricity production': 'Total(GWh)', 'COUNTRY': 'Country'}, inplace=True)

# Calculating the percentage of 'mean_solar' relative to 'mean_total' and assigning it to a new column 'solar_pct'
df_filt = df_filt.assign(**{'Solar(%)': ((df_filt['Solar(GWh)'] / df_filt['Total(GWh)']) * 100).round(2)})

# Sorting the DataFrame by the column 'solar_pct' in descending order and printing the result
print(df_filt.sort_values('Solar(%)', ascending=False))
#df_filt.to_csv('solar_vs_total.csv', index=False)