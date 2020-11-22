"""
Случайный комметарий
"""
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time

N = 2

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Кодировение/Декодирование текста")
        self.setFixedSize(1000, 650)
        self.move(200, 200)
        self.setStyleSheet('QMainWindow {background-color: #63AB48 ;}')

        # Текст "Текст до кодирования"
        self.title_text = QLabel(self)
        self.title_text.setText("Текст до кодирования")
        self.title_text.resize(450, 40)
        self.title_text.move(100, 20)
        self.title_text.setFont(QFont('Arial', 14))

        # Текст "Путь до файла с текстом"
        self.path_text = QLabel(self)
        self.path_text.setText("Путь до файла с текстом:")
        self.path_text.resize(450, 40)
        self.path_text.move(100, 375)
        self.path_text.setFont(QFont('Arial', 10))

        # Заголовок области декодирования
        self.title_text2 = QLabel(self)
        self.title_text2.setText("{Закодированный текст")
        self.title_text2.resize(450, 40)
        self.title_text2.move(550, 20)
        self.title_text2.setFont(QFont('Arial', 14))

        # Область ввода текста для кодирования
        self.clear_text = QPlainTextEdit(self)
        self.clear_text.move(100, 70)
        self.clear_text.resize(350, 300)

        # Ввод пути файла для открытия для кодирования
        self.path_to_file = QPlainTextEdit(self)
        self.path_to_file.move(100, 410)
        self.path_to_file.resize(300, 30)

        # Область вывода закодированного текста
        self.code_text = QPlainTextEdit(self)
        self.code_text.setReadOnly(True)
        self.code_text.move(550, 70)
        self.code_text.resize(350, 350)

        # Кнопки кодировать/декодировать
        self.code_btn = QPushButton("Закодировать", self)
        self.code_btn.move(100, 470)
        self.code_btn.resize(350, 75)
        self.code_btn.clicked.connect(self.code_clear_text)
        self.decode_btn = QPushButton("Декодировать", self)
        self.decode_btn.move(550, 470)
        self.decode_btn.resize(350, 75)
        self.decode_btn.clicked.connect(self.dectypt)

        # Кнопка Открыть текст для кодирования из файла
        self.fromfile = QPushButton("Открыть текст для кодирования \n из файла", self)
        self.fromfile.clicked.connect(self.open_from_file)
        self.fromfile.move(100, 550)
        self.fromfile.resize(350, 50)

        # Кнопка Очистить поле текста для кодирования
        self.clrarea_btn = QPushButton("Очистить поле текста для кодирования", self)
        self.clrarea_btn.clicked.connect(self.clear_area)
        self.clrarea_btn.move(550, 550)
        self.clrarea_btn.resize(350, 50)

        self.show()

    def code_clear_text(self):  # Функция кодирования текста из поля clear_text. Срабатывает по нажатию на code_btn.
        before_code_text = self.clear_text.toPlainText()
        encrypt_text = self.encrypt(before_code_text)  # Само кодирование происходит в другой функции для удобства.
        self.code_text.setPlainText(encrypt_text)

    def open_from_file(self):  # Функция открытия файла и чтения из него для кодирования
                               # Если проверки на верность введённого пути файла от пользователя.
        filepath = self.path_to_file.toPlainText()
        if filepath == '' or filepath == 'ЗАПОЛНИ ЭТО ПОЛЕ!':
            self.path_to_file.setPlainText("ЗАПОЛНИ ЭТО ПОЛЕ!")
        elif not os.path.isfile(filepath):
            self.path_to_file.setPlainText("ТАКОГО ПУТИ НЕ СУЩЕСТВУЕТ!")
        else:
            text_from_file = open(filepath).read()
            self.clear_text.setPlainText(text_from_file)

    def clear_area(self):  # Простое очищение поля clear_text. Работает по нажатию кнопки clrarea_btn
        self.clear_text.clear()

    def dectypt(self):  # Функция дешифрования. Берётся символьное значение числа согласно кодировке ascii.
                        # Работает по нажатию кнопки decode_btn
        decryptext = ''
        encrypt_text = self.code_text.toPlainText().split()
        for i in encrypt_text:
            decryptext += chr(int(i) - N)
        self.clear_text.setPlainText(decryptext)

    @staticmethod
    def encrypt(text):  # Функция так назваемого шифрования. Берётся числовое значения символа согласно кодировке ascii
                        # Работает по нажатию кнопки code_btn
        res = []
        for i in text:
            res.append(ord(i) + N)
        return str(res)[1:-1].replace(',', ' ')
    
    @staticmethod
    def time_trace(start = 0, end = 0):
        pass

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
