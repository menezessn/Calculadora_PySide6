from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QMainWindow()
    
    cw = QWidget()
    v_layout = QVBoxLayout()
    cw.setLayout(v_layout)

    label1 = QLabel('O meu texto')
    v_layout.addWidget(label1)

    window.setCentralWidget(cw)
    window.show()
    app.exec()