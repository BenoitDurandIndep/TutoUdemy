from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies


class App(QtWidgets.QWidget):

    APP_TITLE = "Cine Club"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.APP_TITLE)
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        # self.setup_css()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.lie_title = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Add movie")
        self.lw_listMovies = QtWidgets.QListWidget()
        self.lw_listMovies.setSelectionMode(
            QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove = QtWidgets.QPushButton("Remove the movie(s)")

        self.layout.addWidget(self.lie_title)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_listMovies)
        self.layout.addWidget(self.btn_remove)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movie)
        self.lie_title.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        for movie in get_movies():
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_listMovies.addItem(lw_item)

    def add_movie(self):
        myTitle = self.lie_title.text()
        if not myTitle:
            return False
        else:
            myMovie = Movie(title=myTitle)
            added = myMovie.add_to_movies()
            if added:
                lw_item = QtWidgets.QListWidgetItem(myMovie.title)
                lw_item.setData(QtCore.Qt.UserRole, myMovie)
                self.lw_listMovies.addItem(lw_item)
                self.lie_title.setText("")
                return True
            else:
                self.lie_title.setText("")
                return False

    def remove_movie(self):
        for selected_item in self.lw_listMovies.selectedItems():
            myMovie = selected_item.data(QtCore.Qt.UserRole)
            myMovie.remove_from_movies()
            self.lw_listMovies.takeItem(self.lw_listMovies.row(selected_item))
        return True


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()
