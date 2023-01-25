from PyQt5 import QtCore, QtGui, QtWidgets
from calculator_ui import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(lambda: self.button_click(0))
        self.pushButton_1.clicked.connect(lambda: self.button_click(1))
        self.pushButton_2.clicked.connect(lambda: self.button_click(2))
        self.pushButton_3.clicked.connect(lambda: self.button_click(3))
        self.pushButton_4.clicked.connect(lambda: self.button_click(4))
        self.pushButton_5.clicked.connect(lambda: self.button_click(5))
        self.pushButton_6.clicked.connect(lambda: self.button_click(6))
        self.pushButton_7.clicked.connect(lambda: self.button_click(7))
        self.pushButton_8.clicked.connect(lambda: self.button_click(8))
        self.pushButton_9.clicked.connect(lambda: self.button_click(9))

        self.pushButton_add.clicked.connect(lambda: self.button_click("+"))
        self.pushButton_subtract.clicked.connect(lambda: self.button_click("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.button_click("*"))
        self.pushButton_divide.clicked.connect(lambda: self.button_click("/"))
        self.pushButton_equal.clicked.connect(self.evaluate)

    def button_click(self, number):
        current = self.lineEdit.text()
        self.lineEdit.setText(current + str(number))

    def evaluate(self):
        current = self.lineEdit.text()
        try:
            self.lineEdit.setText(str(eval(current)))
        except:
            self.lineEdit.setText("Error")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())