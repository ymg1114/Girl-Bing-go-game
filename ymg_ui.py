# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ymg_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 655)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(620, 30, 160, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GameStart = QPushButton(self.verticalLayoutWidget)
        self.GameStart.setObjectName(u"GameStart")

        self.verticalLayout.addWidget(self.GameStart)

        self.RandomShuffle = QPushButton(self.verticalLayoutWidget)
        self.RandomShuffle.setObjectName(u"RandomShuffle")
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.RandomShuffle.setPalette(palette)

        self.verticalLayout.addWidget(self.RandomShuffle)

        self.Close = QPushButton(self.verticalLayoutWidget)
        self.Close.setObjectName(u"Close")

        self.verticalLayout.addWidget(self.Close)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 500, 500))
        self.widget.setMouseTracking(True)
        self.widget.setTabletTracking(True)
        self.widget.setAcceptDrops(True)
        self.ScoreBoard = QLCDNumber(self.centralwidget)
        self.ScoreBoard.setObjectName(u"ScoreBoard")
        self.ScoreBoard.setGeometry(QRect(620, 170, 158, 141))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(620, 150, 71, 16))
        self.EmptySpace1 = QWidget(self.centralwidget)
        self.EmptySpace1.setObjectName(u"EmptySpace1")
        self.EmptySpace1.setGeometry(QRect(620, 350, 100, 100))
        self.EmptySpace1.setMouseTracking(True)
        self.EmptySpace1.setTabletTracking(True)
        self.EmptySpace1.setAcceptDrops(True)
        self.EmptySpace2 = QWidget(self.centralwidget)
        self.EmptySpace2.setObjectName(u"EmptySpace2")
        self.EmptySpace2.setGeometry(QRect(620, 500, 100, 100))
        self.EmptySpace2.setMouseTracking(True)
        self.EmptySpace2.setTabletTracking(True)
        self.EmptySpace2.setAcceptDrops(True)
        self.asd = QLabel(self.centralwidget)
        self.asd.setObjectName(u"asd")
        self.asd.setGeometry(QRect(620, 330, 91, 16))
        self.qwe = QLabel(self.centralwidget)
        self.qwe.setObjectName(u"qwe")
        self.qwe.setGeometry(QRect(620, 480, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 816, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GameStart.setText(QCoreApplication.translate("MainWindow", u"GameStart", None))
        self.RandomShuffle.setText(QCoreApplication.translate("MainWindow", u"RandomShuffle", None))
        self.Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ScoreBoard", None))
        self.asd.setText(QCoreApplication.translate("MainWindow", u"EmptySpace 1", None))
        self.qwe.setText(QCoreApplication.translate("MainWindow", u"EmptySpace 2", None))
    # retranslateUi

