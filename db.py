import sqlite3
from sqlite3 import Error
import pandas as pd
def sql_connection():
    try:
        con = sqlite3.connect('weather.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE WEATHER(ID,ten,quoc_gia,kinh_do,vi_do,thoi_gian,nhiet_do,do_am,ap_suat,huong_gio,toc_do_gio)")
    con.commit()

con = sql_connection()
cursorObj = con.cursor()
# sql_table(con)


def insert_data(con, data):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO  WEATHER(ID,ten,quoc_gia,kinh_do,vi_do,thoi_gian,nhiet_do,do_am,ap_suat,huong_gio,toc_do_gio)"
              "VALUES (?,?,?,?,?,?,?,?,?,?,?)", data)
    con.commit()

def delete_data(con, ten, thoi_gian):
    cursorObj = con.cursor()
    delete_query = "DELETE FROM WEATHER WHERE ten = '"+ df_ten + "' AND thoi_gian='"+ df_thoi_gian +"'"
    cursorObj.execute(delete_query)
    con.commit()
# df= pd.read_csv('weather.csv')   
# for row in df.values:
#     insert_data(con, tuple(row))
