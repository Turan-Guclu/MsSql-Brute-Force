import sys
from PyQt5 import QtWidgets
from y import Ui_Form
import io
import pypyodbc
import time

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.final)

        
    def bilgi(self):
        self.count=self.ui.COUNT_LBL.text()
        x=int(self.count)
        return x


    def sifre(self):
        self.sifreee=[]
        self.sifree=[]
        try:
            dosya=io.open("pass.txt","r",encoding="UTF-8")
        except FileNotFoundError:
            print("Lütfen Uygulamaya 'pass.txt' dosyanızı Ekleyiniz Program 5 saniye içinde Kapanacaktır")
            time.sleep(5)
            exit()
        for i in dosya:
            self.sifree.append(i)
        for m in self.sifree[:self.bilgi()]:
            self.sifreee.append(m)
        return self.sifreee

    def final(self):
            ip=self.ui.IP_LBL.text()
            database=self.ui.USR_LBL.text()
            username=self.ui.USR_LBL.text()
            for x in self.sifre():
                password=x.strip("\n")
            
                baglanti = ('Driver={SQL Server};Server='+ip+';Datebase='+database+';UID='+username+';PWD='+password+";CONNECT TIMEONT=1")
                try:
                    db=pypyodbc.connect(baglanti)
                    if db.connected==True:
                        self.ui.textEdit.append("Bağlantı Başarılı")
                        break
                    else:
                        continue
                except pypyodbc.DatabaseError as err:
                    self.ui.textEdit.setText("Bağlantı Başarısız")
                    print("",err)

def App():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

App()