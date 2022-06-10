
from PyQt5 import QtCore, QtGui, QtWidgets



class menu_rezerwacja(object):
    def __init__(self,system):
        self.system=system
    def setupUi(self, Dialog):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.wybierz_lot = QtWidgets.QComboBox(Dialog)
        self.wybierz_lot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybierz_lot.setObjectName("wybierz_lot")

        for i in range(len(self.system.get_loty())):
            self.wybierz_lot.addItem(str(i)+". "+str(self.system.get_loty()[i]))

        self.verticalLayout.addWidget(self.wybierz_lot)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.wybierz_klienta = QtWidgets.QComboBox(Dialog)
        self.wybierz_klienta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybierz_klienta.setObjectName("wybierz_klienta")

        for i in range(len(self.system.get_klienci())):
            self.wybierz_klienta.addItem(str(i)+". "+str(self.system.get_klienci()[i]))

        self.verticalLayout.addWidget(self.wybierz_klienta)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.ilosc_miejsc = QtWidgets.QSpinBox(Dialog)
        self.ilosc_miejsc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ilosc_miejsc.setMaximum(999)
        self.ilosc_miejsc.setObjectName("ilosc_miejsc")
        self.verticalLayout.addWidget(self.ilosc_miejsc)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anuluj = QtWidgets.QPushButton(self.frame)
        self.anuluj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.anuluj.setObjectName("anuluj")
        self.anuluj.clicked.connect(Dialog.close)
        self.horizontalLayout.addWidget(self.anuluj)
        self.rezerwuj = QtWidgets.QPushButton(self.frame)
        self.rezerwuj.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.rezerwuj.setObjectName("rezerwuj")

        self.rezerwuj.clicked.connect(self.rezerwuj_fun)
        self.rezerwuj.clicked.connect(Dialog.close)

        self.horizontalLayout.addWidget(self.rezerwuj)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rezerwacja"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Wybierz lot:</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Wybierz klienta:</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Ilość miejsc:</p></body></html>"))
        self.anuluj.setText(_translate("Dialog", "anuluj"))
        self.rezerwuj.setText(_translate("Dialog", "rezerwuj"))

    def rezerwuj_fun(self):

        ile_miejsc=int(self.ilosc_miejsc.text())
        index_lotu=int(self.wybierz_lot.currentText().split(".")[0])
        index_klienta=int(self.wybierz_klienta.currentText().split(".")[0])
        self.system.get_loty()[index_lotu].rezerwuj(self.system.get_klienci()[index_klienta],ile_miejsc)
        #print(self.system.get_loty()[0].get_zajete())




