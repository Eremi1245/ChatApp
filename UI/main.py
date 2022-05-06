import sys
from PyQt5 import QtWidgets

from UI.Views.py_format.messenger import Ui_MainWindow


class MainWindowQt(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.print_text_console)


    def print_text_console(self):
        self.text=self.ui.message_text.toPlainText()
        print(self.text)

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindowQt()
    window.show()
    sys.exit(app.exec_())
