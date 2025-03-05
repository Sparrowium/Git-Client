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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 654)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerMenu = QWidget(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.centerMenu)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.stackedWidget = QStackedWidget(self.centerMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(40, 140, 120, 80))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 50, 79, 26))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.centerMenu, 0, 1, 1, 1)

        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.leftMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

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


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.leftMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.gridLayout.addWidget(self.leftMenu, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")

        self.gridLayout.addWidget(self.mainBody, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.localBox.setTitle(QCoreApplication.translate("MainWindow", u"LOCAL", None))
        self.tagsBox.setTitle(QCoreApplication.translate("MainWindow", u"TAGS", None))
        self.remoteBox.setTitle(QCoreApplication.translate("MainWindow", u"REMOTE", None))
        self.submodulesBox.setTitle(QCoreApplication.translate("MainWindow", u"SUBMODULES", None))
        self.issueBox.setTitle(QCoreApplication.translate("MainWindow", u"ISSUE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

