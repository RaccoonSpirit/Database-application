import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtCore import Qt
from dbconect import dbworker
from PyQt6.QtGui import QAction
db = dbworker('Military_unit')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Меню')
        output_table = QMenu('Вывести таблицу', self)
        table_division = QAction('Таблица отделения', self)
        table_servicemans = QAction('Таблица военнослужащие', self)
        table_weapon = QAction('Таблица вооружение', self)
        output_table.addAction(table_division)
        output_table.addAction(table_servicemans)
        output_table.addAction(table_weapon)
        

        add_record = QAction('Добавить зпаись в бд', self)

        fileMenu.addAction(add_record)
        fileMenu.addMenu(output_table)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')
        self.show()
        

        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()