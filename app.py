import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import dates
import json
import requests






st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('  ⛅🌞🌅⚡💧💦💨❄🌈')
st.title('Trạm theo dõi thời tiết (Nhóm 1)')

df=pd.read_csv('weather.csv')
df = df.rename(columns={"vi_do": "lat", "kinh_do": "lon"}, errors="raise")
st.map(df)

# @st.cache
def load_data(city):
    print(city)
    r= requests.request("POST",f"http://127.0.0.1:9999/get_weather/{city}" )
    print(f"http://127.0.0.1:9999/get_weather/{city}")
    df=json.loads(r.content)
    
    return df

# data_load_state.text("Done! (using st.cache)")

# st.title(f"📅 Today is : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%Y-%m-%d')} {data.thoi_gian.dt.hour[n]}h")
st.header("🌐 Chọn thành phố bạn muốn xem")
place = st.text_input("Nhập tên thành phố  ", "")
b = st.button("SUBMIT")
st.set_option('deprecation.showPyplotGlobalUse', False)


def weather_detail(place="hanoi"):
    data = load_data(place)
    data=pd.DataFrame(data)
    data.thoi_gian= pd.to_datetime(data.thoi_gian)
    if st.checkbox('Hiện dữ liệu thô'):
        st.subheader('Dữ liệu thô')
        st.write(data)
    
    # du lieu hien tai
    n=len(data)-1

    st.title(f"📅 {data.ten[n].upper()} : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%m/%d/%Y ')} ")
    df = pd.DataFrame(
     np.array([[data.vi_do[n],data.kinh_do[n]]]),
     columns=['lat', 'lon'])

    st.map(df) 


    st.write(f"### 🌡 Nhiệt độ: {(data.nhiet_do[n])} ℃ 🌡")
    st.write(f"### 💧 Độ ẩm: {int(data.nhiet_do[n])}% 💧")
    st.write(f"### 📍 Áp suất: {(data.ap_suat[n])} Pa 📍")
    st.write(f"### 💨 Hướng gió: {int(data.huong_gio[n])}💨")
    st.write(f"### 💨 Vận tốc gió: {(data.toc_do_gio[n])} km/h💨")

    plot_T(data)


def plot_T(data):

    rcParams['figure.figsize'] = 6, 4
    plt.plot(data.thoi_gian, data.nhiet_do, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(data.thoi_gian+pd.Timedelta(hours=17), data.nhiet_do, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    # plt.ylim(min(min_t) - 4, max(max_t) + 4)
    # plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%Hh')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.legend(["Nhiệt độ đo được", "Nhiệt độ dự đoán"], loc=1)
    plt.xlabel('Thời gian (h)')
    plt.ylabel('Nhiệt độ (℃)')
    plt.title('Biểu đồ nhiệt độ')

    st.pyplot()
    plt.clf()

    rcParams['figure.figsize'] = 6, 4
    plt.plot(data.thoi_gian, data.do_am, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(data.thoi_gian+pd.Timedelta(hours=17), data.do_am, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    # plt.ylim(min(min_t) - 4, max(max_t) + 4)
    # plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%Hh')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.legend(["Đo được", "Dự đoán"], loc=1)
    plt.xlabel('Thời gian (h)')
    plt.ylabel('Độ ẩm (%)')
    plt.title('Biểu đồ độ ẩm')

    st.pyplot()
    plt.clf()

if b:
    if place != "":
        # try:
            weather_detail(place)

        # except :
        #     st.write("Vui lòng điền chính xác địa chỉ thành phố !!!")







# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)