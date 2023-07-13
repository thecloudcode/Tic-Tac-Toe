from PyQt5 import QtCore, QtGui, QtWidgets
import resources1
from GamePlay import Ui_GameWindow
import images
from score2 import Ui_ScoreWindow
import webbrowser
from welcome import Ui_WelcomeWindow
from PyQt5.QtCore import QTimer


class Ui_TicTacToe(object):
    def OpenGamePlay(self):
        self.writeDataToFile()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self.window)
        self.ui.connectKeyEvents(self.window)
        self.window.show()

    # def OpenWelcomeWindow(self):
    #     self.window=QtWidgets.QMainWindow()
    #     self.ui=Ui_GameWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    def writeDataToFile(self):
        p1 = self.lineEdit.text()
        print("p1", p1)
        p2 = self.lineEdit_2.text()

        with open("data.txt", "w") as file:
            file.write(f"{p1}\n{p2}\n0\n0")

    def open_linkedin_profile(self):
        url = "https://www.linkedin.com/in/badalprasadsingh/"
        webbrowser.open(url)

    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.resize(1259, 740)
        self.centralwidget = QtWidgets.QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 761))
        self.label.setStyleSheet("\n"
                                 "background-image:url(:/background/Red and Black Dark Gamer Sports YouTube Banner.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-size: 1261px 761px;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 300, 370, 61))
        self.lineEdit.setStyleSheet("background-color: \'#031319\';\n"
                                    "        border: 3px solid \'#F60D7D\';\n"
                                    "        border-radius: 10px;\n"
                                    "        color: white;\n"
                                    "        font-size: 17px;\n"
                                    "padding-left: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 370, 370, 61))
        self.lineEdit_2.setStyleSheet("background-color: \'#031319\';\n"
                                      "        border: 3px solid \'#F60D7D\';\n"
                                      "        border-radius: 10px;\n"
                                      "        color: white;\n"
                                      "        font-size: 17px;\n"
                                      "padding-left: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,
                                                clicked=self.OpenGamePlay)  # Connect to OpenGamePlay
        self.pushButton.setGeometry(QtCore.QRect(430, 470, 370, 81))
        self.pushButton.setStyleSheet(" QPushButton{background-color: #F60D7D;\n"
                                      "        color: white;\n"
                                      "        border-radius: 10px;\n"
                                      "        font-size: 20px;\n"
                                      "        font-weight: bold;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color :#c50763;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.Contact = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_linkedin_profile())
        self.Contact.setGeometry(QtCore.QRect(1110, 10, 141, 41))
        self.Contact.setStyleSheet("QPushButton {\n"
                                   "    background-color: #661aff;\n"
                                   "    color: white;\n"
                                   "    border-radius: 10px;\n"
                                   "    font-size: 15px;\n"
                                   "    font-weight: bold;\n"
                                   "    box-shadow: 0 12px 14px rgba(0, 0, 0, 0.8);\n"
                                   "\n"
                                   "    \n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #3b00b3;\n"
                                   "    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.6);\n"
                                   "}\n"
                                   "")
        self.Contact.setObjectName("Contact")
        self.Player1name = QtWidgets.QPushButton(self.centralwidget)
        self.Player1name.setGeometry(QtCore.QRect(0, 640, 160, 61))
        self.Player1name.setStyleSheet(
            "        background-color: #f6097c;\n"
            "        border: 0px solid \'#f6097c\';\n"
            "        color: white;\n"
            "        font-size: 27px;\n"
            "        font-weight: bold;\n"
            "border-radius: 27px;\n"
            "text-align:center;\n"
            "")
        self.Player1name.setObjectName("Player1name")
        TicTacToe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TicTacToe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1259, 26))
        self.menubar.setObjectName("menubar")
        TicTacToe.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TicTacToe)
        self.statusbar.setObjectName("statusbar")
        TicTacToe.setStatusBar(self.statusbar)

        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton.setObjectName("pushButton")
        self.Contact.setObjectName("Contact")
        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

    def retranslateUi(self, TicTacToe):
        _translate = QtCore.QCoreApplication.translate
        TicTacToe.setWindowTitle(_translate("TicTacToe", "Tic Tac Toe - Badal"))
        self.label.setText(_translate("TicTacToe", "`"))
        self.lineEdit.setPlaceholderText(_translate("TicTacToe", "Enter Player 1..."))
        self.lineEdit_2.setPlaceholderText(_translate("TicTacToe", "Enter Player 2..."))
        self.pushButton.setText(_translate("TicTacToe", "START"))
        self.Contact.setText(_translate("TicTacToe", "CONTACT ME"))
        self.Player1name.setText(_translate("MainWindow", 'BADAL'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    welcomewindow = QtWidgets.QMainWindow()
    ui = Ui_WelcomeWindow()
    ui.setupUi(welcomewindow)
    app_icon = QtGui.QIcon('logo.png')
    welcomewindow.setWindowIcon(app_icon)
    welcomewindow.show()

    QTimer.singleShot(8000, lambda: welcomewindow.close())

    TicTacToe = QtWidgets.QMainWindow()
    ui = Ui_TicTacToe()
    ui.setupUi(TicTacToe)
    # TicTacToe.show()
    app_icon = QtGui.QIcon('logo.png')
    TicTacToe.setWindowIcon(app_icon)
    QTimer.singleShot(7000, lambda: TicTacToe.show())

    sys.exit(app.exec_())




