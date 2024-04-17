# Solar Energy Study

__## Data Source__
- [Monthly Electricity Production in GWh 2010-2022](https://www.kaggle.com/datasets/ccanb23/iea-monthly-electricity-statistics?resource=download)

__## Questions to answer__
1. What percentage of Germany's total electricity production came from solar energy between 2010 and 2022, and how do these figures deviate from the OECD average?
2. Out of the countries for which we have data, which ones generated a higher percentage of solar energy relative to their total generated energy between 2017 and 2022?

__## Step-by-step procedure__

## 1. Comprehensive exploration of the data in BigQuery
In order to understand the structure of the data and prepare for the analysis I used some basic SQL queries and came to the following conclusions:
- The "VALUE" column shows the numerical data with which we can work in decimal form and with GWh as the unit of measure. This value is always associated with a particular "PRODUCT" in a particular "MONTH" of a particular "YEAR" in a particular "COUNTRY". 
- The "PRODUCT" column determines what type of parameter the value in the "VALUE" column refers to. There are a total of 27 different types of "PRODUCT" and some examples are "Total exports", "Distribution losses", "Wind", "Oil", "Used for pumped storage", "Renewables", etc. The only ones of interest for the project are "Net electricity production" and "Solar" so we will need to filter the data in order to only get the results for these two types of "PRODUCT".
- The "share" column shows the percentage of the "Net electricity production" which each value in the "VALUE" column represents (for the rows where "PRODUCT" = "Net electricity production", the value in the column "share" is 1). Since we want to obtain the data annually instead of monthly, this column will not help us as much as we might intuitively think. If we were to average the monthly values in this column we would not get the real annual share value, as the monthly values would not be properly weighted. For example, the value corresponding to the month in which the "Net electricity production" is the maximum should have more weight in the annual average than the value corresponding to the month in which the "Net electricity production" is the minimum. The way to correctly make the annual share is to add up all the monthly values and then make the percentage of the two totals.
- In the column "COUNTRY" we find values such as "OECD Total", "IEA Total", "OECD Americas", "OECD Europe" or "OECD Asia Oceania". We will exclude them when working on answering question 2 as they are sets of countries rather than specific countries.

## 2. Data Cleaning and Verification (SQL BigQuery)
- In the COUNTRY column, there are 52 distinct values corresponding to countries or groups of countries, and only 2 of them have incomplete data for "Solar" and "Net electricity production" in the last 5 years (Costa Rica and Iceland) (Figure 1).
- Some averages might be biased, as missing data for certain years for certain countries could also lead to missing data for certain months. This was not the case, as all countries had data for each month during the last 5 years for both "Solar" and "Net electricity production". Additionally, none of these monthly data points are 0 (Query result: 6000 = 5 years * 50 countries * 12 months * 2 values Solar and Total) (Figure 2).
- Germany has data from 2010 to 2022 for all months, and in none of the cases, the value is 0 (Figure 3).

## 3. Analysis and creation of necessary tables for visualization (Python Pandas)
- Create a table showing how much electricity each country produced between 2018 and 2022 (inclusive) in total and from solar energy, along with a column reflecting the percentage of the total that solar energy represented [(Figure 4)](solar_vs_total.py).
- Create a table showing, for Germany, for all years from 2010 to 2022, the total electricity production, total electricity production from solar energy, the ratio between the two, and the annual increase in this ratio. Additionally, create a table comparing the % of solar energy in Germany with that of OECD Europe and OECD Total [(Figure 5)](solar_germany.py).

![Ejemplo de imagen](visualizations/Viz1.png)
