class Rezerwacja:
    def __init__(self,klient,ilosc_biletow:int):
        self.__klient=klient
        self.__ilosc_biletow=ilosc_biletow
    def get_ilosc_biletow(self):
        return self.__ilosc_biletow
    def get_klient(self):
        return self.__klient

