
class Gerente:
    def __init__(self, nome: str, senha: str):
        self.__nome = nome
        self.__senha = senha


    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

