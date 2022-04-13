
import threading #Thư viện lập trình với luồng
import random
import requests
import time
import numpy as np
import json
 #Thư viện tạo số ngẫu nhiên
def send_data():
    threading.Timer(10,send_data).start() #Tạo luồng
    city = np.random.choice(['hanoi','hue', 'danang','haiphong'])
    data=get_weather(city)
    data=json.dumps(data)
    # print(data)
    r= requests.request("POST","http://127.0.0.1:9999/weather", data=data)
    
    print(f'send data {city}')

#     print(r.apparent_encoding)
# # print(r.content)
#     print(r.encoding)
#     print(r.cookies)
    # print(r.elapsed)
#     print(r.encoding)
#     print(r.headers)
#     print(r.history)
#     print(r.is_permanent_redirect)
#     print(r.iter_content())
#     print(r.links)
#     # print(r.raise_for_status())
    # print(r.json())



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