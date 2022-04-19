import pandas as pd
import numpy as np
import yaml
def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()


def save_data(data):
    if data['ten']=='iot':
        thoi_gian=data['thoi_gian']
        # t=np.array(thoi_gian.replace("[","").replace("]","").split(", ")).astype(int)
        t=thoi_gian
        from datetime import datetime
        d = datetime(t[0],t[1],t[2],t[3],t[4],t[5],)+ pd.Timedelta(hours=7)
        data['thoi_gian']=d.strftime("%a %b %d %H:%M:%S %Y")
    
    df = pd.read_csv('weather.csv')
    df = df.dropna()
    if len(df.columns)==len(pd.DataFrame(pd.Series(data)).T.columns):
        df = df.append(pd.DataFrame(pd.Series(data)).T, ignore_index=True)

        df = df.dropna()
        df.to_csv('weather.csv', index=None)
        return True
    else:
        return False



def get_config(config_path: str):
    if config_path.endswith("json"):
        with open(config_path, 'r') as f:
            config = json.load(f)
    elif config_path.endswith("yml"):
        with open(config_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    return config
