
import json
import pandas as pd
from flask import Flask, jsonify,  request
from utils import *
from unidecode import unidecode
                   
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/get_weather/<city>', methods=['GET', 'POST'])
def get_weather(city):

    city=unidecode(city).lower().replace(" ","")

    df = pd.read_csv('weather.csv')
    df = df.dropna()
    data = df.loc[df.ten == city]
    if len(data) == 0:
        return f"Không có dữ liệu thành phố {city}, Vui lòng kiểm tra lại !!!"
    else:
        if request.method == 'GET':
            data = data[-1:]
            kq = data.to_dict('records')[-1]
        elif request.method == 'POST':
            data = data[-9:]
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
                "vi_do": data.vi_do.unique()[0]
            }

        return json.dumps(kq, default=np_encoder)


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return jsonify({" reponse": "nhap ten thanh pho"})
    elif request.method == 'POST':
        try:
            req_json = json.loads(request.data)

            save_data(req_json)
            print(
                f"gui thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}")

            return f"gui thanh cong du lieu tai {req_json['ten']}, {req_json['thoi_gian']}"
        except :
            return f"gui du lieu khong thanh cong"


if __name__ == '__main__':
    app.run(debug=True, port=9999)
