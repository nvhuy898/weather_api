import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import dates
import json
import requests


st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('⛅🌞🌅⚡💧💦❄🌈')
st.title('Trạm theo dõi thời tiết (Nhóm 1)')

DATE_COLUMN = 'date'

DATA_URL = ('weather.csv')
# @st.cache
def load_data(city):
    print(city)
    r= requests.request("POST",f"http://127.0.0.1:9999/get_weather/{city}" )
    print(f"http://127.0.0.1:9999/get_weather/{city}")
    df=json.loads(r.content)
    df=pd.DataFrame(df)
    df.thoi_gian= pd.to_datetime(df.thoi_gian)
    return df

# data_load_state.text("Done! (using st.cache)")

# st.title(f"📅 Today is : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%Y-%m-%d')} {data.thoi_gian.dt.hour[n]}h")
st.header("🌐 Chọn thành phố bạn muốn")
place = st.text_input("Nhập tên thành phố 🌆 ", "")
b = st.button("SUBMIT")
st.set_option('deprecation.showPyplotGlobalUse', False)


def weather_detail(place="hanoi"):
    data = load_data(place)
    
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
    
    # du lieu hien tai
    n=len(data)-1

    st.title(f"📅 {place.upper()} : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%Y-%m-%d')} ")


    st.write(f"### Nhiệt độ: {(data.nhiet_do[n])} ℃")
    st.write(f"### Độ ẩm: {int(data.nhiet_do[n])}%")
    st.write(f"### Áp suất: {int(data.ap_suat[n])} Pa")
    st.write(f"### Hướng gió: {int(data.huong_gio[n])}")
    st.write(f"### Vận tốc gió: {int(data.toc_do_gio[n])} km/h")

    
    st.write("### ▶️Mưa giông rải rác☔!!")
    days = []
    dates_2 = []
    min_t = []
    max_t = []
    # for i in range(24*1):
        
    #     day = data.thoi_gian[n-i]
    #     date1 = day.strftime("%d/%m")
    #     if date1 not in dates_2:
    #         dates_2.append(date1)
    #         min_t.append(None)
    #         max_t.append(None)
    #         days.append(date1)
    #     temperature = data.nhiet_do[n-i]
    #     if not min_t[-1] or temperature < min_t[-1]:
    #         min_t[-1] = temperature
    #     if not max_t[-1] or temperature > max_t[-1]:
    #         max_t[-1] = temperature
    # st.write(f"## 📆 Ngày :  Max - Min  (℃)")

    # for i in range(len(days)):
    #     # ta = (obj.strftime("%d/%m"))
    #     st.write(f'### ➡️ {days[i]} :\t   ({max_t[i]} - {min_t[i]})')
    #     i += 1
    # plot_line(days, min_t, max_t)
    plot_T(data)


def plot_T(data):
    # days = dates.thoi_gian2num(days)
    rcParams['figure.figsize'] = 6, 4
    plt.plot(data.thoi_gian, data.nhiet_do, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(data.thoi_gian+pd.Timedelta(minutes=12), data.nhiet_do, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    # plt.ylim(min(min_t) - 4, max(max_t) + 4)
    # plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%Mh')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.legend(["Nhiệt độ đo được", "Nhiệt độ dự đoán"], loc=1)
    plt.xlabel('Thời gian (h)')
    plt.ylabel('Nhiệt độ (℃)')
    plt.title('Biểu đồ nhiệt độ')

    st.pyplot()
    plt.clf()

    rcParams['figure.figsize'] = 6, 4
    print(data.thoi_gian)
    plt.plot(data.thoi_gian, data.do_am, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(data.thoi_gian+pd.Timedelta(minutes=12), data.do_am, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    # plt.ylim(min(min_t) - 4, max(max_t) + 4)
    # plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%Mh')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.legend(["Đo được", "Dự đoán"], loc=1)
    plt.xlabel('Thời gian (h)')
    plt.ylabel('Độ ẩm (%)')
    plt.title('Biểu đồ độ ẩm')

    st.pyplot()
    plt.clf()

if b:
    if place != "":
        try:
            weather_detail(place)

        except :
            st.write("Vui lòng điền chính xác địa chỉ thành phố !!!")







# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)