from Entidade.Quarto import Quarto


class ReservaQuarto:
    def __init__(self, 
    cod: int, status: int, quarto: Quarto, l_hospedes: list,
    data_reserva: str, data_entrada: str, 
    data_saida: str, data_checkin: str = None, data_checkout: str = None,
    valor:float = None):
        self.__cod = cod
        self.__status = status
        self.__quarto = quarto
        self.__lista_hospedes = l_hospedes
        self.__data_reserva = data_reserva
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida

        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout
        self.__valor = valor                        # funçao(quarto.valor * calculo data) valor_total?
    
    def info_basica(self):         # opcional
        return {"codigo": self.__cod,
                "status": self.__status,
                "quarto": self.__quarto,
                "l_hospedes": self.__lista_hospedes,
                "data_reserva": self.__data_reserva,
                "data_entrada": self.__data_entrada,
                "data_saida": self.__data_saida}

    @property
    def cod(self):
        return self.__cod

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status =  valor

    @property
    def quarto(self):
        return self.__quarto

    @property
    def valor(self):
        return self.__valor

    @property
    def lista_hospedes(self):
        return self.__lista_hospedes

    @lista_hospedes.setter
    def lista_hospedes(self, valor):
        self.__lista_hospedes = valor
    
    @property
    def data_reserva(self):
        return self.__data_reserva

    @property
    def data_entrada(self):
        return self.__data_entrada
    
    @property
    def data_saida(self):
        return self.__data_saida

    @property
    def data_checkin(self):
        return self.__data_checkin
    
    @property
    def data_checkout(self):
        return self.__data_checkout

