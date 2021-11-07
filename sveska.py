from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from gai2 import Ui_MainWindow
import sys
import main_01

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        def clicked(self) : 
            self.ui.pushButton.clicked.connect(self.loadProducts) 
        clicked(self)
    def loadProducts(self):
        main_01.main() 
        all = main_01.returns_data() 
        named = [] 
        urls = []
        
        for key , value in all.items():
            named.append(key) 
            urls.append(value)
        
        products = [
            {'name':f'{named[0]}', 'url':f'{urls[0]}'},
            {'name':f'{named[1]}', 'url':f'{urls[1]}'},
            {'name':f'{named[2]}', 'url':f'{urls[2]}'},
            {'name':f'{named[3]}', 'url':f'{urls[3]}'},
            {'name':f'{named[4]}', 'url':f'{urls[4]}'},
            {'name':f'{named[5]}', 'url':f'{urls[5]}'},
            {'name':f'{named[6]}', 'url':f'{urls[6]}'},
            {'name':f'{named[7]}', 'url':f'{urls[7]}'}, 
            {'name':f'{named[8]}', 'url':f'{urls[8]}'},
         ]
        self.ui.tableWidget.setRowCount(len(products))
        self.ui.tableWidget.setColumnCount(2)

        self.ui.tableWidget.setHorizontalHeaderLabels(('Навзание','Ссылка'))

        self.ui.tableWidget.setColumnWidth(0,120)
        self.ui.tableWidget.setColumnWidth(1,50)


        row_index = 0
        for product in products:
            self.ui.tableWidget.setItem(row_index,0,QTableWidgetItem(str(product['name'])))
            self.ui.tableWidget.setItem(row_index,1,QTableWidgetItem(str(product['url'])))
            row_index += 1
    
    
        

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

create_app()







#from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication 


#Form, Window = uic.loadUiType(".ui")

#

#app = QApplication([])
#window = Window()
#form = Form()
#form.setupUi(window)
#window.show()
#app.exec_()