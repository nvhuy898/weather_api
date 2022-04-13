import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import dates
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('⛅🌞🌅⚡💧💦❄🌈')
st.title('Trạm theo dõi thời tiết (Nhóm 1)')

DATE_COLUMN = 'date'

DATA_URL = ('weather.csv')
# @st.cache
def load_data(nrows):
    data_load_state = st.text('Loading data...')
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data.astype({'temp': 'int32'})
    data['thoi_gian'] = pd.to_datetime(data['thoi_gian'])
    return data


data = load_data(50)

# data_load_state.text("Done! (using st.cache)")
# choice today
n=10
# st.title(f"📅 Today is : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%Y-%m-%d')} {data.thoi_gian.dt.hour[n]}h")
st.header("🌐 Chọn thành phố bạn muốn")
place = st.text_input("tên thành phố 🌆 ", " ")
b = st.button("SUBMIT")
st.set_option('deprecation.showPyplotGlobalUse', False)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data[n-12:n+12])
def weather_detail(place="Ha noi"):
    st.title(f"📅 {place} is : {data.thoi_gian[n].day_name()} {data.thoi_gian[n].strftime('%Y-%m-%d')} {data.thoi_gian.dt.hour[n]}h")


    st.write(f"## Nhiệt độ: {int(data.nhiet_do[n])} ℃")
    # st.write(f"## Độ ẩm: {int(data.nhiet_do[n])}%")
    st.write(f"## Độ ẩm: {80}%")
    st.write("## ▶️Mưa giông rải rác☔!!")
    days = []
    dates_2 = []
    min_t = []
    max_t = []
    for i in range(24*6):
        
        day = data.thoi_gian[n-i]
        date1 = day.strftime("%d/%m")
        if date1 not in dates_2:
            dates_2.append(date1)
            min_t.append(None)
            max_t.append(None)
            days.append(date1)
        temperature = data.nhiet_do[n-i]
        if not min_t[-1] or temperature < min_t[-1]:
            min_t[-1] = temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1] = temperature
    st.write(f"## 📆 Ngày :  Max - Min  (℃)")

    for i in range(len(days)):
        # ta = (obj.strftime("%d/%m"))
        st.write(f'### ➡️ {days[i]} :\t   ({max_t[i]} - {min_t[i]})')
        i += 1
    plot_line(days, min_t, max_t)
    plot_T()


def plot_line(days, min_t, max_t):
    # days = dates.thoi_gian2num(days)
    rcParams['figure.figsize'] = 6, 4
    plt.plot(days, max_t, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(days, min_t, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    plt.ylim(min(min_t) - 4, max(max_t) + 4)
    plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.thoi_gianFormatter('%d/%m')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.grid(True, color='brown')
    plt.legend(["Nhiệ độ cao nhất", "Nhiệt độ thấp nhất"], loc=1)
    plt.xlabel('Ngày')
    plt.ylabel('Nhiệt độ')
    plt.title('Dự báo thời tiết')

    for i in range(5):
        plt.text(str(days[i]), min_t[i] - 1.5, min_t[i],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color='black')
    for i in range(5):
        plt.text(str(days[i]), max_t[i] + 0.5, max_t[i],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color='black')
    # plt.show()
    # plt.savefig('figure_line.png')
    st.pyplot()
    plt.clf()

def plot_T():
    # days = dates.thoi_gian2num(days)
    rcParams['figure.figsize'] = 6, 4
    plt.plot(data.thoi_gian[n-12:n], data.nhiet_do[n-12:n], color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='red',
             markersize=7)
    plt.plot(data.thoi_gian[n:n+6], data.nhiet_do[n:n+6], color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    # plt.ylim(min(min_t) - 4, max(max_t) + 4)
    # plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.thoi_gianFormatter('%h')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.legend(["Nhiệt độ đo được", "Nhiệt độ dự đoán"], loc=1)
    plt.xlabel('Thời')
    plt.ylabel('Nhiệt độ')
    plt.title('Biểu đồ nhiệt độ')

    st.pyplot()
    plt.clf()

if b:
    if place != "":
        try:
            weather_detail(place,)

        except NotFoundError:
            st.write("Vui lòng điền chính xác địa chỉ thành phố")







# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)