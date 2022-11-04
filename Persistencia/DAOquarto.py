


# TEMPORARIO APENAS PARA TESTES


import pickle
from pathlib import Path
from Entidade.Quarto import Quarto


class DAOquarto:
    __instance = None       
    def __init__(self):
        self.__arquivo = f"{Path.home()}\Documents\Quartos.pkl"     #universializar path para o user (mudar?)
        self.__cache = {"quartos": []}

        try:
            self.abrir()
        except:
            self.guardar()

    def getQuarto(self, numero):          # CPF?
        objQuarto = 0
        print(self.__cache["quartos"])
        for quarto in self.__cache["quartos"]:
            if quarto.numero == numero:
                objQuarto = quarto

        return objQuarto

    def add(self, objeto: Quarto):
        if objeto != None and isinstance(objeto, Quarto):
            self.__cache["quartos"].append(objeto)  # guarda no cache local
            self.guardar(["quartos", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Quarto):
        if objeto != None and isinstance(objeto, Quarto):
            self.__cache["quartos"].remove(objeto)  # guarda no cache local
            self.guardar(["quartos", self.__cache])  # guarda no cache principal e no disco

    @property
    def cache(self):
        return self.__cache

    def __new__(cls):                                   
        if DAOquarto.__instance is None:
            DAOquarto.__instance = object.__new__(cls)
        return DAOquarto.__instance


    def guardar(self, data=None):
        if data != None:
            #self.__cache[data[0]] = data[1]
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
        self.__cache = {"quartos": []}
        pickle.dump(self.__cache, open(self.__arquivo, "wb"))