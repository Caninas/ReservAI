
class Gerente:
    def __init__(self, nome: str, usuario: str, senha: str):
        self.__nome = nome
        self.__usuario = usuario
        self.__senha = senha


    @property
    def nome(self):
        return self.__nome

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha

