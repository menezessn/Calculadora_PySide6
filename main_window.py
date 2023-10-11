
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        # Layout básico
        super().__init__(parent, *args, *kwargs)
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        # Título
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Ultimos ajustes
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
