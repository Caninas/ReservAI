from Persistencia.DAObarco import DAObraco
from Persistencia.DAOreserva_barco import DAOreserva_barco
from Persistencia.DAOreserva import DAOreserva
from Limite.TelaBarco import TelaBarco
from Entidade.Reserva_Barco import Reserva_Barco
from Entidade.Barco import Barco
import PySimpleGUI as sg
import datetime


class ControladorBarco:
    def __init__(self, controlador_sistema, dao_reserva, dao_barco, dao_reservabarco):
        self.__controlador_sistema = controlador_sistema
        self.__dao_reserva = dao_reserva
        self.__dao_barco = dao_barco
        self.__dao_reservabarco = dao_reservabarco
        self.__tela_barco = TelaBarco()
        self.criar_barcos()

    @property
    def barcos(self):
        return self.__dao_barco.get_all()

    @property
    def reservas_barcos(self):
        return self.__dao_reservabarco.get_all()
    
    def criar_barcos(self):                               
        #if self.__dao_barco.get_all == []:
        barco = Barco('barco de luxo', 1, 120)
        self.__dao_barco.add(barco)
        barco = Barco('barco normal', 2, 70)
        self.__dao_barco.add(barco)
        barco = Barco('barco humilde', 3, 50)
        self.__dao_barco.add(barco)
    
    def abre_tela(self):
        lista_opçoes = {1: self.realizar_reservabarco}
        while True:
            opçao, valores = self.__tela_barco.opçoes_reserva()
            print(opçao,valores)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                 self.__tela_barco.close_menu_reserva()
                 break
            if opçao == 1:
                o = lista_opçoes[opçao](valores)

                if o == 1:
                    break
    
    def realizar_reservabarco(self, valores):
        reserva = self.__dao_reserva.getReservaCod(valores["n_reserva"])
        if reserva:    # existe
            self.__tela_barco.close_menu_reserva()
        else:     # nao existe
            self.__tela_barco.msg("reserva não existente")
            self.__tela_barco.close_menu_reserva()

        barco = self.__dao_barco.getBarco(int(valores["n_barco"]))

        cod = self.__dao_reservabarco.getCodUltimaReservaBarco() + 1
        reserva_barco = Reserva_Barco(barco, cod, reserva.cod,                      
                                valores["data_entrada"], barco.valor)
        self.__dao_reserva.remove(reserva)
        self.__dao_reservabarco.add(reserva_barco)
        reserva.add_reserva_barco(reserva_barco)
        self.__dao_reserva.add(reserva)
        print (reserva.info_basica())

        self.__tela_barco.msg("Reserva criada com sucesso!")
        self.__tela_barco.close_menu_reserva()

        for i in self.__dao_reservabarco.get_all():
            print(i.info_basica())                      
        return 1
