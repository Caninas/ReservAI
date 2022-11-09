from Persistencia.DAObarco import DAObarco
from Persistencia.DAOreserva_barco import DAOreserva_barco
from Persistencia.DAOreserva import DAOreserva
from Limite.TelaBarco import TelaBarco
from Entidade.Reserva_Barco import Reserva_Barco
from Entidade.Barco import Barco
import PySimpleGUI as sg
from Entidade.Quarto import Quarto
from datetime import datetime as dt
from datetime import timedelta


class ControladorQuarto:
    def __init__(self, controlador_sistema, dao_quarto):
        self.__controlador_sistema = controlador_sistema

        self.__quarto_dao = dao_quarto
        
        self.criar_quartos()

    @property
    def quartos(self):
        return self.__quartos

    def getQuarto(self, n_quarto):
        return self.__quarto_dao.getQuarto(n_quarto)

    def criar_quartos(self):                                                 # temporario para teste
        if self.__quarto_dao.cache["quartos"] == []:                                
            for i in range(1,5):
                quarto = Quarto(i, 2, 1, 0, 500, "Quarto Casal (2 lugares)", 0)
                self.__quarto_dao.add(quarto)
            for i in range(5,9):
                quarto = Quarto(i, 4, 1, 2, 1000, "Quarto Familia (4 lugares)", 0)
                self.__quarto_dao.add(quarto)

    