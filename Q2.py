import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Usuario/Desktop/Project 1/electricity_production.csv')

# Filter the DataFrame based on specific conditions, then group and aggregate the data
df_question2 = (df.query("PRODUCT in ['Solar', 'Net electricity production'] and YEAR > 2017 and COUNTRY not in ['Costa "
                    "Rica', 'Iceland','OECD Total','IEA Total', 'OECD Americas','OECD Europe','OECD Asia Oceania']")
                .groupby(['COUNTRY', 'PRODUCT'])['VALUE']
                .sum()
                .unstack('PRODUCT')
                .reset_index()
                .round(2)
                )
# Remove the name of the columns' index
df_question2.columns.name = None

# Rename the columns for clarity
df_question2.rename(columns={'Solar': 'Solar(GWh)', 'Net electricity production': 'Total(GWh)', 'COUNTRY': 'Country'},
                    inplace=True)

# Calculate the percentage of solar energy
df_question2 = df_question2.assign(**{'Solar(%)': ((df_question2['Solar(GWh)'] / df_question2['Total(GWh)']) * 100).round(2)})

# Sort the DataFrame by the column 'Solar(%)' in descending order and printing the result
print(df_question2.sort_values('Solar(%)', ascending=False))

# Export DataFrames to CSV file
df_question2.to_csv('Q2.csv', index=False)
