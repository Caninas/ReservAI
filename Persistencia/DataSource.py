import pickle
from pathlib import Path


class DataSource:
    __instance = None       
    def __init__(self):
        self.__arquivo = f"{Path.home()}\Documents\ReservAI.pkl"     #universializar path para o user (mudar?)
        self.__cache = {"gerente":[], "funcionarios":[], "hospedes":[]}

        try:
            self.abrir()
        except:
            self.guardar()

    @property
    def cache(self):
        return self.__cache

    def __new__(cls):                                   
        if DataSource.__instance is None:
            DataSource.__instance = object.__new__(cls)
        return DataSource.__instance


    def guardar(self, data=None):
        if data != None:
            self.__cache[data[0]] = data[1]
            pickle.dump(self.__cache, open(self.__arquivo, "wb"))
        else:
            pickle.dump(self.__cache, open(self.__arquivo, "wb"))

    def abrir(self, data=None):
        if data != None:
            self.__cache = pickle.load(open(self.__arquivo, "rb"))
            return self.__cache[data]
        else:
            self.__cache = pickle.load(open(self.__arquivo, "rb"))


    def apagar(self):
        self.__cache = {"gerente":[], "funcionarios":[], "hospedes":[]}
        pickle.dump(self.__cache, open(self.__arquivo, "wb"))