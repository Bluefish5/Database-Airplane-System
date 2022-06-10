class Trasa:
    def __init__(self,lotniska:list,odleglosc:int,czas:int):
        self.__lotniska=lotniska
        self.__odleglosc=odleglosc
        self.__czas=czas
    def get_odleglosc(self)->int:
        return self.__odleglosc
    def get_czas(self)->int:
        return self.__czas
    def __str__(self):
        return "{}->{}, {}km {}min".format(self.__lotniska[0].__str__(),self.__lotniska[1].__str__(),self.__odleglosc,self.__czas)
    def get_lotniska_w_trasy(self):
        return  self.__lotniska