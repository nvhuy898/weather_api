import pandas as pd
import numpy as np

def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()


def save_data(data):
    df = pd.read_csv('weather.csv')
    df = df.dropna()
    if len(df.columns)==len(pd.DataFrame(pd.Series(data)).T.columns):
        df = df.append(pd.DataFrame(pd.Series(data)).T, ignore_index=True)

        df = df.dropna()
        df.to_csv('weather.csv', index=None)