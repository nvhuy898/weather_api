# weather_api
API thời tiết sử dụng flask

Demo sảm phẩm tại [Demo](https://drive.google.com/drive/folders/1NqAaXT-LtqM84XugpzbYBwhu4DUxHKLy?usp=sharing)

Các file chính:
- api.py: file server api
- app.py : file giao diện web
- esp.py : file đọc dữ liệu từ esp và gửi dữ liệu lên server
- sendata.py: demo gửi dữ liệu lên server
- weather.csv: file lưu trữ dữ liệu thời tiết
 
 **Hướng dẫn sử dụng:**

 
Cài thư viện:

```pip install -r requirements.txt```

tải file weight tại [weight](https://drive.google.com/file/d/17kofUi2lz1OGPxDT53KKCFV37CpWUDwP/view?usp=sharing) lưu vào thư mục weights

Chạy code:

``` python api.py ```

``` streamlit run app.py ```

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



