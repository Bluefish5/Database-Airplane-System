from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuloty(object):
    def __init__(self,system):
        self.system=system

    def setupUi(self, menuloty):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menuloty.setWindowIcon(icon)
        menuloty.setObjectName("menuloty")
        menuloty.resize(800, 600)
        menuloty.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.verticalLayout = QtWidgets.QVBoxLayout(menuloty)
        self.verticalLayout.setObjectName("verticalLayout")
        self.napis_trasa = QtWidgets.QLabel(menuloty)
        self.napis_trasa.setMaximumSize(QtCore.QSize(200, 16777215))
        self.napis_trasa.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.napis_trasa.setObjectName("napis_trasa")
        self.verticalLayout.addWidget(self.napis_trasa)
        self.wybierz_trase = QtWidgets.QComboBox(menuloty)
        self.wybierz_trase.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybierz_trase.setObjectName("wybierz_trase")
        self.verticalLayout.addWidget(self.wybierz_trase)

        for i in range(len(self.system.get_trasy())):
            self.wybierz_trase.addItem(str(i)+". "+str(self.system.get_trasy()[i]))


        self.napisczas = QtWidgets.QLabel(menuloty)
        self.napisczas.setMaximumSize(QtCore.QSize(200, 16777215))
        self.napisczas.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.napisczas.setObjectName("napisczas")
        self.verticalLayout.addWidget(self.napisczas)
        self.wybierz_czas = QtWidgets.QTimeEdit(menuloty)
        self.wybierz_czas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybierz_czas.setObjectName("wybierz_czas")
        self.verticalLayout.addWidget(self.wybierz_czas)
        self.napi_data = QtWidgets.QLabel(menuloty)
        self.napi_data.setMaximumSize(QtCore.QSize(200, 16777215))
        self.napi_data.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.napi_data.setObjectName("napi_data")
        self.verticalLayout.addWidget(self.napi_data)
        self.wybierz_date = QtWidgets.QDateEdit(menuloty)
        self.wybierz_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybierz_date.setObjectName("wybierz_date")
        self.verticalLayout.addWidget(self.wybierz_date)
        self.frame = QtWidgets.QFrame(menuloty)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anuluj = QtWidgets.QPushButton(self.frame)
        self.anuluj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.anuluj.setObjectName("anuluj")
        self.anuluj.clicked.connect(menuloty.close)
        self.horizontalLayout.addWidget(self.anuluj)
        self.dodaj = QtWidgets.QPushButton(self.frame)
        self.dodaj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.dodaj.setObjectName("dodaj")

        self.dodaj.clicked.connect(self.dodaj_lot)
        self.dodaj.clicked.connect(menuloty.close)

        self.horizontalLayout.addWidget(self.dodaj)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(menuloty)
        QtCore.QMetaObject.connectSlotsByName(menuloty)

    def retranslateUi(self, menuloty):
        _translate = QtCore.QCoreApplication.translate
        menuloty.setWindowTitle(_translate("menuloty", "Dodawanie lotu"))
        self.napis_trasa.setText(_translate("menuloty", "<html><head/><body><p align=\"center\">Wybierz trase:</p></body></html>"))
        self.napisczas.setText(_translate("menuloty", "<html><head/><body><p align=\"center\">Wybierz czas:</p></body></html>"))
        self.napi_data.setText(_translate("menuloty", "<html><head/><body><p align=\"center\">Wybierz date: </p></body></html>"))
        self.anuluj.setText(_translate("menuloty", "anuluj"))
        self.dodaj.setText(_translate("menuloty", "dodaj"))

    def dodaj_lot(self):
        trasa=self.wybierz_trase.currentText().split(".")
        data=self.wybierz_date.text()
        czas=self.wybierz_czas.text()
        x=self.system.get_trasy()[int(trasa[0])]
        self.system.generuj_lot(x,str(data),str(czas))



