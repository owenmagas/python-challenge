# import sys
import pandas as pd
# import numpy as np

df = pd.read_csv("/Users/owenmagas/Documents/MDS/Level 1.1/Advanced Prtogramming For Data Analytics/"
                 "python-challenge/PyPoll/Resources/election_data.csv")
# print(df.head())

df.set_index("Voter ID", inplace=True)

print(df.head())