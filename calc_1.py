#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Составлено на основе статей отсюда: https://pythonworld.ru/gui
# Автор: Михаил Кучеренко, 04.01.2019
# Форматирование: autopep8

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QApplication


class MyMainWindow(QMainWindow):

    '''
        Это docstring - комментарий к классу/функции/методу/итд.

        Класс окна для приложения, наследуется от QMainWindow
        Т.е. родительский класс в данном случае - QMainWindow
        Больше про этот синтаксис:
        Объектно-ориентированное программирование: http://clc.am/ZBwKWg
        Инкапсуляция, наследование, полиморфизм: http://clc.am/IDeLxA
    '''

    def __init__(self):
        '''
            Конструктор класса MyMainWindow
        '''
        super().__init__()  # Вызов конструктора родителя
        self.initUI()       # Вызов инициализатора окна

    def initUI(self):
        '''
            Инициализация окна
        '''
        # Выражение, которое необходимо подсчитать
        self.expression = ''  # Изначально - пустое

        # Надпись просто для красоты
        self.lbl1 = QLabel('Калькулятор - 1', self)
        self.lbl1.setGeometry(10, 5, 100, 20)  # Назначет положение и размер

        # В эту надпись (label, lbl) запишем выражение
        self.lbl2 = QLabel(self.expression, self)
        self.lbl2.setGeometry(10, 20, 100, 20)

        # В эту надпись (label, lbl) запишем результат
        self.lbl3 = QLabel('= Результат', self)
        self.lbl3.setGeometry(200, 20, 100, 20)

        # Первая кнопка (button, btn) - с текстом '2'
        self.btn1 = QPushButton("2", self)
        self.btn1.move(30, 50)  # Просто назначает положение на форме

        # Вторая кнопка (button, btn) - с текстом '+'
        self.btn2 = QPushButton("+", self)
        self.btn2.move(150, 50)

        # Вторая кнопка (button, btn) - с текстом '='
        self.btn3 = QPushButton("=", self)
        self.btn3.move(150, 100)

        # Назначаем обработчики для события "Нажатие" (Click)
        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2.clicked.connect(self.buttonClicked)
        self.btn3.clicked.connect(self.buttonClicked)

        self.statusBar()                      # Включить отображение панели
        self.setGeometry(300, 300, 290, 150)  # Размеры окна
        self.setWindowTitle('Калькулятор')    # Заголовок окна

        self.show()                           # Запуск окна

    def calc(self, expr):
        '''
            Подсчитывает выражение и выводит на экран формы
        '''
        # Пробуем выполнить блок кода ниже (в нем могут возникнуть ошибки)
        try:
            # Встроенная функция питона для исполнения кода,
            #   на С/С++ пришлось бы написать сотни строк,
            #   чтобы реализовать честный алгоритм обработки
            #   и парсинга строки с математическим выражением
            # Например, можно было бы воспользоваться алгоритмом,
            #   называемым "Парсинг обратной польской нотации".
            #   Но он довольно сложен для новичка в программировании.
            # Говорим, что expr это python-код и интерпретатор его выполняет,
            #   но так как у нас вводят только математические символы,
            #   то мы получим результат математической операции
            # Однако, это ОЧЕНЬ небезопасная функция,
            #   eё нельзя использовать в продакшн-коде (реальных системах)!
            result = eval(expr)                 # Но для учебных целей - можно
            new_result = '= {}'.format(result)  # Формируем вывод в виде строки
        # Если же в процессе исполнения кода выше произошла ошибка,
        #   еще говорят "выпало исключение", что равносильно
        except:
            new_result = 'Ошибка'  # То его ловим и пишем что произошла ошибка
        # Конец блока try-except
        # Больше про этот синтаксис тут: http://clc.am/RF12Eg
        self.lbl3.setText(new_result)  # Собственно, устанавливаем новый текст

    def buttonClicked(self):
        '''
            Обработчик события нажатия кнопки
        '''
        sender = self.sender()             # Определяем объект, который нажали
        msg = sender.text() + ' нажато'    # Создаем сообщение с текстом кнопки
        self.statusBar().showMessage(msg)  # Вывести сообщение на статус-бар

        if sender.text() == '=':           # Если текст кнопки - равно
            self.calc(self.expression)     # То подсчитываем выражение
        else:
            # Иначе - изменяем выражение
            self.expression += '{}'.format(sender.text())
            # Переустанавливаем текст надписи для выражения
            self.lbl2.setText(self.expression)


# Если запускаем скрипт не как бибилотеку, то выполнится блок кода ниже:
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем сущность нашего приложения PyQT
    main_form = MyMainWindow()    # Создаем экранную форму (окошко приложения)
    sys.exit(app.exec_())         # Исполняем
