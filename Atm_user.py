import sqlite3
from Atm_user_operations import *

class Client():
    def __init__(self,name,surname,no,password,client_id):
        self.name = name
        self.surname = surname
        self.no = no
        self.password = password
        self.client_id = client_id



class Proccess_of_user():
    def __init__(self):
        self.connection()

    def connection(self):
        self.connect = sqlite3.connect("atm_database.db")
        self.cursor = self.connect.cursor()
        request = "Create table if not exists Client (Name TEXT, Surname TEXT, No INT, Password INT,ID INTEGER PRIMARY KEY AUTOINCREMENT)"
        self.cursor.execute(request)
        self.connect.commit()

    def client_info(self,no):
        request = "Select * from Client where No = ?"
        self.cursor.execute(request,(no,))
        data = self.cursor.fetchall()
        client = Client(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4])
        
        return client

    def account_info(self,id):
        request = "Select * from Account where Account_id = ?"
        self.cursor.execute(request,(id,))
        data = self.cursor.fetchall()
        account = Account(data[0][0],data[0][1],data[0][2],data[0][3])

        return account

    def client_enter(self,no):
        request = "Select * From client Where No = ?"
        self.cursor.execute(request,(no,))
        person = self.cursor.fetchall()
        for i in person:
            return i[3]










