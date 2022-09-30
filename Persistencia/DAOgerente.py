import pickle
from Entidade.Gerente import Gerente


# from cryptography.fernet import Fernet

class DAOgerente():
    def __init__(self, dataSource):
        self.__main = dataSource
        self.__cache = []

        self.abrir("gerente")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def getGerente(self, usuario):
        objGerente = 0
        for gerente in self.__cache:
            if gerente.nome == usuario:
                objGerente = gerente

        return objGerente

    def add(self, objeto: Gerente):
        if objeto != None and isinstance(objeto, Gerente):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["gerente", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Gerente):
        if objeto != None and isinstance(objeto, Gerente):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["gerente", self.__cache])  # guarda no cache principal e no disco
