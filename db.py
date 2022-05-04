import sqlite3
from sqlite3 import Error
import pandas as pd
from sqlalchemy import column
class DB():
    def __init__(self,name_db='weather.db'):
        self.con = self.sql_connection(name=name_db)
        self.cursorObj = self.con.cursor()
        table='WEATHER'
        self.column_list = list(pd.read_sql_query(f"SELECT * FROM {table} limit 1", self.con).columns)

    def sql_connection(self, name='weather.db'):
        try:
            con = sqlite3.connect(name,check_same_thread=False)
            return con
        except Error:
            print(Error)

    def sql_table(self):
        self.cursorObj.execute("CREATE TABLE WEATHER(ID,ten,quoc_gia,kinh_do,vi_do,thoi_gian,nhiet_do,do_am,ap_suat,huong_gio,toc_do_gio)")
        self.con.commit()



    def insert_data(self, data):
        cursorObj = self.con.cursor()
        cursorObj.execute("INSERT INTO  WEATHER(ID,ten,quoc_gia,kinh_do,vi_do,thoi_gian,nhiet_do,do_am,ap_suat,huong_gio,toc_do_gio)"
                "VALUES (?,?,?,?,?,?,?,?,?,?,?)", data)
        self.con.commit()
        return True

    def delete_data(self, df_ten, df_thoi_gian):
        cursorObj = self.con.cursor()
        delete_query = "DELETE FROM WEATHER WHERE ten = '"+ df_ten + "' AND thoi_gian='"+ df_thoi_gian +"'"
        cursorObj.execute(delete_query)
        self.con.commit()
        return True

    def update_data(self, df_ten, df_thoi_gian):
        cursorObj = self.con.cursor()
        delete_query = "UPDATE FROM WEATHER WHERE ten = '"+ df_ten + "' AND thoi_gian='"+ df_thoi_gian +"'"
        cursorObj.execute(delete_query)
        self.con.commit()

    def get_data(self,df_ten):
        self.cursorObj.execute("SELECT * FROM WEATHER WHERE ten = '"+ df_ten + "'")
        rows = self.cursorObj.fetchall()
        return pd.DataFrame(rows, columns=self.column_list)


if __name__ == '__main__':
    db=DB()
    df_query=db.get_data( df_ten='hue')
    print(df_query)



