import pandas as pd

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
path = './data_analytics/coursera/import_export/data/data.csv'
df = pd.read_csv(path, header= None)
# print(df.head(4))
# print(df.tail(4))
print(df.columns)
print(df.dtypes)
print(df.describe)
print(df.describe(include='all'))
# path = './data_analytics/coursera/import_export/data/data.csv'

# df.to_csv(path)