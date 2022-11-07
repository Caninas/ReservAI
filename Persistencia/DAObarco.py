from Entidade.Barco import Barco


class DAObarco:
    def __init__(self, dataSource):
        self.__main = dataSource
        self.__cache = []

        self.abrir("barcos")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def getBarco(self, numero):
        objBarco = 0
        for barco in self.__cache:
            if barco.numero == numero:
                objBarco = barco
        return objBarco

    def add(self, objeto: Barco):
        if objeto != None and isinstance(objeto, Barco):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["barcos", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Barco):
        if objeto != None and isinstance(objeto, Barco):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["barcos", self.__cache])  # guarda no cache principal e no disco
