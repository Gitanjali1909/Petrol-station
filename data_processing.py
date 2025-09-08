import pandas as pd

def load_data(file_path):
    df = pd.read_csv("data/data-petrol.csv")
    return df

def filter_data(df, cities=None, states=None):
    if cities:
        df = df[df['City'].isin(cities)]
    if states:
        df = df[df['State'].isin(states)]
    return df

def get_top_rated_pumps(df, top_n=10):
    return df.sort_values(by='Rating', ascending=False).head(top_n)

def rating_distribution(df):
    return df['Rating'].value_counts().sort_index()

def city_state_options(df):
    states = df['State'].dropna().sort_values().unique().tolist()
    cities = df['City'].dropna().sort_values().unique().tolist()
    return cities, states
