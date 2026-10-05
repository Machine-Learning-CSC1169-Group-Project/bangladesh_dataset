
import pandas as pd

data = pd.read_csv("Survey-Survey.csv", encoding="latin1")

print(data.head())
print(data.shape)
print(data.columns)
print(data.info())
