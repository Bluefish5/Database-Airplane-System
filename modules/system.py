from .klient import *
from .samoloty import *
from .trasa import Trasa
from .lotnisko import Lotnisko
from .lot import Lot
import pickle


class System:
    def __init__(self):
        self.__flota=[]
        self.__klienci=[]
        self.__lotniska=[]
        self.__trasy=[]
        self.__loty=[]
        self.__running=True
        self.odczytaj_wszystko()
    #############

    #############
    def dodaj_klienta(self, klient: Klient):
        self.__klienci.append(klient)
    def usun_klienta(self, klient: Klient):
        self.__klienci.remove(klient)
    def get_klienci(self)->list:
        return self.__klienci
    ##############
    def dodaj_samolot(self, samolot: Samolot):
        self.__flota.append(samolot)
    def usun_samolot(self, samolot: Samolot):
        self.__flota.remove(samolot)
    def get_samoloty(self)->list:
        return self.__flota
    ##############
    def dodaj_trase(self, trasa: Trasa):
        self.__trasy.append(trasa)
    def usun_trase(self, trasa: Trasa):
        self.__trasy.remove(trasa)
    def get_trasy(self)->list:
        return self.__trasy
    ##############
    def dodaj_lotnisko(self, lotnisko: Lotnisko):
        self.__lotniska.append(lotnisko)
    def usun_lotnisko(self, lotnisko: Lotnisko):
        self.__lotniska.remove(lotnisko)
    def get_lotniska(self)->list:
        return self.__lotniska
    ##############
    def dodaj_lot(self,lot):
        self.__loty.append(lot)
    def get_loty(self)->list:
        return self.__loty
    def usun_lot(self,lot):
        self.__loty.remove(lot)

    def generuj_lot(self,trasa:Trasa,data:str,godzina:str)->bool:
        samolot_class=self.optymalny_samolot(trasa.get_odleglosc())
        print(samolot_class)
        for i in self.__flota:
            #print(self.jest_zajety(i,data))
            #print("i",isinstance(i,samolot_class))
            print(type(i).__name__)

            if isinstance(i,samolot_class) and not self.jest_zajety(i,data):
                self.__loty.append(Lot(i,trasa,data,godzina))
                return True
        return False

    ##############
    def jest_zajety(self,samolot,data)->bool:
        for i in self.__loty:
            if i.get_samolot() == samolot and i.get_data() == data:
                return True
        return False
    def optymalny_samolot(self,odleglosc:int):
        if 0 <=odleglosc <=800:
            return Regionalny
        elif 800 <= odleglosc <= 2500:
            return Waskokadlubowy
        elif 2500 <= odleglosc <= 8000:
            return Szerokokadlubowy
        else:
            return 0
    def zapis(self,path,func):
        with open(path,"wb") as handle:
            for i in func():
                pickle.dump(i,handle,protocol=pickle.HIGHEST_PROTOCOL)
    def odczyt(self,path,func):
        with open(path,"rb") as handle:
            arr=[]
            while 1:
                try:
                    arr.append(pickle.load(handle))
                except EOFError:
                    break
            for i in arr:
                func(i)

    def zapisz_wszystko(self):
        self.zapis("modules/data/klienci.pkl",self.get_klienci)
        self.zapis("modules/data/lotniska.pkl",self.get_lotniska)
        self.zapis("modules/data/loty.pkl",self.get_loty)
        self.zapis("modules/data/samoloty.pkl",self.get_samoloty)
        self.zapis("modules/data/trasy.pkl",self.get_trasy)

    def odczytaj_wszystko(self):
        self.__flota=[]
        self.__klienci=[]
        self.__lotniska=[]
        self.__trasy=[]
        self.__loty=[]
        self.odczyt("modules/data/klienci.pkl",self.dodaj_klienta)
        self.odczyt("modules/data/lotniska.pkl",self.dodaj_lotnisko)
        self.odczyt("modules/data/loty.pkl",self.dodaj_lot)
        self.odczyt("modules/data/samoloty.pkl",self.dodaj_samolot)
        self.odczyt("modules/data/trasy.pkl",self.dodaj_trase)

    ######WERSJA TERMINAL#######
    def pokaz(self,func):
        arr=func()
        for i in range(len(arr)):
            print("{}. {}".format(i,arr[i].__str__()))
    def is_running(self):
        return self.__running
    def close(self):
        self.__running=False
        return "System zamkniety"
    def usun_pozycje(self,getter,show,delete):
        arr=getter()
        length=len(arr)
        if length<=0:
            print("Brak danych")
            return
        else:
            show(getter)
            num=int(input("Podaj numer pozycji ktora chcesz usunac: "))
            if 0 <= num <= length-1:
                delete(arr[num])
            else:
                print("Błąd")

    def lotnisko_menu(self):
        choose=input("1. Pokaz lotniska\n2. Dodaj lotnisko\n3. Usun lotnisko\n4. Wroc\n")
        if choose=='1':
            self.pokaz(self.get_lotniska)
        elif choose=='2':
            miasto=input("Podaj miasto: ")
            panstwo=input("Podaj panstwo: ")
            self.dodaj_lotnisko(Lotnisko(panstwo,miasto))
        elif choose=='3':
            self.usun_pozycje(self.get_lotniska,self.pokaz,self.usun_lotnisko)
        elif choose=='4':
            return
        else:
            print("Blad")
        wait()

    def klient_menu(self):
        choose=input("1. Pokaz klientow\n2. Dodaj klienta\n3. Usun klienta\n4. Wroc\n")
        if choose=='1':
            self.pokaz(self.get_klienci)
        elif choose == '2':
            type_choose=input("1. Dodaj Osobe\n2. Dodaj Firme\n")
            if type_choose=='1':
                imie=input("Podaj imie: ")
                nazwisko=input("Podaj nazwisko: ")
                pesel=input("Podaj pesel: ")
                self.dodaj_klienta(Osoba(imie,nazwisko,pesel))
            elif type_choose=='2':
                nazwa=input("Podaj nazwe: ")
                nip=input("Podaj nip: ")
                self.dodaj_klienta(Firma(nip,nazwa))
            else:
                print("Blad")
        elif choose == '3':
            self.usun_pozycje(self.get_klienci,self.pokaz,self.usun_klienta)
        elif choose=='4':
            return
        else:
            print("Blad")
        wait()
    def samolot_menu(self):
        choose=input("1. Pokaz samoloty\n2. Dodaj Samolot\n3. Usun Samolot\n4. Wroc\n")
        if choose=='1':
            self.pokaz(self.get_samoloty)
        elif choose=='2':
            samoloty_dict = {'1': Regionalny,
                             '2': Waskokadlubowy,
                             '3': Szerokokadlubowy
                             }
            samolot_type=input("1. Regionalny\n2. Waskokadlubowy\n3. Szerokokadlubowy\n")
            try:
                self.dodaj_samolot(samoloty_dict[samolot_type]())
            except KeyError:
                print("Blad")
        elif choose=='3':
            self.usun_pozycje(self.get_samoloty,self.pokaz,self.usun_samolot)
        elif choose=='4':
            return
        else:
            print("Blad")
        wait()
    def trasa_menu(self):
        choose=input("1. Pokaz trasy\n2. Dodaj trase\n3. Usun trase\n4. Wroc\n")
        if choose=='1':
            self.pokaz(self.get_trasy)
        elif choose=='2':
            self.pokaz(self.get_lotniska)
            inp1=int(input("Wybierz nr pierwszego lotniska: "))
            inp2=int(input("Wybierz nr drugiego lotniska: "))
            odleglosc=int(input("Podaj odleglosc: "))
            czas=int(input("Podaj czas: "))
            self.dodaj_trase(Trasa([self.get_lotniska()[inp1],self.get_lotniska()[inp2]],odleglosc,czas))
        elif choose=='3':
            self.usun_pozycje(self.get_trasy,self.pokaz,self.usun_trase)
        elif choose=='4':
            return
        wait()
    def lot_menu(self):
        choose=input("1. Pokaz loty\n2. Generuj lot\n3. Usun lot\n4. Rezerwuj Bilet\n5. Wroc\n")
        if choose=='1':
            self.pokaz(self.get_loty)
        elif choose=='2':
            self.pokaz(self.get_trasy)
            inp=int(input("Wybierz nr trasy: "))
            data=input("Wpisz date w formacie dd.mm.yyyy: ")
            godzina=input("Wpisz godzine w formacie hh:mm: ")
            try:
                if not self.generuj_lot(self.get_trasy()[inp],data,godzina):
                    print("Wystapil blad przy generowaniu lotu")
            except IndexError:
                print("Nie ma takiego lotu")
        elif choose=='3':
            self.usun_pozycje(self.get_loty,self.pokaz,self.usun_lot)
        elif choose=='4':
            arr_loty=self.get_loty()
            self.pokaz(self.get_loty)
            nr_lotu=int(input("Wybierz nr lotu: "))
            arr_klient=self.get_klienci()
            self.pokaz(self.get_klienci)
            nr_klienta=int(input("Wybierz klienta: "))
            try:
                if isinstance(arr_klient[nr_klienta],Osoba):
                    if not arr_loty[nr_lotu].rezerwuj(arr_klient[nr_klienta],1,True):
                        print("Brak wolnych miejsc lub klient juz zarezerwowal bilet")
                elif isinstance(arr_klient[nr_klienta],Firma):
                    ilosc=int(input("Podaj ilosc biletow do zarezerwowania: "))
                    if not arr_loty[nr_lotu].rezerwuj(arr_klient[nr_klienta],ilosc):
                        print("Brak wolnych miejsc")
            except IndexError:
                print("Wystapil blad przy wyborze klienta lub lotu")
        elif choose=='5':
            return
        else:
            print("Blad")
        wait()

def wait():
    input("Wcisnij enter aby kontynuowac")

