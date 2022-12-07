from Entidade.ReservaQuarto import ReservaQuarto


class DAOreserva:
    def __init__(self, dataSource):
        self.__main = dataSource
        self.__cache = []

        self.abrir("reservas")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def atualizar(self):
        self.__main.guardar(["reservas", self.__cache])

    def getCodUltimaReserva(self):
        maior_cod = 0
        for reserva in self.__cache:
            if reserva.cod > maior_cod:
                maior_cod = reserva.cod
        
        return maior_cod

    def getReservaCod(self, cod):          # CPF?
        objReserva = 0
        for reserva in self.__cache:
            if reserva.cod == int(cod):
                objReserva = reserva

        return objReserva

    def getReserva(self, cpf):          # CPF?
        objReserva = []
        for reserva in self.__cache:
            if reserva.lista_hospedes[0].cpf == int(cpf):
                objReserva.append(reserva)

        return objReserva
    
    def getReservaparabarco(self, cpf, data_barco):
        objReserva = 0
        for reserva in self.__cache:
            if reserva.lista_hospedes[0].cpf == int(cpf) and data_barco < reserva.data_saida and reserva.data_entrada >= data_barco and reserva.status == 2:
                objReserva = reserva
        
        return objReserva

    def add(self, objeto: ReservaQuarto):
        if objeto != None and isinstance(objeto, ReservaQuarto):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["reservas", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: ReservaQuarto):
        if objeto != None and isinstance(objeto, ReservaQuarto):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["reservas", self.__cache])  # guarda no cache principal e no disco
