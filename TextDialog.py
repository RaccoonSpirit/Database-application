from PyQt6.QtWidgets import (QVBoxLayout,QLineEdit,QDialogButtonBox, 
                             QDialog, QLabel)


'''Окно поиска'''
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
    def get_text(self) -> str:
        return self.text_input.text()
'''Окно добавление новой записи'''
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
        self.label_name_weapon = QLabel("Название вооружения, введите через запятую")
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
        fio = self.text_input_fio.text()
        date = self.text_input_date.text() 
        branch_number = self.text_input_branch_number.text()
        rank = self.text_input_rank.text()
        name_weapon = self.text_input_name_weapon.text()
        list_weapon = name_weapon.split(",")
        list_weapon = [word.strip() for word in list_weapon]
        return [fio, date, branch_number, rank], list_weapon 
'''Окно удаленеия записи'''
class TextDialogDelete(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Удаление записи")
        self.label = QLabel("Введите ФИО военнослужащего и его дату рождения через пробел")
        self.text_input = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        self.setLayout(layout)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    def get_text(self) -> str:
        list_data = (self.text_input.text()).split(",")
        return list_data

        