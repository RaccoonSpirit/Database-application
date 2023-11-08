from PyQt6.QtWidgets import (QVBoxLayout,QLineEdit,QDialogButtonBox, 
                             QDialog, QLabel)

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
class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Авторизация")
        self.adress = QLabel("Введите адрес базы данных")
        self.input_adress = QLineEdit()
        self.login = QLabel("Введите логин")
        self.input_login = QLineEdit()
        self.password = QLabel("Введите пароль")
        self.input_password = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.adress)
        layout.addWidget(self.input_adress)
        layout.addWidget(self.login)
        layout.addWidget(self.input_login)
        layout.addWidget(self.password)
        layout.addWidget(self.input_password)
        self.setLayout(layout)
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    def get_text(self):
        return [self.input_adress.text(),self.input_login.text(),self.input_password.text()]