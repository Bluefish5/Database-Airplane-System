class Lotnisko:
    def __init__(self,kraj:str,miasto:str):
        self.__kraj=kraj
        self.__miasto=miasto
    def __str__(self):
        return "({},{})".format(self.__kraj,self.__miasto)
    def get_miasto(self):
        return self.__miasto
    def get_panstwo(self):
        return self.__kraj
