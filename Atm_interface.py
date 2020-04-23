from PyQt5 import QtWidgets, QtChart, QtGui, QtCore
import sys
from Atm_user import *


user = Proccess_of_user()
operation = Operation()


class Login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.dialog()

    def dialog(self):        
        self.setWindowTitle("Login")
        self.resize(500,120)

        layout = QtWidgets.QGridLayout()

        label_name = QtWidgets.QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QtWidgets.QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your user name")
        layout.addWidget(label_name,0,0)
        layout.addWidget(self.lineEdit_username,0,1)

        label_password = QtWidgets.QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setPlaceholderText("Please enter your user password")
        layout.addWidget(label_password,1,0)
        layout.addWidget(self.lineEdit_password,1,1)

        login_buton = QtWidgets.QPushButton("Login")
        layout.addWidget(login_buton,2,1)

        login_buton.clicked.connect(self.client_entering)

        self.setLayout(layout)
    
    def client_entering(self,no):
        entered_password = self.lineEdit_password.text()
        entered_no = self.lineEdit_username.text()
        true_password = user.client_enter(entered_no)
        if(int(entered_password) == true_password):            
            self.client = user.client_info(entered_no)
            self.accept()
                        
        else :
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')
            self.lineEdit_password.clear()
            self.lineEdit_username.clear()
        

class Window(QtWidgets.QWidget):
    def __init__(self,client,account):
        super().__init__()
        self.client = client
        self.flag = False
        self.window()
        
    def window(self):
        self.setWindowTitle("Window")
        self.resize(600,600)
        vbox = QtWidgets.QVBoxLayout()
        tabWidget = QtWidgets.QTabWidget()

        tabWidget.addTab(Tab_ballance(client,account), "Varlıklar")

        tabWidget.addTab(Tab_debt(client,account), "Borçlar")
        tabWidget.addTab(Tab_account_operation(),"İşlemler")

        vbox.addWidget(tabWidget)
        self.setLayout(vbox)


class Tab_ballance(QtWidgets.QWidget):
    def __init__(self,client,account):

        super().__init__()
        self.account = account
        self.client = client
        self.ballance_ui()

    def ballance_ui(self):
        
        g_box = QtWidgets.QGridLayout()

        self.total_balance = QtWidgets.QLabel("Toplam")
        self.checking_account = QtWidgets.QLabel("Vadesiz Hesap")
        self.deposit_account = QtWidgets.QLabel("Vadeli eHesap")

        self.total_balance_amount = QtWidgets.QLabel("{}".format(self.account.deposit_account+self.account.checking_account))
        self.checking_account_amount = QtWidgets.QLabel("{}".format(self.account.checking_account))
        self.deposit_account_amount = QtWidgets.QLabel("{}".format(self.account.deposit_account))

        series = QtChart.QPieSeries()
        series.setHoleSize(0.35)
        series.append("Vadeli",self.account.deposit_account)
        series.append("Vadesiz",self.account.checking_account)

        chart = QtChart.QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignLeft)
 
        chartview = QtChart.QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)

        self.withdrawing_buton = QtWidgets.QPushButton("Para Çekme")
        self.bank_buton = QtWidgets.QPushButton("Para Yatırma")

        g_box.addWidget(self.total_balance,0,0)
        g_box.addWidget(self.checking_account,1,0)
        g_box.addWidget(self.deposit_account,2,0)
        g_box.addWidget(self.total_balance_amount,0,1)
        g_box.addWidget(self.checking_account_amount,1,1)
        g_box.addWidget(self.deposit_account_amount,2,1)
        g_box.addWidget(self.bank_buton,0,2)
        g_box.addWidget(self.withdrawing_buton,1,2)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(chartview)
        v_box.addLayout(g_box)

        self.withdrawing_buton.clicked.connect(self.withdrawing)
        self.bank_buton.clicked.connect(self.bank)

        self.setLayout(v_box)
        

    def bank(self):
        pass
    
    def withdrawing(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setModal(True)
        self.dialog.resize(500,150)

        vbox = QtWidgets.QVBoxLayout()
        tabWidget = QtWidgets.QTabWidget()

        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()

        tabWidget.addTab(tab1,"Vadeli Hesap")
        tabWidget.addTab(tab2,"Vadesiz Hesap")

        vbox.addWidget(tabWidget)

        tab1_layout = QtWidgets.QGridLayout()

        self.buton1 = QtWidgets.QPushButton("Ok")
        label_name1 = QtWidgets.QLabel('<font size="4"> Vadeli hesabınızdan çekmek istediğiniz tutarı girin </font>')
        self.lineEdit_1 = QtWidgets.QLineEdit()        

        tab1_layout.addWidget(label_name1,0,0)
        tab1_layout.addWidget(self.lineEdit_1,1,0)
        tab1_layout.addWidget(self.buton1,1,1)
        
        tab1.setLayout(tab1_layout)

        tab2_layout = QtWidgets.QGridLayout()

        buton2 = QtWidgets.QPushButton("Ok")
        label_name2 = QtWidgets.QLabel('<font size="4"> Vadesiz hesabınızdan çekmek istediğiniz tutarı girin </font>')
        self.lineEdit_2 = QtWidgets.QLineEdit()

        tab2_layout.addWidget(label_name2,0,0)
        tab2_layout.addWidget(self.lineEdit_2,1,0)
        tab2_layout.addWidget(buton2,1,1)

        tab2.setLayout(tab2_layout)
                
        self.buton1.clicked.connect(lambda : self.withdraw_module(True))
        buton2.clicked.connect(lambda : self.withdraw_module(False))

        self.dialog.setLayout(vbox)
        

        self.dialog.exec()
    
    def withdraw_module(self,bool):
        if bool == True:
            self.amount1 = self.lineEdit_1.text()
            operation.withdrawing(self.account.account_id,self.amount1,True)

            self.dialog.accept()
            
            
        if bool == False:
            operation.withdrawing(self.account.account_id,self.amount2,False)


class Tab_debt(QtWidgets.QWidget):
    def __init__(self,client,account):
        super().__init__()
        self.account = account
        self.client = client
        self.debt_ui()
            

    def debt_ui(self):
        g_box = QtWidgets.QGridLayout()
        
        self.total_limit = QtWidgets.QLabel("Toplam limit")
        self.credit_avialable = QtWidgets.QLabel("Kullanılabilir limit")
        self.debt = QtWidgets.QLabel("Son ekstreden kalan borç")

        self.total_limit_amount = QtWidgets.QLabel("500")
        self.credit_avialable_amount = QtWidgets.QLabel(str(500 - self.account.debt) )
        self.debt_amount = QtWidgets.QLabel("{}".format(self.account.debt))

        series = QtChart.QPieSeries()
        series.append("Kullanılabilir limit",(500 - self.account.debt))
        series.append("Kalan borç",self.account.debt)

        chart = QtChart.QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignLeft)
 
        chartview = QtChart.QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)

        g_box.addWidget(self.total_limit,0,0)
        g_box.addWidget(self.credit_avialable,1,0)
        g_box.addWidget(self.debt,2,0)
        g_box.addWidget(self.total_limit_amount,0,1)
        g_box.addWidget(self.credit_avialable_amount,1,1)
        g_box.addWidget(self.debt_amount,2,1)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(chartview)
        v_box.addLayout(g_box)

        self.setLayout(v_box)


class Tab_account_operation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.operation_ui()    

    def operation_ui(self):
        pass
        


class Tab_account_statement(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.currency_ui()    

    def currency_ui(self):
        pass


class Tab_currency(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.currency_ui()    

    def currency_ui(self):
        pass


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        
        client = login.client
        account = user.account_info(client.client_id)
        window1 = Window(client,account)
        window1.show()        
        sys.exit(app.exec_())


























