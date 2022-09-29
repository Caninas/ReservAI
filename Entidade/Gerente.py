
class Gerente:
    def __init__(self, nome: str, cpf: str, senha: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
