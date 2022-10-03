import pickle
from Entidade.Hospede import Hospede


class DAOhospede:
    def __init__(self, dataSource):
        self.__main = dataSource
        self.__cache = []

        self.abrir("hospedes")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def atualizar(self):
        self.__main.guardar(["hospedes", self.__cache])

    def getHospede(self, cpf):
        objHospede = 0
        for hospede in self.__cache:
            if hospede.cpf == int(cpf):
                objHospede = hospede

        return objHospede

    def add(self, objeto: Hospede):
        if objeto != None and isinstance(objeto, Hospede):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["hospedes", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Hospede):
        if objeto != None and isinstance(objeto, Hospede):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["hospedes", self.__cache])  # guarda no cache principal e no disco
