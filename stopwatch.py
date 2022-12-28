import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import QFont


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')

        # Set the window dimensions
        self.resize(150, 200)

        # Create the LCD number display for the stopwatch
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setDigitCount(8)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setProperty("value", 0.0)
        self.lcd.setObjectName("lcd")

        # Create the start/stop button
        self.btn = QPushButton('Start')
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.startStop)

        # Create the reset button
        self.resetBtn = QPushButton('Reset')
        self.resetBtn.clicked.connect(self.reset)

        # Use a vertical layout to arrange the widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.resetBtn)
        self.setLayout(vbox)

        # Create a timer to update the stopwatch every 1/10th of a second
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateLCD)

        # Initialize the stopwatch to 0
        self.time = 0

    def startStop(self):
        if self.btn.isChecked():
            self.btn.setText('Stop')
            self.timer.start()
        else:
            self.btn.setText('Start')
            self.timer.stop()

    def reset(self):
        self.time = 0
        self.lcd.display(self.time)

    def updateLCD(self):
        self.time += 0.1
        self.lcd.display(self.time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
