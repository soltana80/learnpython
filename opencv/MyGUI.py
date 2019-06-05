

print("Hallo fucking world!")
import sys
from PyQt5 import QtWidgets
from src.MainWindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()

main_window = Ui_MainWindow()

main_window.setupUi(window)


window.show()

sys.exit(app.exec_())



