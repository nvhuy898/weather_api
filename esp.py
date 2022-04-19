from machine import Pin
from time import sleep
import machine
import dht 
import urequests
import ujson
import ntptime
import time
import network
#sensor = dht.DHT22(Pin(14))
#ntptime.host = "3.pool.ntp.org"
#ntptime.settime( múi giờ = 8 , máy chủ = 'ntp.ntsc.ac.cn' )
#settime((timezone=7,server ='3.asia.pool.ntp.org'))
#ntptime.settime()
sensor = dht.DHT11(Pin(14))
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Mai Tien', '12345678')
        while not wlan.isconnected():
          pass
do_connect()
t=time.localtime()
ntptime.settime()
while True:
  t=time.localtime()
  if t[5]==0:
      sensor.measure()
      temp = sensor.temperature()
      hum = sensor.humidity()
      temp_f = temp * (9/5) + 32.0
      print('Temperature: %3.1f C' %temp)
      print('Temperature: %3.1f F' %temp_f)
      print('Humidity: %3.1f %%' %hum)
      data = {
      "ID": 1581130.0,
      "ten": "iot",
      "quoc_gia": "VN",
      "kinh_do": 105.8412,
      "vi_do": 21.0245,
      "thoi_gian": t,
      "nhiet_do": temp,
      "do_am": hum,
      "ap_suat": 1006.0,
      "huong_gio": 136.0,
      "toc_do_gio": 5.67
      }
      post_data = ujson.dumps(data)
      response = urequests.post('http://192.168.1.2:9999/weather',data=post_data)
      print(type(response))
      print(response.text)
      sleep(1)


