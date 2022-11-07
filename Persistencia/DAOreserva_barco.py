from Entidade.Reserva_Barco import Reserva_Barco


class DAOreserva_barco:
    def __init__(self, dataSource):
        self.__main = dataSource
        self.__cache = []

        self.abrir("reservas_barcos")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def atualizar(self):
        self.__main.guardar(["reservas_barcos", self.__cache])


    def getCodUltimaReservaBarco(self):
        maior_cod = 0
        for reserva in self.__cache:
            if reserva.cod > maior_cod:
                maior_cod = reserva.cod
        
        return maior_cod


    def getReserva_barco(self, cod):
        objReserva = 0
        for reserva in self.__cache:
            if reserva.cod == int(cod):
                objReserva = reserva

        return objReserva

    def add(self, objeto: Reserva_Barco):
        if objeto != None and isinstance(objeto, Reserva_Barco):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["reservas_barcos", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Reserva_Barco):
        if objeto != None and isinstance(objeto, Reserva_Barco):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["reservas_barcos", self.__cache])  # guarda no cache principal e no disco
