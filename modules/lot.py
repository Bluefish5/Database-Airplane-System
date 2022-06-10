from .rezerwacja import Rezerwacja

class Lot:
    def __init__(self, samolot, trasa,data, godzina):
        self.__samolot=samolot
        self.__trasa=trasa
        self.__klienci=[]
        self.__data=data
        self.__godzina=godzina
        self.__rezerwacje=[]
    def get_samolot(self):
        return self.__samolot
    def get_data(self):
        return self.__data
    def get_zajete(self)->int:
        suma=0
        for rez in self.__rezerwacje:
            suma+=rez.get_ilosc_biletow()
        return suma
    def get_trasa(self):
        return self.__trasa
    def __str__(self):
        return "{}, Samolot {}, {} {}".format(self.__trasa.__str__(),self.__samolot.__str__(),self.__data,self.__godzina)

    def rezerwuj(self,klient,ilosc)->bool:

        if self.__samolot.get_miejsca()<=self.get_zajete()+ilosc:
            return False
        else:
            self.__rezerwacje.append(Rezerwacja(klient,ilosc))
            return True