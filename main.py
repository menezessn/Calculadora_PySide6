import sys
from PySide6.QtWidgets import (QApplication)
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid


if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u'CompanyName.ProductName.SubProduct.VersionInformation')
    # Arbitrary string


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info('teste')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    # grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
