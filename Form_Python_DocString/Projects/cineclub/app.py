from PySide2 import QtWidgets,QtCore
from movie import Movie,get_movies


class App(QtWidgets.QWidget):

	APP_TITLE="Cine Club"

	def __init__(self):
		super().__init__()
		self.setWindowTitle(self.APP_TITLE)
		self.setup_ui()
		self.populate_movies()
		#self.setup_connections()
		#self.setup_css()

	def setup_ui(self):
		self.layout = QtWidgets.QVBoxLayout(self)
		self.lie_title = QtWidgets.QLineEdit()
		self.btn_addMovie = QtWidgets.QPushButton("Add movie")
		self.lw_listMovies = QtWidgets.QListWidget()
		self.btn_remove = QtWidgets.QPushButton("Remove the movie(s)")

		self.layout.addWidget(self.lie_title)
		self.layout.addWidget(self.btn_addMovie)
		self.layout.addWidget(self.lw_listMovies)
		self.layout.addWidget(self.btn_remove)

	def populate_movies(self):
		for movie in get_movies():
			lw_item=QtWidgets.QListWidgetItem(movie.title)
			lw_item.setData(QtCore.Qt.UserRole,movie)
			self.lw_listMovies.addItem(lw_item)


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()