import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QFontDatabase

app = QApplication(sys.argv)
widget = QWidget()
layout = QVBoxLayout(widget)

font1 = QFont()
font1.setStyleHint(QFont.Monospace)
fam1 = font1.defaultFamily()
font1.setFamily(fam1)

font2 = QFont()
font2.setStyleHint(QFont.TypeWriter)
fam2 = font2.defaultFamily()
font2.setFamily(fam1)

font3 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
fam3 = font3.family()

print(fam1)
print(fam2)
print(fam3)
