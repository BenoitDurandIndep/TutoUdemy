from PySide2 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):

	#Constants
	APP_TITLE="Currency converter"
	DEF_CURR="EUR"
	DEF_VAL=100
	MIN_RANGE=1
	MAX_RANGE=1000000

	def __init__(self):
		super().__init__()
		self.c = currency_converter.CurrencyConverter()
		self.setWindowTitle(self.APP_TITLE)
		self.setup_ui()
		self.set_default_values()
		self.setup_connections()
		self.setup_css()

	def setup_ui(self):
		self.layout = QtWidgets.QHBoxLayout(self)
		self.cbb_currFrom = QtWidgets.QComboBox()
		self.spn_amount = QtWidgets.QSpinBox()
		self.cbb_currTo = QtWidgets.QComboBox()
		self.spn_amountConverted = QtWidgets.QSpinBox()
		self.btn_reverse = QtWidgets.QPushButton("Reverse currencies")

		self.layout.addWidget(self.cbb_currFrom)
		self.layout.addWidget(self.spn_amount)
		self.layout.addWidget(self.cbb_currTo)
		self.layout.addWidget(self.spn_amountConverted)
		self.layout.addWidget(self.btn_reverse)

	def set_default_values(self):
		self.cbb_currFrom.addItems(sorted(list(self.c.currencies)))
		self.cbb_currTo.addItems(sorted(list(self.c.currencies)))
		self.cbb_currFrom.setCurrentText(self.DEF_CURR)
		self.cbb_currTo.setCurrentText(self.DEF_CURR)

		self.spn_amount.setRange(self.MIN_RANGE,self.MAX_RANGE)
		self.spn_amountConverted.setRange(self.MIN_RANGE,self.MAX_RANGE)
		self.spn_amount.setValue(self.DEF_VAL)
		self.spn_amountConverted.setValue(self.DEF_VAL)

	def setup_connections(self):
		self.cbb_currFrom.activated.connect(self.compute)
		self.cbb_currTo.activated.connect(self.compute)
		self.spn_amount.valueChanged.connect(self.compute)
		self.btn_reverse.clicked.connect(self.revert_curr)

	def compute(self):
		amount = self.spn_amount.value()
		curr_from = self.cbb_currFrom.currentText()
		curr_to = self.cbb_currTo.currentText()
		
		try:
			res = self.c.convert(amount, curr_from, curr_to)
		except currency_converter.currency_converter.RateNotFoundError:
			print("Conversion failed")
		else:
			self.spn_amountConverted.setValue(res)

	def revert_curr(self):
		curr_from = self.cbb_currFrom.currentText()
		curr_to = self.cbb_currTo.currentText()
		self.cbb_currFrom.setCurrentText(curr_to)
		self.cbb_currTo.setCurrentText(curr_from)
		self.compute()

	def setup_css(self):
		self.setStyleSheet("""
		background-color:rgb(30,30,30);
		color: rgb(240,240,240);
		border:none;
		""")

app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()
