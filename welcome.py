
from PyQt5 import QtCore, QtGui, QtWidgets
import newfront
class Ui_WelcomeWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 621))
        self.label.setStyleSheet("background-image: url(:/go/first2.png);")
        self.label.setObjectName("label")
        self.Player1name = QtWidgets.QPushButton(self.centralwidget)
        self.Player1name.setGeometry(QtCore.QRect(370, 290, 231, 61))
        self.Player1name.setStyleSheet(
                                       "        border: 0px solid \'#031319\';\n"
                                       "        color: #f6097c;\n"
                                       "        font-size: 27px;\n"
                                       "        font-weight: bold;\n"
                                       "text-align:right;\n"
                                       "")
        self.Player1name.setObjectName("Player1name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome - Badal"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.Player1name.setText(_translate("MainWindow", 'Loading...'))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(MainWindow)
    app_icon = QtGui.QIcon('logo.png')
    MainWindow.setWindowIcon(app_icon)
    MainWindow.show()
    sys.exit(app.exec_())
