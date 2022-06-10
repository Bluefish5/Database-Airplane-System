

from PyQt5 import QtCore, QtGui, QtWidgets
from .system import Trasa

class Ui_menu_trasy(object):
    def __init__(self,system):
        self.system=system
    def setupUi(self, menu_trasy):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu_trasy.setWindowIcon(icon)
        menu_trasy.setObjectName("menu_trasy")
        menu_trasy.resize(600, 800)
        menu_trasy.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.verticalLayout = QtWidgets.QVBoxLayout(menu_trasy)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lotnisko_starowe = QtWidgets.QLabel(menu_trasy)
        self.lotnisko_starowe.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lotnisko_starowe.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lotnisko_starowe.setObjectName("lotnisko_starowe")
        self.verticalLayout.addWidget(self.lotnisko_starowe)
        self.lotnisko_startowe = QtWidgets.QComboBox(menu_trasy)
        self.lotnisko_startowe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lotnisko_startowe.setObjectName("lotnisko_startowe")

        for i in self.system.get_lotniska():
            self.lotnisko_startowe.addItem(str(i))

        self.verticalLayout.addWidget(self.lotnisko_startowe)
        self.lotnisko_konicowe_2 = QtWidgets.QLabel(menu_trasy)
        self.lotnisko_konicowe_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lotnisko_konicowe_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lotnisko_konicowe_2.setObjectName("lotnisko_konicowe_2")
        self.verticalLayout.addWidget(self.lotnisko_konicowe_2)


        self.lotnisko_konicowe = QtWidgets.QComboBox(menu_trasy)
        self.lotnisko_konicowe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lotnisko_konicowe.setObjectName("lotnisko_konicowe")

        for i in self.system.get_lotniska():
            self.lotnisko_konicowe.addItem(str(i))



        self.verticalLayout.addWidget(self.lotnisko_konicowe)
        self.podaj_czas_napis = QtWidgets.QLabel(menu_trasy)
        self.podaj_czas_napis.setMaximumSize(QtCore.QSize(200, 16777215))
        self.podaj_czas_napis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.podaj_czas_napis.setObjectName("podaj_czas_napis")
        self.verticalLayout.addWidget(self.podaj_czas_napis)
        self.podaj_czas_2 = QtWidgets.QLineEdit(menu_trasy)
        self.podaj_czas_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.podaj_czas_2.setObjectName("podaj_czas_2")
        self.verticalLayout.addWidget(self.podaj_czas_2)
        self.podajodleglosc_napis = QtWidgets.QLabel(menu_trasy)
        self.podajodleglosc_napis.setMaximumSize(QtCore.QSize(200, 16777215))
        self.podajodleglosc_napis.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.podajodleglosc_napis.setObjectName("podajodleglosc_napis")
        self.verticalLayout.addWidget(self.podajodleglosc_napis)
        self.podaj_odleglosc = QtWidgets.QLineEdit(menu_trasy)
        self.podaj_odleglosc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.podaj_odleglosc.setObjectName("podaj_odleglosc")
        self.verticalLayout.addWidget(self.podaj_odleglosc)
        self.frame = QtWidgets.QFrame(menu_trasy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(194, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anuluj = QtWidgets.QPushButton(self.frame)
        self.anuluj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.anuluj.setObjectName("anuluj")
        self.anuluj.clicked.connect(menu_trasy.close)
        self.horizontalLayout.addWidget(self.anuluj)
        self.dodaj = QtWidgets.QPushButton(self.frame)
        self.dodaj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.dodaj.setObjectName("dodaj")

        self.dodaj.clicked.connect(self.dodaj_trase)
        self.dodaj.clicked.connect(menu_trasy.close)

        self.horizontalLayout.addWidget(self.dodaj)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(menu_trasy)
        QtCore.QMetaObject.connectSlotsByName(menu_trasy)

    def retranslateUi(self, menu_trasy):
        _translate = QtCore.QCoreApplication.translate
        menu_trasy.setWindowTitle(_translate("menu_trasy", "menu_trasy"))
        self.lotnisko_starowe.setText(_translate("menu_trasy", "<html><head/><body><p align=\"center\">Lotnisko startowe:</p></body></html>"))
        self.lotnisko_konicowe_2.setText(_translate("menu_trasy", "<html><head/><body><p align=\"center\">Lotnisko końcowe</p></body></html>"))
        self.podaj_czas_napis.setText(_translate("menu_trasy", "<html><head/><body><p align=\"center\">Podaj czas:</p></body></html>"))
        self.podajodleglosc_napis.setText(_translate("menu_trasy", "<html><head/><body><p align=\"center\">Podaj odległość</p></body></html>"))
        self.anuluj.setText(_translate("menu_trasy", "anuluj"))
        self.dodaj.setText(_translate("menu_trasy", "dodaj"))
        self.podaj_odleglosc.setPlaceholderText(_translate("menu_trasy", "Wpisz tutaj odległość."))
        self.podaj_czas_2.setPlaceholderText(_translate("menu_trasy","Wpisz tutaj czas."))

    def dodaj_trase(self):
        lotnisko_1=self.lotnisko_startowe.currentText()
        lotnisko_2=self.lotnisko_konicowe.currentText()
        tab=[lotnisko_1,lotnisko_2]
        odleglosc=self.podaj_odleglosc.text()
        czas=self.podaj_czas_2.text()
        self.system.dodaj_trase(Trasa(tab,int(czas),int(odleglosc)))



