import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header= None)
print(df.head(4))
# print(df.tail(4))
print(df.columns)

path = './data_analytics/coursera/data/data.csv'

df.to_csv(path)