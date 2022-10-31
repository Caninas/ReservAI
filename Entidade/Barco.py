from socket import NI_NUMERICHOST
from telnetlib import STATUS


class Barco:
    def __init__(self, descricao: str, numero: int, status: int, valor: float):
        self.__descricao = descricao
        self.__numero = numero
        self.__status = status
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @property
    def numero(self):
        return self.__numero

    @property
    def status(self):
        return self.__status

    @property
    def valor(self):
        return self.__valor

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @status.setter
    def status(self, status):
        self.__status = status
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
