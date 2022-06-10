from PyQt5 import QtCore, QtGui, QtWidgets
from .klient import Osoba,Firma

class Menu_klient(object):
    def __init__(self,system):
        self.system=system

    def setupUi(self, Dialog):

        Dialog.setObjectName("Klienci")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        Dialog.setWindowIcon(icon)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.zmien_na_firme = QtWidgets.QPushButton(self.page)
        self.zmien_na_firme.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.zmien_na_firme.setObjectName("zmien_na_firme")

        self.zmien_na_firme.clicked.connect(self.zmiana_na_firma)
        self.verticalLayout_2.addWidget(self.zmien_na_firme)
        self.imie = QtWidgets.QLabel(self.page)
        self.imie.setMinimumSize(QtCore.QSize(0, 0))
        self.imie.setMaximumSize(QtCore.QSize(140, 16777215))
        self.imie.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.imie.setObjectName("imie")
        self.verticalLayout_2.addWidget(self.imie)
        self.miejsce_na_imie = QtWidgets.QLineEdit(self.page)
        self.miejsce_na_imie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.miejsce_na_imie.setObjectName("miejsce_na_imie")

        self.verticalLayout_2.addWidget(self.miejsce_na_imie)
        self.nazwisko = QtWidgets.QLabel(self.page)
        self.nazwisko.setMaximumSize(QtCore.QSize(140, 16777215))
        self.nazwisko.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.nazwisko.setObjectName("nazwisko")
        self.verticalLayout_2.addWidget(self.nazwisko)
        self.mijesce_na_nazwisko = QtWidgets.QLineEdit(self.page)
        self.mijesce_na_nazwisko.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mijesce_na_nazwisko.setObjectName("mijesce_na_nazwisko")
        self.verticalLayout_2.addWidget(self.mijesce_na_nazwisko)
        self.pesel = QtWidgets.QLabel(self.page)
        self.pesel.setMaximumSize(QtCore.QSize(140, 16777215))
        self.pesel.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.pesel.setObjectName("pesel")
        self.verticalLayout_2.addWidget(self.pesel)
        self.mijejsce_na_pesel = QtWidgets.QLineEdit(self.page)
        self.mijejsce_na_pesel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mijejsce_na_pesel.setObjectName("mijejsce_na_pesel")
        self.verticalLayout_2.addWidget(self.mijejsce_na_pesel)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.przycisk_anuluj = QtWidgets.QPushButton(self.frame)
        self.przycisk_anuluj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.przycisk_anuluj.setObjectName("przycisk_anuluj")
        self.przycisk_anuluj.clicked.connect(Dialog.close)

        self.horizontalLayout.addWidget(self.przycisk_anuluj)
        self.przycisk_dodaj = QtWidgets.QPushButton(self.frame)
        self.przycisk_dodaj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.przycisk_dodaj.setObjectName("przycisk_dodaj")
        self.przycisk_dodaj.clicked.connect(self.dodaj_klient)
        self.przycisk_dodaj.clicked.connect(Dialog.close)


        self.horizontalLayout.addWidget(self.przycisk_dodaj)
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.zmiana_na_klient)

        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.nazwa_firmy = QtWidgets.QLabel(self.page_2)
        self.nazwa_firmy.setMaximumSize(QtCore.QSize(140, 16777215))
        self.nazwa_firmy.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.nazwa_firmy.setObjectName("nazwa_firmy")
        self.verticalLayout_3.addWidget(self.nazwa_firmy)
        self.miejsce_na_nazwe_firmy = QtWidgets.QLineEdit(self.page_2)
        self.miejsce_na_nazwe_firmy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.miejsce_na_nazwe_firmy.setObjectName("miejsce_na_nazwe_firmy")
        self.verticalLayout_3.addWidget(self.miejsce_na_nazwe_firmy)
        self.nip = QtWidgets.QLabel(self.page_2)
        self.nip.setMaximumSize(QtCore.QSize(140, 16777215))
        self.nip.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.nip.setObjectName("nip")
        self.verticalLayout_3.addWidget(self.nip)
        self.miejsce_na_nip = QtWidgets.QLineEdit(self.page_2)
        self.miejsce_na_nip.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.miejsce_na_nip.setObjectName("miejsce_na_nip")
        self.verticalLayout_3.addWidget(self.miejsce_na_nip)
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.przycisk_anuluj_2 = QtWidgets.QPushButton(self.frame_2)
        self.przycisk_anuluj_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.przycisk_anuluj_2.setObjectName("przycisk_anuluj_2")
        self.przycisk_anuluj_2.clicked.connect(Dialog.close)

        self.horizontalLayout_2.addWidget(self.przycisk_anuluj_2)
        self.przycisk_dodaj_2 = QtWidgets.QPushButton(self.frame_2)
        self.przycisk_dodaj_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.przycisk_dodaj_2.setObjectName("przycisk_dodaj_2")
        self.przycisk_dodaj_2.clicked.connect(self.dodaj_firma)
        self.przycisk_dodaj_2.clicked.connect(Dialog.close)
        self.horizontalLayout_2.addWidget(self.przycisk_dodaj_2)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dodawanie klienta"))
        self.zmien_na_firme.setText(_translate("Dialog", "zmien na firme"))
        self.imie.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Imie</p></body></html>"))
        self.nazwisko.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Nazwisko</p></body></html>"))
        self.pesel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Pesel</p></body></html>"))
        self.przycisk_anuluj.setText(_translate("Dialog", "anuluj"))
        self.przycisk_dodaj.setText(_translate("Dialog", "dodaj"))
        self.pushButton_2.setText(_translate("Dialog", "zmien na klianta"))
        self.nazwa_firmy.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Nazwa firmy:</p></body></html>"))
        self.nip.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Nip</p></body></html>"))
        self.przycisk_anuluj_2.setText(_translate("Dialog", "anuluj"))
        self.przycisk_dodaj_2.setText(_translate("Dialog", "dodaj"))
        self.miejsce_na_nazwe_firmy.setPlaceholderText(_translate("Dialog", "Wpisz tutaj nazwe firmy."))
        self.miejsce_na_imie.setPlaceholderText(_translate("Dialog", "Wpisz tutaj imię."))
        self.mijesce_na_nazwisko.setPlaceholderText(_translate("Dialog", "Wpisz tutaj nazwisko."))
        self.mijejsce_na_pesel.setPlaceholderText(_translate("Dialog", "Wpisz tutaj pesel."))
        self.miejsce_na_nip.setPlaceholderText(_translate("Dialog", "Wpisz tutaj nip."))


    def zmiana_na_klient(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def zmiana_na_firma(self):
        self.stackedWidget.setCurrentWidget(self.page_2)


    def dodaj_klient(self):
        imie=self.miejsce_na_imie.text()
        nazwisko=self.mijesce_na_nazwisko.text()
        pesel=self.mijejsce_na_pesel.text()
        self.system.dodaj_klienta(Osoba(imie,nazwisko,pesel))



    def dodaj_firma(self):
        nip=self.miejsce_na_nip.text()
        nazwa_firmy=self.miejsce_na_nazwe_firmy.text()
        self.system.dodaj_klienta(Firma(nip,nazwa_firmy))


