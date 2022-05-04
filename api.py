
import json
import pandas as pd
from flask import Flask,  request
from utils import *
from unidecode import unidecode
from db import DB
from ai import AI

app = Flask(__name__)
ai=AI()
db=DB(name_db='weather.db')

config= get_config('config.yml')
ip_host=config['ip_host']



def save_data(data):
    if data['ten']=='iot':
        thoi_gian=data['thoi_gian']
        # t=np.array(thoi_gian.replace("[","").replace("]","").split(", ")).astype(int)
        t=thoi_gian
        from datetime import datetime
        d = datetime(t[0],t[1],t[2],t[3],t[4],t[5],)+ pd.Timedelta(hours=7)
        data['thoi_gian']=d.strftime("%a %b %d %H:%M:%S %Y")
    
    # df = pd.read_csv('weather.csv')
    # df = df.dropna()
    print('++++++++++++',list(data.values()))
    if db.column_list==list(data.keys()):
        
        # df = df.append(pd.DataFrame(pd.Series(data)).T, ignore_index=True)

        # df = df.dropna()
        # df.to_csv('weather.csv', index=None)
        return db.insert_data(list(data.values()))
    else:
        return False



@app.route('/get_weather/<city>', methods=['GET', 'POST'])
def get_weather(city):

    city=unidecode(city).lower().replace(" ","")

    # df = pd.read_csv('weather.csv')
    # df = df.dropna()
    # data = df.loc[df.ten == city]
    data=db.get_data(df_ten=city)
    X=data[-1:]
    X=X[['nhiet_do','do_am','toc_do_gio','huong_gio','ap_suat']].astype(float)
    X=X
    print(X,type(X))
    thoi_tiet_du_doan=ai.du_doan_thoi_tiet(X)
    print(thoi_tiet_du_doan)
    if len(data) == 0:
        return f"Không có dữ liệu thành phố {city}, Vui lòng kiểm tra lại !!!"
    else:
        if request.method == 'GET':
            data = data[-1:]
            kq = data.to_dict('records')[-1]

        elif request.method == 'POST':
            data = data[-12:]
            nhiet_do_du_doan=ai.du_doan_nhiet_do(data)
            kq = {
                "ID": data.ID.unique()[0],
                "ap_suat": list(data.ap_suat),
                "do_am": list(data.do_am),
                "huong_gio": list(data.huong_gio),
                "kinh_do": data.kinh_do.unique()[0],
                "nhiet_do": list(data.nhiet_do),
                "quoc_gia": data.quoc_gia.unique()[0],
                "ten": data.ten.unique()[0],
                "thoi_gian": list(data.thoi_gian),
                "toc_do_gio": list(data.toc_do_gio),
                "vi_do": data.vi_do.unique()[0],
                "nhiet_do_du_doan": list(nhiet_do_du_doan)
            }
        kq['thoi_tiet_du_doan']=thoi_tiet_du_doan
        return json.dumps(kq, default=np_encoder)


@app.route('/weather', methods=['GET', 'POST', 'DELETE'])
def weather():
    if request.method == 'GET':
        return "hãy gửi dữ liệu thời tiết"

    elif request.method == 'DELETE':
        # try:
            req_json = json.loads(request.data)
            print(req_json)
            ten=req_json['ten']
            thoi_gian=req_json['thoi_gian']

            kq=db.delete_data(ten,thoi_gian)
            
            if kq:
                print(
                    f"xoa thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}")

                return f"xoa thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}"
            else:
                return f"xoa du lieu khong thanh cong, kiem tra lai ten va thoi gian"

        # except :
        #     return f"xoa du lieu khong thanh cong"



            
    elif request.method == 'POST':
        try:
            req_json = json.loads(request.data)
            print(req_json)

            kq=save_data(req_json)
            
            if kq:
                print(
                    f"gui thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}")

                return f"gui thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}"
            else:
                return f"gui du lieu khong thanh cong, du lieu khong day du hoac sai"

        except :
            return f"gui du lieu khong thanh cong"


if __name__ == '__main__':
    # ipv4='192.168.51.102' #dia chi ipv4
    app.run(debug=True, host= ip_host, port=9999)
    # app.run(debug=True, port=9999)
    
