
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        # Layout básico
        super().__init__(parent, *args, *kwargs)
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        # Título
        self.setWindowTitle('Calculadora')
        
    def adjustFixedSize(self):
        # Ultimos ajustes
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        self.adjustFixedSize()