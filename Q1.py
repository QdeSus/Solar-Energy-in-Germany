# Import the pandas library
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:/Users/Usuario/Desktop/Project 1/electricity_production.csv')

# Filter the DataFrame based on specific conditions, then group and aggregate the data
df_filt = (df.query(
    "COUNTRY in ['Germany', 'OECD Europe', 'OECD Total'] and PRODUCT in ['Solar', 'Net electricity production']")
           .groupby(['YEAR', 'PRODUCT', 'COUNTRY'])['VALUE']
           .sum()
           .unstack('PRODUCT')
           .reset_index()
           .sort_values('YEAR', ascending=True)
           )

# Calculate the percentage of solar electricity production relative to total electricity production
df_filt = df_filt.assign(**{'Solar(%)': ((df_filt['Solar'] / df_filt['Net electricity production']) * 100).round(2)})

# Extract relevant columns and reshape the DataFrame
df_question1 = df_filt[['YEAR', 'COUNTRY', 'Solar(%)', ]].set_index(['YEAR', 'COUNTRY']).unstack('COUNTRY').reset_index(
    col_level=1)

# Rename columns for clarity
df_question1.columns = df_question1.columns.map('{0[0]}_{0[1]}'.format)
df_question1.rename(columns={'Solar(%)_Germany': 'Germany (%)', 'Solar(%)_OECD Europe': 'OECD Europe (%)',
                             'Solar(%)_OECD Total': 'OECD Total (%)', "_YEAR": 'Year'}, inplace=True)

# Print the resulting DataFrame comparing solar electricity production percentages in Germany and OECD countries
print(df_question1)

# Export DataFrame to CSV file
df_question1.to_csv('Q1.csv', index=False)
