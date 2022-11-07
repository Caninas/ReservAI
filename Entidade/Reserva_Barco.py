from Entidade.Barco import Barco


class Reserva_Barco:
    def __init__(self, barco: Barco, cod: int, cod_reserva: int, status: int, data_reserva: str,
    valor: float):
        self.__barco = barco
        self.__cod = cod
        self.__cod_reserva = cod_reserva
        self.__status = status
        self.__data_reserva = data_reserva
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
    def status(self):
        return self.__status
    
    @property
    def data_reserva(self):
        return self.__data_reserva

    @property
    def valor(self):
        return self.__valor
    
    @status.setter
    def status(self, status):
        self.__status = status

    def info_basica(self):         # opcional
        return {"codigo": self.__cod,
                "cod_reserva": self.__cod_reserva,
                "data": self.__data_reserva,
                "data_reserva": self.__data_reserva,
                "valor": self.__valor,
                "barco": self.__barco}
