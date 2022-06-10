from PyQt5 import QtCore, QtGui, QtWidgets
from .system import Lotnisko

class Ui_dodawani_lotniska(object):
    def __init__(self,system):
        self.system=system
    def setupUi(self, dodawani_lotniska):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dodawani_lotniska.setWindowIcon(icon)
        dodawani_lotniska.setObjectName("dodawani_lotniska")
        dodawani_lotniska.resize(800, 600)
        dodawani_lotniska.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.verticalLayout = QtWidgets.QVBoxLayout(dodawani_lotniska)
        self.verticalLayout.setObjectName("verticalLayout")
        self.miasto = QtWidgets.QLabel(dodawani_lotniska)
        self.miasto.setMaximumSize(QtCore.QSize(140, 16777215))
        self.miasto.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.miasto.setObjectName("miasto")
        self.verticalLayout.addWidget(self.miasto)
        self.miejsce_na_miasto = QtWidgets.QLineEdit(dodawani_lotniska)
        self.miejsce_na_miasto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.miejsce_na_miasto.setObjectName("miejsce_na_miasto")
        self.verticalLayout.addWidget(self.miejsce_na_miasto)
        self.panstwo = QtWidgets.QLabel(dodawani_lotniska)
        self.panstwo.setMaximumSize(QtCore.QSize(140, 16777215))
        self.panstwo.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.panstwo.setObjectName("panstwo")
        self.verticalLayout.addWidget(self.panstwo)
        self.miejsce_na_panstwo = QtWidgets.QLineEdit(dodawani_lotniska)
        self.miejsce_na_panstwo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.miejsce_na_panstwo.setObjectName("miejsce_na_panstwo")
        self.verticalLayout.addWidget(self.miejsce_na_panstwo)
        self.frame = QtWidgets.QFrame(dodawani_lotniska)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anuluj = QtWidgets.QPushButton(self.frame)
        self.anuluj.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.anuluj.setObjectName("anuluj")
        self.anuluj.clicked.connect(dodawani_lotniska.close)
        self.horizontalLayout.addWidget(self.anuluj)
        self.dodaj = QtWidgets.QPushButton(self.frame)
        self.dodaj.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.dodaj.setObjectName("dodaj")
        self.dodaj.clicked.connect(self.dodaj_lotnisko)
        self.dodaj.clicked.connect(dodawani_lotniska.close)
        self.horizontalLayout.addWidget(self.dodaj)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(dodawani_lotniska)
        QtCore.QMetaObject.connectSlotsByName(dodawani_lotniska)

    def retranslateUi(self, dodawani_lotniska):
        _translate = QtCore.QCoreApplication.translate
        dodawani_lotniska.setWindowTitle(_translate("dodawani_lotniska", "Dodawanie lotniska"))
        self.miasto.setText(_translate("dodawani_lotniska", "<html><head/><body><p align=\"center\">Miasto</p></body></html>"))
        self.panstwo.setText(_translate("dodawani_lotniska", "<html><head/><body><p align=\"center\">Państwo</p></body></html>"))
        self.anuluj.setText(_translate("dodawani_lotniska", "anuluj"))
        self.dodaj.setText(_translate("dodawani_lotniska", "dodaj"))
        self.miejsce_na_miasto.setPlaceholderText(_translate("dodawani_lotniska", "Wpisz tutaj miasto."))
        self.miejsce_na_panstwo.setPlaceholderText(_translate("dodawanie_lotniska", "Wpisz tutaj państwo."))

    def dodaj_lotnisko(self):
        miasto=self.miejsce_na_miasto.text()
        panstwo=self.miejsce_na_panstwo.text()
        self.system.dodaj_lotnisko(Lotnisko(panstwo,miasto))



