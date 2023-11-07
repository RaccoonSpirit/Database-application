import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication, QTableView
from dbconect import dbworker
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
db = dbworker('Military_unit')
from PyQt6.QtCore import Qt



class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        
        return len(self._data)

    def columnCount(self, index):
        
        return len(self._data[0])
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Меню')
        output_table = QMenu('Вывести таблицу', self)
        table_servicemans = QAction('Таблица военнослужащие', self)
        table_weapon = QAction('Таблица вооружение', self)
        servicemans_weapon = QAction('Военнослужащие и их вооружение', self)
        table_servicemans.triggered.connect(self.showServiceman)
        table_weapon.triggered.connect(self.showWeapon)
        output_table.addAction(table_servicemans)
        output_table.addAction(table_weapon)
        output_table.addAction(servicemans_weapon)
        

        add_record = QAction('Добавить зпаись в бд', self)

        fileMenu.addAction(add_record)
        fileMenu.addMenu(output_table)

        

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Приложение для работы с бд')
        self.show()
        

        
        
    def showServiceman(self):
        '''Метод выводящий всех военнослужащих'''
        self.table = QTableView()
        self.model = TableModel(db.get_serviceman())
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
    
    def showWeapon(self):
        '''Метод выводящий всего воооружения'''
        self.table = QTableView()
        self.model = TableModel(db.get_weapon())
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()