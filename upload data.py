
import pandas as pd

data = pd.read_csv("Survey-Survey.csv", encoding="latin1")

data = data.dropna()  # Drop rows with missing values

data.columns = [column.split("\n")[0].strip() for column in data.columns]

data.to_csv("Survey-Survey-cleaned.csv", index=False, encoding="utf-8-sig")

print(data.head())
print(data.shape)
print(data.columns.tolist())
