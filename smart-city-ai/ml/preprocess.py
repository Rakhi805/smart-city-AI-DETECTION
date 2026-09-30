import pandas as pd
def load_data(path='data/city_data.csv'):
    return pd.read_csv(path).dropna()
