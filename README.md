# Solar Energy Study

## Data Source:
- [Monthly Electricity Production in GWh 2010-2022](https://www.kaggle.com/datasets/ccanb23/iea-monthly-electricity-statistics?resource=download)

## Questions to answer:
- What is the annual percentage of Germany's total electricity generated by solar energy from 2010 to 2022, and how do these figures deviate from the OECD average?
- Which countries in Europe generated a higher percentage of solar energy relative to their total generated energy between 2017 and 2022?

## Exploration of the table (SQL BigQuery):
The electricity production values are mixed in the VALUE column, where data from solar energy production, total production, and distribution losses are included. To determine which parameter the VALUE column refers to, we need to look at the associated values in the PRODUCT column. The only data of interest for the study, which will help us answer the questions, will be found in the VALUE column when PRODUCT = "Net electricity production" and when PRODUCT = "Solar". We will exclude "OECD Total", "IEA Total", "OECD Americas", "OECD Europe", "OECD Asia Oceania" as they are sets of countries rather than specific countries.

## Data Cleaning and Verification (SQL BigQuery)
- In the COUNTRY column, there are 52 distinct values corresponding to countries or groups of countries, and only 2 of them have incomplete data for "Solar" and "Net electricity production" in the last 5 years (Costa Rica and Iceland) (Figure 1).
- Some averages might be biased, as missing data for certain years for certain countries could also lead to missing data for certain months. This was not the case, as all countries had data for each month during the last 5 years for both "Solar" and "Net electricity production". Additionally, none of these monthly data points are 0 (Query result: 6000 = 5 years * 50 countries * 12 months * 2 values Solar and Total) (Figure 2).
- Germany has data from 2010 to 2022 for all months, and in none of the cases, the value is 0 (Figure 3).

## Analysis and creation of necessary tables for visualization (Python Pandas)
- Create a table showing how much electricity each country produced between 2018 and 2022 (inclusive) in total and from solar energy, along with a column reflecting the percentage of the total that solar energy represented (Figure 4).
- Create a table showing, for Germany, for all years from 2010 to 2022, the total electricity production, total electricity production from solar energy, the ratio between the two, and the annual increase in this ratio. Additionally, create a table comparing the % of solar energy in Germany with that of OECD Europe and OECD Total (Figure 5).

![Ejemplo de imagen](visualizations/Viz1.png)
