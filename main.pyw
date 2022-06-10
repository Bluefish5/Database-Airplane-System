from modules import *

system = System()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    System_rezerwacji_biletow = QtWidgets.QMainWindow()
    ui = Ui_System_rezerwacji_biletow(system)
    ui.setupUi(System_rezerwacji_biletow)
    System_rezerwacji_biletow.show()
    sys.exit(app.exec_())

