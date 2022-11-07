class Quarto:
    def __init__(self, numero: int, capacidade: int, cama_c: int, cama_s: int, valor: float, descricao: str, status: int):
        self.__numero = int(numero)
        self.__capacidade = int(capacidade)
        self.__cama_c = cama_c
        self.__cama_s = cama_s
        self.__valor = valor
        self.__descriçao = descricao
        self.__status = status
    
    def get_info(self):
        return [self.__numero,
                self.__capacidade,
                self.__cama_c,
                self.__cama_s,
                self.__valor,
                self.__descriçao,
                self.__status]

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def valor(self):
        return self.__valor

    @property
    def numero(self):
        return self.__numero