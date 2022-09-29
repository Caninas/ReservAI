class Hospede:
    def __init__(self, nome: str, cpf: int, quarto=None):
        self.__nome = nome
        self.__cpf = int(cpf)
        self.__quarto = quarto  #objeto?


    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def quarto(self):
        return self.__quarto