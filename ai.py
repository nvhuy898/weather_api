import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow import keras
from collections import deque

class AI():
    def __init__(self):
        self.model_nhiet_do=keras.models.load_model('./weights/nhiet_do.h5')
    

    def du_doan_nhiet_do(self, df):
        X=deque(list(df.nhiet_do), maxlen=12)
        y=[]
        for i in range(6):
            p=(self.model_nhiet_do.predict(np.array([list(X)]))[0][0])
            y.append(int(p))
            X.append(p)
        return y



        