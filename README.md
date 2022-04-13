# weather_api
API thời tiết sử dụng flask
Các file chính:
- api.py: file api server
- sendata.py: gửi dữ liệu lên api
- weather.csv: file lưu trữ dữ liệu thời tiết
 
 **Hướng dẫn sử dụng:**
 
Chạy code:

``` python app.py ```

truy cập vào <http://127.0.0.1:9999/get_weather/hanoi> để xem thông tin nhiệt độ

có thể cập nhật dữ liệu bằng phương thức POST tại <http://127.0.0.1:9999/weather> , dữ liệu gửi lên phải có dạng json:

    {
    "ID": 1581130,
    "ten": "hanoi",
    "quoc_gia": "VN",
    "kinh_do": 105.8412,
    "vi_do": 21.0245,
    "thoi_gian": "Mon Apr 11 22:47:12 2022",
    "nhiet_do": 23,
    "do_am": 82,
    "ap_suat": 1008,
    "huong_gio": 150,
    "toc_do_gio": 3.75
    }

