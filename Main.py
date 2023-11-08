import sys
from PyQt6.QtWidgets import (QMainWindow, QMenu, QApplication, 
                             QTableView, QDialog, QLabel)
from dbconect import dbworker
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from TextDialog import TextDialogAdd, TextDialogSearch
from TableModel import TableModel
db = dbworker('Military_unit')


          
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        '''Создание меню'''
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Меню')
        
        '''Пункт вывести таблицу'''
        output_table = QMenu('Вывести таблицу', self)
        table_servicemans = QAction('Таблица военнослужащие', self)
        table_weapon = QAction('Таблица вооружение', self)
        servicemans_weapon = QAction('Военнослужащие и их вооружение', self)
        table_servicemans.triggered.connect(lambda:self.output_table(db.get_serviceman()))
        table_weapon.triggered.connect(lambda:self.output_table(db.get_weapon()))
        output_table.addAction(table_servicemans)
        output_table.addAction(table_weapon)
        output_table.addAction(servicemans_weapon)
        
        '''Пункт поиск по бд'''
        search_record = QAction('Поиск по бд', self)
        search_record.triggered.connect(self.data_search)
        
        '''Пункт добавить новую запись в бд'''
        add_record = QAction('Добавить запись в бд', self)
        add_record.triggered.connect(self.data_add)
        
        '''Отображение всех пунктов меню в окне'''
        fileMenu.addAction(search_record)
        fileMenu.addAction(add_record)
        fileMenu.addMenu(output_table)
        self.setGeometry(500, 300, 750, 550)
        self.setWindowTitle('Приложение для работы с бд')
    
    
    def data_search(self):
        '''Поиск'''
        dialog = TextDialogSearch(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = dialog.get_text()
            self.output_table(db.search_serviceman(text))
    
    def data_add(self):
        '''Добавление новой записи'''
        dialog = TextDialogAdd(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = dialog.get_text()
            print(text)
    
    def output_table(self, data:list):
        '''Метод выводящий таблицу'''
        if data != []:
            self.table = QTableView()
            self.model = TableModel(data)
            self.table.setModel(self.model)
            self.setCentralWidget(self.table)
        else:
            label = QLabel("Ничего не найдено")
            font = label.font()
            font.setPointSize(20)
            label.setFont(font)
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()