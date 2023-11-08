import sys
from PyQt6.QtWidgets import (QMainWindow, QMenu, QApplication, 
                             QTableView, QVBoxLayout,QLineEdit,QDialogButtonBox, 
                             QDialog, QLabel)
from dbconect import dbworker
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

db = dbworker('Military_unit')

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

class TextDialogSearch(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Поиск")
        self.label = QLabel("Введите ФИО военнослужащего или название вооружения")
        self.text_input = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        self.setLayout(layout)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    def get_text(self):
        return self.text_input.text()
class TextDialogAdd(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление данных")
        self.label_fio = QLabel("Введите ФИО военнослужащего ")
        self.text_input_fio = QLineEdit()
        self.label_date = QLabel("Дату рождения")
        self.text_input_date = QLineEdit()
        self.label_branch_number = QLabel("Номер отделения")
        self.text_input_branch_number = QLineEdit()
        self.label_rank = QLabel("Звание")
        self.text_input_rank = QLineEdit()
        self.label_name_weapon = QLabel("Название вооружения")
        self.text_input_name_weapon = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.label_fio)
        layout.addWidget(self.text_input_fio)
        layout.addWidget(self.label_date)
        layout.addWidget(self.text_input_date)
        layout.addWidget(self.label_branch_number)
        layout.addWidget(self.text_input_branch_number)
        layout.addWidget(self.label_rank)
        layout.addWidget(self.text_input_rank)
        layout.addWidget(self.label_name_weapon)
        layout.addWidget(self.text_input_name_weapon)
        self.setLayout(layout)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_text(self):
        return [self.text_input_fio.text(),self.text_input_date.text(),self.text_input_branch_number.text(),self.text_input_rank.text(),self.text_input_name_weapon.text()]
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Меню')
        output_table = QMenu('Вывести таблицу', self)
        table_servicemans = QAction('Таблица военнослужащие', self)
        table_weapon = QAction('Таблица вооружение', self)
        servicemans_weapon = QAction('Военнослужащие и их вооружение', self)
        table_servicemans.triggered.connect(lambda:self.output_table(db.get_serviceman()))
        table_weapon.triggered.connect(lambda:self.output_table(db.get_weapon()))
        output_table.addAction(table_servicemans)
        output_table.addAction(table_weapon)
        output_table.addAction(servicemans_weapon)
        
        search_record = QAction('Поиск по бд', self)
        search_record.triggered.connect(self.data_search)
        add_record = QAction('Добавить запись в бд', self)
        add_record.triggered.connect(self.data_add)
        
        fileMenu.addAction(search_record)
        fileMenu.addAction(add_record)
        fileMenu.addMenu(output_table)
        self.setGeometry(500, 300, 750, 550)
        self.setWindowTitle('Приложение для работы с бд')
    
    def data_search(self):
        dialog = TextDialogSearch(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = dialog.get_text()
            self.output_table(db.search_serviceman(text))
    def data_add(self):
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