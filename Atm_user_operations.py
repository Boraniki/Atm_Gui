import sqlite3


class Account():
    def __init__(self, account_id, deposit_account, checking_account, debt):
        self.account_id = account_id
        self.deposit_account = deposit_account
        self.checking_account = checking_account
        self.debt = debt 


class Operation():
    def __init__(self):
        self.connection()
    
    def connection(self):
        self.connect = sqlite3.connect("atm_database.db")
        self.cursor = self.connect.cursor()
        request1 = "Create table if not exists Account (Account_id, Deposit_account INT, Checking_account INT, Debt INT)"
        request2 = "Create table if not exists Activities (Account_id INT, Amount INT, Date INT, Isdeposit INT,Other_account_id INT)"
        self.cursor.execute(request1)
        self.cursor.execute(request2)
        self.connect.commit()

    def money_transfer(self):
        pass

    def account_activities(self):
        pass

    def withdrawing(self, id, amount, isdeposit):
        request = "Select * from Account where Account_id = ?"
        self.cursor.execute(request,(id,))
        data = self.cursor.fetchall()
        
        for i in data :
            current_balance = i[1]
            if isdeposit == True:
                new_balance = current_balance - int(amount)
                if (new_balance) < 0:
                    pass
                else :
                    request = "Update Account set Deposit_account = ? where Account_id = ?"
                    self.cursor.execute(request,(new_balance,id))
                    self.connect.commit()
    
    def bank(self, no, amount, isdeposit):
        request = "Select * from Client where no = ?"
        self.cursor.execute(request,(no,))
        data = self.cursor.fetchall()
        for i in data:
            id = i[4]
            request = "Select * from Acount where Account_id = ?"
            self.cursor.execute(request,(id,))
            data1 = self.cursor.fetchall()

            if isdeposit == "1" :
                balance = data1[0]
                current_balance = balance - amount
               
                request = "Update Account set Deposit_account = ? where Account_id = ?"
                self.cursor.execute(request,(current_balance,id))
            if isdeposit == "0" :
                balance = data1[0]
                current_balance = balance - amount
                
                request = "Update Account set Checking_account = ? where Account_id = ?"
                self.cursor.execute(request,(current_balance,id))

    def debt_discharging(self):
        pass

    def currency(self):
        pass










