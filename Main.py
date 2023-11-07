import sys
from PyQt6.QtWidgets import (QMainWindow, QMenu, QApplication, 
                             QTableView, QVBoxLayout,QLineEdit,QDialogButtonBox, 
                             QDialog)
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

class TextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Диалоговое окно")

        self.text_input = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        self.setLayout(layout)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_text(self):
        return self.text_input.text()
        
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
        
        add_record = QAction('Добавить зпаись в бд', self)
        add_record.triggered.connect(self.data_entry)
        
        fileMenu.addAction(add_record)
        fileMenu.addMenu(output_table)
        self.setGeometry(500, 300, 750, 550)
        self.setWindowTitle('Приложение для работы с бд')
    
    def data_entry(self):
        dialog = TextDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            text = dialog.get_text()
            self.output_table(db.search_serviceman(text))
            
    def output_table(self, data:list):
        '''Метод выводящий таблицу'''
        self.table = QTableView()
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()