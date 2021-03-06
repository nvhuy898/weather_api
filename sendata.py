
import threading #Thư viện lập trình với luồng
import random
import requests
import time
import numpy as np
import json
import time
from utils import *

config= get_config('config.yml')
ip_host=config['ip_host']

def send_data():

    while True:
        t=time.gmtime()
        cities =['danang', 'hanoi', 'haiphong','hue', 'london', 'seoul ', 'tokyo', 'bangkok' ]
        print(t.tm_sec)
        if (t.tm_sec==0):
            for city in cities:
                data=get_weather(city)
                # data= {
                #     "ID": 1581130.0,
                #     "ten": "iot",
                #     "quoc_gia": "VN",
                #     "kinh_do": 105.8412,
                #     "vi_do": 21.0245,
                #     "thoi_gian": "Fri Apr 15 18:01:01 2022",
                #     "nhiet_do": 27.0,
                #     "do_am": 79.0, 
                #     "ap_suat": 1006.0,
                #     "huong_gio": 136.0,
                #     "toc_do_gio": "5.67"
                # }
                data=json.dumps(data)
                print(data)
                r= requests.request("POST",f"http://{ip_host}:9999/weather", data=data)
            
                print(f'Gửi dữ liệu tại {city}, {time.ctime(time.time())}')
        time.sleep(1) 


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=b21a2633ddaac750a77524f91fe104e7"
    r = requests.get(url).json()
    weather = {
            'ID' : r['id'],
            'ten': city,
            'kinh_do': r['coord']['lon'],
            'vi_do': r['coord']['lat'],
            'thoi_gian': time.ctime(),
            'nhiet_do' : r['main']['temp'],
            'do_am' : r['main']['humidity'],
            'ap_suat' : r['main']['pressure'],
            'huong_gio': r['wind']['deg'],
            'toc_do_gio': r['wind']['speed'],
            'quoc_gia': r['sys']['country']

        }
    return weather

if __name__ == '__main__':
 send_data()