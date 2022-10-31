from Barco import Barco


class Reserva_Barco:
    def __init__(self, barco: Barco, cod: int, cod_reserva: int, 
    data_entrada: str,data_reserva: str, data_saida: str, 
    status: int, valor: float):
        self.__barco = barco
        self.__cod = cod
        self.__cod_reserva = cod_reserva
        self.__data_entrada = data_entrada
        self.__data_reserva = data_reserva
        self.__data_saida = data_saida
        self.__status = status
        self.__valor = valor
    
    @property
    def barco(self):
        return self.__barco
    
    @property
    def cod(self):
        return self.__cod
    
    @property
    def cod_reserva(self):
        return self.__cod_reserva
    
    @property
    def data_entrada(self):
        return self.__data_entrada
    
    @property
    def data_reserva(self):
        return self.__data_reserva
    
    @property
    def data_saida(self):
        return self.__data_saida

    @property
    def status(self):
        return self.__status

    @property
    def valor(self):
        return self.__valor