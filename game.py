from PyQt5 import QtWidgets #НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!! РАБОТАЙ ПОЖАЛУЙСТА В СВОЕЙ ПАПКЕ
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import *
import sys
flag = True

def application():
    global button
    global flag
    app = QApplication(sys.argv)
    window = QMainWindow()
    text = QtWidgets.QLabel(window)
    text1 = QtWidgets.QLabel(window)
    text2 = QtWidgets.QLabel(window)  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!

    window.setWindowTitle("Моя програма")
    window.setGeometry(30, 25, 350, 200)  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!
    text.setText("Player")  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!
    text.move(300, 150)
    text1.setText("Монстр")  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!
    text1.move(-50, -50)
    text2.setText("Сундук")  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!
    text2.move(-300, -50)

    def up():
        global flag
        button.move(265, 70)
        if flag == True:
            text.move(300, 110)
        flag = False
    def left():
        global flag
        button1.move(100, 150)
        text.move(220, 150)
        if flag == True:
            text.move(300, 110)
        flag = False
    def right():
        global flag
        button2.move(430, 150)
        text.move(380, 150)
        if flag == True:
            text.move(300, 110)
        flag = False
    def down():
        global flag
        button3.move(265, 235)
        text.move(300, 190)
        if flag == True:
            text.move(300, 110)
        flag = False

    button = QtWidgets.QPushButton(window)
    button.move(265, 110)
    button.setText("Комната")
    button.clicked.connect(up)

    button1 = QtWidgets.QPushButton(window)
    button1.move(180, 150)
    button1.setText("Комната")
    button1.clicked.connect(left)

    button2 = QtWidgets.QPushButton(window)
    button2.move(350, 150)
    button2.setText("Комната")
    button2.clicked.connect(right)

    button3 = QtWidgets.QPushButton(window)
    button3.move(265, 195)
    button3.setText("Комната")
    button3.clicked.connect(down)

    window.show()  # НЕ ТРОГАЙ КОД, НЕ ТВОЁ!!!
    sys.exit(app.exec_())




if __name__ == "__main__":
    application()