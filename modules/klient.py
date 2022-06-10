class Klient:
	def __init__(self):
		pass

class Osoba(Klient):
	def __init__(self,imie:str,nazwisko:str,pesel:str):
		super().__init__()
		self.__imie=imie
		self.__nazwisko=nazwisko
		self.__pesel=pesel
	def __str__(self):
		return "({},{},PESEL: {})".format(self.__imie,self.__nazwisko,self.__pesel)
	def get_imie(self):
		return self.__imie
	def get_nazwisko(self):
		return self.__nazwisko
	def get_pesel(self):
		return self.__pesel
class Firma(Klient):
	def get_imie(self):
		return self.__nazwa
	def get_nazwisko(self):
		return "-"
	def get_pesel(self):
		return self.__nip
	def __init__(self,nip:str,nazwa:str):
		super().__init__()
		self.__nip=nip
		self.__nazwa=nazwa
	def __str__(self):
		return "Firma: ({},{})".format(self.__nazwa,self.__nip)