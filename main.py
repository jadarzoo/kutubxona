from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
app = QApplication([])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        contain = QWidget()
        layoud = QVBoxLayout(contain)
        btn = QPushButton("Dasturga kirish")
        layoud.addWidget(btn)
        self.setCentralWidget(conrain)


window = Window()
window.show()
app.exec()

