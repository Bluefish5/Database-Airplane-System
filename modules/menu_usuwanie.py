
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_usuwanie(object):
    def __init__(self,system,item):
        self.system=system
        self.item=item
    def setupUi(self, usuwanie):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("modules/ikony/plane.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        usuwanie.setWindowIcon(icon)
        usuwanie.setObjectName("usuwanie")
        usuwanie.resize(800, 600)
        usuwanie.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.verticalLayout = QtWidgets.QVBoxLayout(usuwanie)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wybiersz_element = QtWidgets.QComboBox(usuwanie)
        self.wybiersz_element.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wybiersz_element.setObjectName("wybiersz_element")
        self.verticalLayout.addWidget(self.wybiersz_element)
        self.frame = QtWidgets.QFrame(usuwanie)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.anuluj_przycisk = QtWidgets.QPushButton(self.frame)
        self.anuluj_przycisk.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.anuluj_przycisk.setObjectName("anuluj_przycisk")
        self.anuluj_przycisk.setMinimumSize(QtCore.QSize(180,50))
        self.anuluj_przycisk.clicked.connect(usuwanie.close)

        self.horizontalLayout.addWidget(self.anuluj_przycisk)
        self.usun_przycisk = QtWidgets.QPushButton(self.frame)
        self.usun_przycisk.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.usun_przycisk.setObjectName("usun_przycisk")
        self.usun_przycisk.setMinimumSize(QtCore.QSize(180,50))
        self.horizontalLayout.addWidget(self.usun_przycisk)
        self.verticalLayout.addWidget(self.frame)

        if self.item == 1:
            for i in range(len(self.system.get_klienci())):
                self.wybiersz_element.addItem(str(i)+". "+str((self.system.get_klienci()[i])))
            self.usun_przycisk.clicked.connect(self.usun_klient)
        elif self.item ==2:
            for i in range(len(self.system.get_samoloty())):
                self.wybiersz_element.addItem(str(i)+". "+str((self.system.get_samoloty()[i])))
            self.usun_przycisk.clicked.connect(self.usun_samoloty)
        elif self.item == 3:
            for i in range(len(self.system.get_trasy())):
                self.wybiersz_element.addItem(str(i)+". "+str((self.system.get_trasy()[i])))
            self.usun_przycisk.clicked.connect(self.usun_trasy)
        elif self.item == 4:
            for i in range(len(self.system.get_lotniska())):
                self.wybiersz_element.addItem(str(i)+". "+str((self.system.get_lotniska()[i])))
            self.usun_przycisk.clicked.connect(self.usun_lotniska)
        elif self.item == 5:
            for i in range(len(self.system.get_loty())):
                self.wybiersz_element.addItem(str(i)+". "+str((self.system.get_loty()[i])))
            self.usun_przycisk.clicked.connect(self.usun_loty)

        self.usun_przycisk.clicked.connect(usuwanie.close)
        self.retranslateUi(usuwanie)
        QtCore.QMetaObject.connectSlotsByName(usuwanie)

    def retranslateUi(self, usuwanie):
        _translate = QtCore.QCoreApplication.translate
        usuwanie.setWindowTitle(_translate("usuwanie", "Usuwanie"))
        self.anuluj_przycisk.setText(_translate("usuwanie", "anuluj"))
        self.usun_przycisk.setText(_translate("usuwanie", "usun"))

    def usun_klient(self):
        index=self.wybiersz_element.currentText().split(".")
        self.system.get_klienci().remove(self.system.get_klienci()[int(index[0])])
    def usun_samoloty(self):
        index=self.wybiersz_element.currentText().split(".")
        self.system.get_samoloty().remove(self.system.get_samoloty()[int(index[0])])
    def usun_trasy(self):
        index=self.wybiersz_element.currentText().split(".")
        self.system.get_trasy().remove(self.system.get_trasy()[int(index[0])])
    def usun_lotniska(self):
        index=self.wybiersz_element.currentText().split(".")
        self.system.get_lotniska().remove(self.system.get_lotniska()[int(index[0])])
    def usun_loty(self):
        index=self.wybiersz_element.currentText().split(".")
        self.system.get_loty().remove(self.system.get_loty()[int(index[0])])

