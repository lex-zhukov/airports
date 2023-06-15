from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from db import products

products_filtered = []
tec_val = 0

class Ui_Window(QMainWindow):
       
    def __init__(self):
        super(Ui_Window, self).__init__()
    
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(1117, 831)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(50, 140, 221, 28))
        self.clear_btn.setObjectName("clear_btn")
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setGeometry(QtCore.QRect(300, 140, 431, 28))
        self.filter_btn.setObjectName("filter_btn")
        self.lat_min = QtWidgets.QLabel(self.centralwidget)
        self.lat_min.setGeometry(QtCore.QRect(50, 30, 91, 16))
        self.lat_min.setObjectName("lat_min")
        self.lat_max = QtWidgets.QLabel(self.centralwidget)
        self.lat_max.setGeometry(QtCore.QRect(50, 90, 81, 16))
        self.lat_max.setObjectName("lat_max")
        self.long_min = QtWidgets.QLabel(self.centralwidget)
        self.long_min.setGeometry(QtCore.QRect(520, 30, 101, 16))
        self.long_min.setObjectName("long_min")
        self.long_max = QtWidgets.QLabel(self.centralwidget)
        self.long_max.setGeometry(QtCore.QRect(520, 90, 141, 16))
        self.long_max.setObjectName("long_max")
        self.lat_min_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_min_inp.setGeometry(QtCore.QRect(140, 30, 361, 22))
        self.lat_min_inp.setObjectName("lat_min_inp")
        self.lat_max_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.lat_max_inp.setGeometry(QtCore.QRect(140, 90, 361, 22))
        self.lat_max_inp.setObjectName("lat_max_inp")
        self.long_min_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.long_min_inp.setGeometry(QtCore.QRect(610, 30, 361, 22))
        self.long_min_inp.setObjectName("long_min_inp")
        self.long_max_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.long_max_inp.setGeometry(QtCore.QRect(610, 90, 361, 22))
        self.long_max_inp.setObjectName("long_max_inp")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(750, 140, 221, 28))
        self.find_btn.setObjectName("find_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 1051, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "CRAZY AIRLINES"))
        self.clear_btn.setText(_translate("Window", "Clear"))
        self.filter_btn.setText(_translate("Window", "FIlter"))
        self.lat_min.setText(_translate("Window", "latitude min"))
        self.lat_max.setText(_translate("Window", "latitude max"))
        self.long_min.setText(_translate("Window", "longitude min"))
        self.long_max.setText(_translate("Window", "longitude max"))
        self.find_btn.setText(_translate("Window", "Find"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Window", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Window", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Window", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window", "airport"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window", "city"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Window", "country"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Window", "iata"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Window", "icao"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Window", "latitude"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Window", "longitude"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Window", "elevation"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Window", "utc"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Window", "region"))

        self.clear_btn.clicked.connect(self.clear)
        self.find_btn.clicked.connect(self.loadProducts)
        self.filter_btn.clicked.connect(self.fltr)
    
    def fltr(self):
        global tec_val
        if tec_val % 2 == 0:
            products_filtered.sort(key=lambda x: x.get('latitude'))
            tec_val += 1
        else:
            products_filtered.sort(key=lambda x: x.get('longitude'))
            tec_val += 1
        self.tableWidget.clear()
        self.load()            
            
    def clear(self):
        self.lat_min_inp.clear()
        self.lat_max_inp.clear()
        self.long_min_inp.clear()
        self.long_max_inp.clear()
        self.tableWidget.clear()
        
    def find(self, rw):
        a = int(self.lat_min_inp.text())
        b = int(self.lat_max_inp.text())
        c = int(self.long_min_inp.text())
        d = int(self.long_max_inp.text())
        if ((float((products[rw])['latitude']) > a) and 
            (float((products[rw])['latitude']) < b) and 
            (float((products[rw])['longitude']) > c) and 
            (float((products[rw])['longitude']) < d)
            ):
            products_filtered.append(products[rw])

    def cret(self):
        for i in range(len(products)):
            self.find(i)
            i += 1
    
    def loadProducts(self):
        global products_filtered
        products_filtered = []
        self.cret()
        self.tableWidget.setRowCount(len(products_filtered))
        self.load()
        
    def load(self):   
        row_index = 0
        for product in products_filtered:
            self.tableWidget.setItem(row_index,0,QTableWidgetItem(str(product['id'])))
            self.tableWidget.setItem(row_index,1,QTableWidgetItem(str(product['airport'])))
            self.tableWidget.setItem(row_index,2,QTableWidgetItem(str(product['city'])))
            self.tableWidget.setItem(row_index,3,QTableWidgetItem(str(product['country'])))
            self.tableWidget.setItem(row_index,4,QTableWidgetItem(str(product['iata'])))
            self.tableWidget.setItem(row_index,5,QTableWidgetItem(str(product['icao'])))
            self.tableWidget.setItem(row_index,6,QTableWidgetItem(str(product['latitude'])))
            self.tableWidget.setItem(row_index,7,QTableWidgetItem(str(product['longitude'])))
            self.tableWidget.setItem(row_index,8,QTableWidgetItem(str(product['elevation'])))
            self.tableWidget.setItem(row_index,9,QTableWidgetItem(str(product['utc'])))
            self.tableWidget.setItem(row_index,10,QTableWidgetItem(str(product['region'])))
            row_index += 1