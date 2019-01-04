#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Улучшеная версия calc_1
# Автор: Михаил Кучеренко, 04.01.2019
# Форматирование: autopep8

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication
from PyQt5.QtGui import QFont


class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
            Инициализация окна
        '''
        self.expression = ''  # Выражение, которое необходимо подсчитать

        self.title_label = QLabel('Калькулятор - 2', self)
        self.title_label.setGeometry(10, 20, 110, 20)

        big_font = QFont("Arial", 18, QFont.Bold)

        self.expression_label = QLabel(self.expression, self)
        self.expression_label.setFont(big_font)
        self.expression_label.setGeometry(10, 50, 130, 20)

        self.result_label = QLabel('= ?', self)
        self.result_label.setFont(big_font)
        self.result_label.setGeometry(130, 50, 100, 20)

        # Хранит в себе все сущности кнопок
        self.numpad = []

        # Вложенная функция для минимизации объемов кода
        def create_btn(code, num, handler, start_x=20, start_y=80,
                       btn_size=20, btn_margin=10, x_count=3):
            btn = QPushButton(code, self)
            btn_space = btn_size + btn_margin
            x = start_x + (num * btn_space % (btn_space * x_count))
            y = start_y + ((num // x_count) * btn_space)
            btn.setGeometry(x, y, btn_size, btn_size)
            btn.clicked.connect(handler)
            self.numpad.append(btn)

        # Кнопки операндов
        for idx, sym in enumerate(list(range(1, 10)) + ['(', '0', ')']):
            if type(sym) != str:
                sym = str(sym)
            create_btn(sym, idx, self.button_clicked)

        # Кнопки операций
        for idx, sym in enumerate(['+', '-', '*', '/', '|', '&', '^', '**']):
            create_btn(sym, idx, self.button_clicked, start_x=130, x_count=2)

        # Специальные кнопки
        for idx, sym in enumerate(['C', '=']):
            create_btn(sym, idx, self.special_clicked, start_x=130, start_y=20)

        self.statusBar()
        self.setGeometry(300, 300, 200, 230)
        self.setWindowTitle('Калькулятор')
        self.show()

    def calc(self, expr):
        '''
            Подсчитывает выражение и выводит на экран формы
        '''
        try:
            result = eval(expr)
            new_result = '= {}'.format(result)
        except:
            new_result = 'Ошибка'
        self.result_label.setText(new_result)

    def special_clicked(self):
        '''
            Обработчик события нажатия специальной кнопки
        '''
        sender = self.sender()
        if sender.text() == 'C':
            msg = 'Нажат сброс'
            self.expression = ''
            self.expression_label.setText(self.expression)
            self.result_label.setText('= ?')
        elif sender.text() == '=':
            msg = 'Подсчет результата ...'
            self.calc(self.expression)
        self.statusBar().showMessage(msg)

    def button_clicked(self):
        '''
            Обработчик события нажатия обычной кнопки
        '''
        sender = self.sender()
        msg = sender.text() + ' нажато'
        self.statusBar().showMessage(msg)
        self.expression += '{}'.format(sender.text())
        self.expression_label.setText(self.expression)


# Если запускаем скрипт не как бибилотеку, то выполнится блок кода ниже:
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем сущность нашего приложения PyQT
    main_form = MyMainWindow()    # Создаем экранную форму (окошко приложения)
    sys.exit(app.exec_())         # Исполняем
