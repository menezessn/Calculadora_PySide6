import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u'CompanyName.ProductName.SubProduct.VersionInformation')  # Arbitrary string


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    # icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 50px;')
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()
    window.show()
    app.exec()