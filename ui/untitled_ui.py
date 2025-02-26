# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(887, 654)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")

        self.gridLayout.addWidget(self.mainBody, 0, 2, 1, 1)

        self.centerMenu = QWidget(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")

        self.gridLayout.addWidget(self.centerMenu, 0, 1, 1, 1)

        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.leftMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 10, 87, 26))

        self.verticalLayout.addWidget(self.widget_4)

        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.localBox = QGroupBox(self.widget)
        self.localBox.setObjectName(u"localBox")
        self.localBox.setFlat(False)
        self.localBox.setCheckable(True)

        self.verticalLayout_2.addWidget(self.localBox)

        self.tagsBox = QGroupBox(self.widget)
        self.tagsBox.setObjectName(u"tagsBox")
        self.tagsBox.setFlat(False)
        self.tagsBox.setCheckable(True)

        self.verticalLayout_2.addWidget(self.tagsBox)

        self.remoteBox = QGroupBox(self.widget)
        self.remoteBox.setObjectName(u"remoteBox")
        self.remoteBox.setFlat(False)
        self.remoteBox.setCheckable(True)

        self.verticalLayout_2.addWidget(self.remoteBox)

        self.submodulesBox = QGroupBox(self.widget)
        self.submodulesBox.setObjectName(u"submodulesBox")
        self.submodulesBox.setFlat(False)
        self.submodulesBox.setCheckable(True)

        self.verticalLayout_2.addWidget(self.submodulesBox)

        self.issueBox = QGroupBox(self.widget)
        self.issueBox.setObjectName(u"issueBox")
        self.issueBox.setFlat(True)
        self.issueBox.setCheckable(True)

        self.verticalLayout_2.addWidget(self.issueBox)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout.addWidget(self.leftMenu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.localBox.setTitle(QCoreApplication.translate("MainWindow", u"LOCAL", None))
        self.tagsBox.setTitle(QCoreApplication.translate("MainWindow", u"TAGS", None))
        self.remoteBox.setTitle(QCoreApplication.translate("MainWindow", u"REMOTE", None))
        self.submodulesBox.setTitle(QCoreApplication.translate("MainWindow", u"SUBMODULES", None))
        self.issueBox.setTitle(QCoreApplication.translate("MainWindow", u"ISSUE", None))
    # retranslateUi

