from PyQt5 import QtCore, QtGui, QtWidgets
import images
from score2 import Ui_ScoreWindow

flag=False
# color1 = "#083444";color2='#083444';color3='#083444';color4="#083444";color5="#083444";color6="#083444";color7="#083444";color8="#083444";color9="#083444"

class Ui_GameWindow(object):
    def OpenScore(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ScoreWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 761))
        self.label.setStyleSheet("\n"
"background-image: url(:/back/gameplayback2.png);\n"
"background-repeat: no-repeat;\n"
"background-size: 1261px 761px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 190, 101, 101))
        self.pushButton.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton.setText("7")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.setButtonTextToX(self.pushButton))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 190, 101, 101))
        self.pushButton_2.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_2.setText("8")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_2))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 190, 101, 101))
        self.pushButton_3.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_3.setText("9")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_3))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 310, 101, 91))
        self.pushButton_4.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color:'#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_4.setText("6")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_4))
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 310, 101, 91))
        self.pushButton_5.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_5.setText("5")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_5))
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 310, 101, 91))
        self.pushButton_6.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_6.setText("4")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_6))
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 410, 101, 101))
        self.pushButton_7.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_7.setText("1")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_7))
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 410, 101, 101))
        self.pushButton_8.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_8.setText("2")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_8))
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(690, 410, 101, 101))
        self.pushButton_9.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
f"        color: '#083444';\n"
"        font-size: 47px;\n"
"        font-weight: bold;\n"
"")
        self.pushButton_9.setText("3")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.setButtonTextToX(self.pushButton_9))
        self.player1label = QtWidgets.QPushButton(self.centralwidget)
        self.player1label.setGeometry(QtCore.QRect(150, 240, 231, 61))
        self.player1label.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
"        color: #8C52FF;\n"
"        font-size: 27px;\n"
"        font-weight: bold;")
        self.player1label.setObjectName("player1label")
        self.player2label = QtWidgets.QPushButton(self.centralwidget)
        self.player2label.setGeometry(QtCore.QRect(900, 240, 231, 61))
        self.player2label.setStyleSheet("background-color: black;\n"
"        border: 2px solid black;\n"
"        color: #8C52FF;\n"
"        font-size: 27px;\n"
"        font-weight: bold;\n"
"")
        self.player2label.setObjectName("player2label")

        with open("data.txt", "r") as file:
            lines = file.readlines()
        p1name=lines[0][:-1:]
        p2name=lines[1][:-1:]
        self.player1name = QtWidgets.QPushButton(self.centralwidget)
        self.player1name.setGeometry(QtCore.QRect(150, 320, 231, 81))
        self.player1name.setStyleSheet("background-color: '#F60D7D';\n"
"        border: 2px solid black;\n"
"border-radius: 17px;\n"
"        color: white;\n"
"        font-size: 27px;\n"
"        font-weight: bold;")
        self.player1name.setText(p1name)
        self.player1name.setObjectName("player1name")
        self.player2name = QtWidgets.QPushButton(self.centralwidget)
        self.player2name.setGeometry(QtCore.QRect(900, 330, 231, 81))
        self.player2name.setStyleSheet("background-color: '#F60D7D';\n"
"        border: 2px solid black;\n"
"        color: white;\n"
"border-radius: 17px;\n"
"        font-size: 27px;\n"
"        font-weight: bold;")
        self.player2name.setText(p2name)
        self.player2name.setObjectName("player2name")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Play - Badal"))
        self.label.setText(_translate("MainWindow", "``"))
        self.player1label.setText(_translate("MainWindow", "Player 1"))
        self.player2label.setText(_translate("MainWindow", "Player 2"))
        self.me.setText(_translate("MainWindow", 'BADAL'))

    def setButtonTextToX(self, button):
        print(button.objectName())
        x=str(button.objectName())[-1]
        button.setStyleSheet("background-color: black;\n"
                             "border: 2px solid black;\n"
                             f"color: white;\n"
                             "font-size: 47px;\n"
                             "font-weight: bold;\n"
                             )
        global flag  # Specify 'global' keyword to modify the global variable
        if flag:
            button.setText("O")
        else:
            button.setText("X")
        flag = not flag
        self.extractButtonText()

    def resetButtonText(self):
        self.pushButton.setText("7")
        self.pushButton_2.setText("8")
        self.pushButton_3.setText("9")
        self.pushButton_4.setText("6")
        self.pushButton_5.setText("5")
        self.pushButton_6.setText("4")
        self.pushButton_7.setText("1")
        self.pushButton_8.setText("2")
        self.pushButton_9.setText("3")
        buttons = [
            self.pushButton, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6,
            self.pushButton_7, self.pushButton_8, self.pushButton_9
        ]
        for button in buttons:
            button.setStyleSheet("background-color: black;\n"
                                 "border: 2px solid black;\n"
                                 f"color: '#083444';\n"
                                 "font-size: 47px;\n"
                                 "font-weight: bold;\n"
                                 )

    def extractButtonText(self):
        buttons = [
            [self.pushButton, self.pushButton_2, self.pushButton_3],
            [self.pushButton_6, self.pushButton_5, self.pushButton_4],
            [self.pushButton_7, self.pushButton_8, self.pushButton_9],
        ]
        # button_texts = [button.text() for button in buttons]
        button_texts = [buttons[0][0].text(),buttons[0][1].text(),buttons[0][2].text(),buttons[1][0].text(),buttons[1][1].text(),buttons[1][2].text(),buttons[2][0].text(),buttons[2][1].text(),buttons[2][2].text()]
        print(button_texts)

        if button_texts[0]==button_texts[1]==button_texts[2]:
            print("Player 1 Wins" if button_texts[0]=='X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[0]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[4]==button_texts[5]==button_texts[3]:
            print("Player 1 Wins" if button_texts[3] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[3]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[6]==button_texts[7]==button_texts[8]:
            print("Player 1 Wins" if button_texts[7] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[7]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[0]==button_texts[3]==button_texts[6]:
            print("Player 1 Wins" if button_texts[0] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[0]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[1]==button_texts[4]==button_texts[7]:
            print("Player 1 Wins" if button_texts[1] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[1]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[2]==button_texts[5]==button_texts[8]:
            print("Player 1 Wins" if button_texts[2] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[2]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[0]==button_texts[4]==button_texts[8]:
            print("Player 1 Wins" if button_texts[0] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[0]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts[2]==button_texts[4]==button_texts[6]:
            print("Player 1 Wins" if button_texts[4] == 'X' else 'Player 2 Wins')
            self.PlayerOneWins() if button_texts[4]=='X' else self.PlayerTwoWins()
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
        elif button_texts.count('X')+button_texts.count('O')==len(button_texts):
            print("Draw")
            self.resetButtonText()
            self.OpenScore()
            # sys.exit(app.exec_())
    def handleKeyPress(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_1:
            self.setButtonTextToX(self.pushButton_7)
        if key == QtCore.Qt.Key_2:
            self.setButtonTextToX(self.pushButton_8)
        if key == QtCore.Qt.Key_3:
            self.setButtonTextToX(self.pushButton_9)
        if key == QtCore.Qt.Key_6:
            self.setButtonTextToX(self.pushButton_4)
        if key == QtCore.Qt.Key_5:
            self.setButtonTextToX(self.pushButton_5)
        if key == QtCore.Qt.Key_4:
            self.setButtonTextToX(self.pushButton_6)
        if key == QtCore.Qt.Key_7:
            self.setButtonTextToX(self.pushButton)
        if key == QtCore.Qt.Key_8:
            self.setButtonTextToX(self.pushButton_2)
        if key == QtCore.Qt.Key_9:
            self.setButtonTextToX(self.pushButton_3)

    def PlayerOneWins(self):
        with open("data.txt", "r") as file:
            lines = file.readlines()
        lines[2]=str(int(lines[2])+1)+'\n'
        with open("data.txt","w") as file:
            file.writelines(lines)

    def PlayerTwoWins(self):
        with open("data.txt", "r") as file:
            lines = file.readlines()
        lines[3]=str(int(lines[3])+1)
        with open("data.txt","w") as file:
            file.writelines(lines)

    def connectKeyEvents(self, MainWindow):
        MainWindow.keyPressEvent = self.handleKeyPress

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GameWindow()
    ui.setupUi(MainWindow)
    ui.connectKeyEvents(MainWindow)
    app_icon = QtGui.QIcon('logo.png')
    MainWindow.setWindowIcon(app_icon)
    MainWindow.show()
    sys.exit(app.exec_())
