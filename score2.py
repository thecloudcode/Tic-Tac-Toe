from PyQt5 import QtCore, QtGui, QtWidgets
import images

class Ui_ScoreWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 761))
        self.label.setStyleSheet("background-image: url(:/back/inbetween.png);\n"
"\n"
"background-repeat: no-repeat;\n"
"background-size: 1261px 761px;")
        self.label.setObjectName("label")
        self.player2label = QtWidgets.QPushButton(self.centralwidget)
        self.player2label.setGeometry(QtCore.QRect(490, 230, 331, 191))
        self.player2label.setStyleSheet("background-color: \'#031319\';\n"
"        border: 2px solid \'#031319\';\n"
"        color: white;\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"border: 2px solid white;\n"
"border-radius: 17px;\n"
"padding: 7px;\n"
"")
        self.player2label.setObjectName("player2label")
        self.Player1name = QtWidgets.QPushButton(self.centralwidget)
        self.Player1name.setGeometry(QtCore.QRect(120, 290, 231, 61))
        self.Player1name.setStyleSheet("background-color: \'#031319\';\n"
"        border: 2px solid \'#031319\';\n"
"        color: white;\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"text-align:right;\n"
"")
        self.Player1name.setObjectName("Player1name")
        self.Player2Name = QtWidgets.QPushButton(self.centralwidget)
        self.Player2Name.setGeometry(QtCore.QRect(950, 290, 231, 61))
        self.Player2Name.setStyleSheet("background-color: \'#031319\';\n"
"        border: 2px solid \'#031319\';\n"
"        color: white;\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"text-align:left;")
        self.Player2Name.setObjectName("Player2Name")
        self.Player2Score = QtWidgets.QPushButton(self.centralwidget)
        self.Player2Score.setGeometry(QtCore.QRect(870, 290, 61, 61))
        self.Player2Score.setStyleSheet("background-color: \'#8C52FF\';\n"
"        border: 2px solid \'#031319\';\n"
"        color: white;\n"
"        font-size: 37px;\n"
"        font-weight: bold;\n"
"\n"
"border-radius: 7px;")
        self.Player2Score.setObjectName("Player2Score")
        self.Player1Score = QtWidgets.QPushButton(self.centralwidget)
        self.Player1Score.setGeometry(QtCore.QRect(380, 290, 61, 61))
        self.Player1Score.setStyleSheet("background-color: \'#8C52FF\';\n"
"        border: 2px solid \'#8C52FF\';\n"
"        color: white;\n"
"        font-size: 37px;\n"
"        font-weight: bold;\n"
"border-radius: 7px;\n"
"")
        self.Player1Score.setObjectName("Player1Score")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: MainWindow.close())

        self.pushButton.setGeometry(QtCore.QRect(480, 500, 251, 91))
        self.pushButton.setStyleSheet("QPushButton{background-color: \'#F60D7D\';\n"
"color: white;\n"
"font-size: 27px;\n"
"font-weight: bold;\n"
"border-radius: 17px;\n"
"box-shadow: 0 2px 4px rgba(0, 0, 0, 1);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: \'#d72151\'; \n"
"box-shadow: 0 4px 8px rgba(0, 0, 0, 1);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.closeAll())
        self.pushButton_3.setGeometry(QtCore.QRect(740, 500, 101, 91))
        self.pushButton_3.setStyleSheet("\n"
"\n"
"QPushButton{background-color: white;\n"
"color: \'#fb3768\';\n"
"font-size: 27px;\n"
"font-weight: bold;\n"
"border-radius: 17px;\n"
"box-shadow: 0 4px 8px rgba(0, 0, 0, 1);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: \'#fecdd9\'; \n"
"box-shadow: 0 4px 8px rgba(0, 0, 0, 1);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(450, 120, 411, 61))
        self.result.setStyleSheet("background-color: \'#031319\';\n"
                                       "        border: 2px solid \'#031319\';\n"
                                       "        color: #8C52FF;\n"
                                       "        font-size: 47px;\n"
                                       "        font-weight: bold;")
        self.result.setObjectName("Result")
        self.label.raise_()
        self.Player1name.raise_()
        self.Player2Name.raise_()
        self.result.raise_()
        self.Player2Score.raise_()
        self.Player1Score.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.player2label.raise_()
        self.me = QtWidgets.QPushButton(self.centralwidget)
        self.me.setGeometry(QtCore.QRect(7, 640, 160, 61))
        self.me.setStyleSheet(
            "        background-color: #f6097c;\n"
            "        border: 0px solid \'#f6097c\';\n"
            "        color: white;\n"
            "        font-size: 27px;\n"
            "        font-weight: bold;\n"
            "border-radius: 27px;\n"
            "text-align:center;\n"
            "")
        self.me.setObjectName("me")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Score - Badal"))
        self.label.setText(_translate("MainWindow", "`"))
        self.player2label.setText(_translate("MainWindow", "SCORE"))
        with open("data.txt", "r") as file:
            lines = file.readlines()
        self.Player1name.setText(_translate("MainWindow", lines[0]))
        self.Player2Name.setText(_translate("MainWindow", lines[1]))
        self.Player2Score.setText(_translate("MainWindow", lines[3][0]))
        self.Player1Score.setText(_translate("MainWindow", lines[2][0]))
        if int(lines[2][0])>int(lines[3][0]):
            self.result.setText(_translate("MainWindow", f'{lines[0][:-1:]} wins!'))
        elif int(lines[2][0])<int(lines[3][0]):
            self.result.setText(_translate("MainWindow", f"{lines[1][:-1:]} wins!"))
        else:
            self.result.setText(_translate("MainWindow", f'Draw!'))
        # self.result.setText(_translate("MainWindow",'My mum raised a Genius!'))
        self.pushButton.setText(_translate("MainWindow", "Restart"))
        self.pushButton_3.setText(_translate("MainWindow", "End"))
        self.me.setText(_translate("MainWindow", 'BADAL'))

    def closeScoreWindow(self):
        MainWindow.close()

    def closeAll(self):
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ScoreWindow()
    ui.setupUi(MainWindow)
    app_icon = QtGui.QIcon('logo.png')
    MainWindow.setWindowIcon(app_icon)
    MainWindow.show()
    sys.exit(app.exec_())
