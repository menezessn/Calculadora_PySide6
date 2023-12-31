from PySide6.QtWidgets import QPushButton, QGridLayout
from typing import TYPE_CHECKING
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from PySide6.QtCore import Slot

if TYPE_CHECKING:
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, info, window: 'MainWindow',  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._grid_mask = [
            ['C', 'del', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua Conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(lambda: print(123))
        self.display.delPressed.connect(self.display.backspace)
        self.display.clear.connect(lambda: print(123))

        for i, row in enumerate(self._grid_mask):
            for j, buttonText in enumerate(row):
                if buttonText == '':
                    continue
                if buttonText == '0':
                    button = Button(buttonText)
                    self.addWidget(button, i, 0, 1, 2)
                    slot = self._makeSlot( self._insertButtonTextToDisplay, button)
                    self._connectButtonClicked(button, slot)
                    continue
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                
                self.addWidget(button, i, j)
                slot = self._makeSlot( self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            slot = self._makeSlot(self._clear)
            self._connectButtonClicked(button, slot)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
                )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

        if text == 'del':
            self._connectButtonClicked(button, self.display.backspace)
            

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Faltou um número na conta.')
            return
        
        if self._left is None:
            self._showError('Faltou um número na conta.')
            return
            
        
        result = 'error'
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = eval(self.equation.replace('^', '**'))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self.display.setText(str(result))
        self._right = None
        self._left = result
        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()