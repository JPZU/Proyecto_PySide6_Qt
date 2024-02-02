# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kanbantKozuQ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 328)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lista_Pendientes = QListWidget(self.centralwidget)
        self.lista_Pendientes.setObjectName(u"lista_Pendientes")

        self.gridLayout.addWidget(self.lista_Pendientes, 2, 0, 1, 1)

        self.lista_EnProgreso = QListWidget(self.centralwidget)
        self.lista_EnProgreso.setObjectName(u"lista_EnProgreso")

        self.gridLayout.addWidget(self.lista_EnProgreso, 2, 1, 1, 1)

        self.label_EnProgreso = QLabel(self.centralwidget)
        self.label_EnProgreso.setObjectName(u"label_EnProgreso")
        self.label_EnProgreso.setStyleSheet(u"background-color: #87CEFA;\n"
"text-transform: uppercase;\n"
"font: bold")

        self.gridLayout.addWidget(self.label_EnProgreso, 1, 1, 1, 1)

        self.label_Titulo = QLabel(self.centralwidget)
        self.label_Titulo.setObjectName(u"label_Titulo")
        self.label_Titulo.setStyleSheet(u"background-color: #A9A9A9;\n"
"text-transform: uppercase;\n"
"font: bold\n"
"")

        self.gridLayout.addWidget(self.label_Titulo, 0, 1, 1, 1)

        self.Lista_Completadas = QListWidget(self.centralwidget)
        self.Lista_Completadas.setObjectName(u"Lista_Completadas")

        self.gridLayout.addWidget(self.Lista_Completadas, 2, 2, 1, 1)

        self.label_Pendientes = QLabel(self.centralwidget)
        self.label_Pendientes.setObjectName(u"label_Pendientes")
        self.label_Pendientes.setStyleSheet(u"background-color: #F08080;\n"
"text-transform: uppercase;\n"
"font: bold")

        self.gridLayout.addWidget(self.label_Pendientes, 1, 0, 1, 1)

        self.label_Completadas = QLabel(self.centralwidget)
        self.label_Completadas.setObjectName(u"label_Completadas")
        self.label_Completadas.setStyleSheet(u"background-color: #32CD32;\n"
"text-transform: uppercase;\n"
"font: bold")

        self.gridLayout.addWidget(self.label_Completadas, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_EnProgreso.setText(QCoreApplication.translate("MainWindow", u"En Progreso", None))
        self.label_Titulo.setText(QCoreApplication.translate("MainWindow", u"Tablero Kanban", None))
        self.label_Pendientes.setText(QCoreApplication.translate("MainWindow", u"Pendientes", None))
        self.label_Completadas.setText(QCoreApplication.translate("MainWindow", u"Completadas", None))
    # retranslateUi

