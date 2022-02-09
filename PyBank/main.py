import sys
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/owenmagas/Documents/MDS/Level 1.1/Advanced Prtogramming For Data Analytics/"
                 "python-challenge/PyBank/Resources/budget_data.csv")
# print(df.head())

# df.set_index("Date", inplace=True)
number_of_months = df['Date'].unique()
# print(len(number_of_months))
#print(df.info())
#print(df['Profit/Losses'].sum())


