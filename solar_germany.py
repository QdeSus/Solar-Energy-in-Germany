# Import the pandas library
import pandas as pd


# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:/Users/Usuario/Desktop/Project 1/electricty_production.csv')


# Filter the DataFrame based on specific conditions, then group and aggregate the data
df_filt = (df.query("COUNTRY in ['Germany', 'OECD Europe', 'OECD Total'] and PRODUCT in ['Solar', 'Net electricity production']")
          .groupby(['YEAR', 'PRODUCT', 'COUNTRY'])['VALUE']
          .sum()  # Sum the values
          .unstack('PRODUCT')  # Unstack the 'PRODUCT' level of the index
          .reset_index()  # Reset the index of the DataFrame
          .round(2)  # Round the values to two decimal places
          .sort_values('YEAR', ascending=True)  # Sort the DataFrame by the 'YEAR' column in ascending order
          )


# Remove the column name for better display
df_filt.columns.name = None


# Rename the columns for clarity
df_filt.rename(columns={'Solar': 'Solar(GWh)', 'Net electricity production': 'Total(GWh)', 'COUNTRY': 'Country', 'YEAR': 'Year'}, inplace=True)


# Calculate the percentage of solar electricity production relative to total electricity production
df_filt = df_filt.assign(**{'Solar(%)': ((df_filt['Solar(GWh)'] / df_filt['Total(GWh)']) * 100).round(2)})


# Calculate the growth percentage of solar electricity production
df_filt['Growth(%)'] = df_filt['Solar(%)'].diff()

# Extract relevant columns and reshape the DataFrame for OECD countries
df_oecd = df_filt[['Year', 'Country', 'Solar(%)',]].set_index(['Year', 'Country']).unstack('Country').reset_index(col_level=1)


# Rename columns for clarity
df_oecd.columns = df_oecd.columns.map('{0[0]}_{0[1]}'.format)
df_oecd.rename(columns={'Solar(%)_Germany': 'Germany (%)', 'Solar(%)_OECD Europe': 'OECD Europe (%)',
                       'Solar(%)_OECD Total': 'OECD Total (%)',  '_Year': 'Year'}, inplace=True)


# Print the resulting DataFrame comparing solar electricity production percentages in Germany and OECD countries
print(df_oecd)


# Export DataFrames to CSV files (optional)
# df_oecd.to_csv('solar_germany_vs_oecd.csv', index=False)
# df_filt.to_csv('solar_germany.csv', index=False)
