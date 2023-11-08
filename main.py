#!/usr/bin/env/ python3

# This Projetc is a usr project that calculate of money percentage
# Created on 9 October, 2023 by Henry
# Main Program Here

from PySide6.QtWidgets import QApplication
import sys
from mWin import MWin

app = QApplication(sys.argv)
window = MWin()
window.show()

app.exec()

