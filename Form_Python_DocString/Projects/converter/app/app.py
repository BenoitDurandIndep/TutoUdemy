from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency converter")
        self.setup_ui()

    def setup_ui(self):
        self.layout=QtWidgets.QHBoxLayout(self)
        self.cbb_currFrom=QtWidgets.QComboBox()
        self.spn_amount=QtWidgets.QSpinBox()
        self.cbb_currTo=QtWidgets.QComboBox()
        self.spn_amountConverted=QtWidgets.QSpinBox()
        self.btn_reverse=QtWidgets.QPushButton("Reverse currencies")

        self.layout.addWidget(self.cbb_currFrom)
        self.layout.addWidget(self.spn_amount)
        self.layout.addWidget(self.cbb_currTo)
        self.layout.addWidget(self.spn_amountConverted)
        self.layout.addWidget(self.btn_reverse)


app= QtWidgets.QApplication([])
win=App()
win.show()

app.exec_()