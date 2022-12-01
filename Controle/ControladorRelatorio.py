from Limite.TelaRelatorio import TelaRelatorio
from datetime import datetime as dt

import PySimpleGUI as sg


class ControladorRelatorio:
    def __init__(self, controlador_sistema, controlador_reserva, controlador_hospede, controlador_barco):
        self.__controlador_sistema = controlador_sistema

        self.__controlador_reserva = controlador_reserva
        self.__controlador_hospede = controlador_hospede
        self.__controlador_barco = controlador_barco

        self.__tela_relatorio = TelaRelatorio()

    def relatorioReservas(self):        # teste
        dados = None
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu_rel_reservas()
            
            print(opçao, valores)
            self.__tela_relatorio.close_menu_rel_reservas()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                break

            reservas = self.__controlador_reserva.reservas

            dados = [len(reservas)]


    def abre_tela(self):                 # clica quarto mapa (recebe numero dele aqui (botao) e dia selecionado)
        lista_opçoes = {"rel_reservas": self.relatorioReservas, "rel_hospedes": print,
                        "rel_passeios": print}
        
        while True:
            opçao, valores = self.__tela_relatorio.opçoes_menu()
            print(opçao, valores)
            self.__tela_relatorio.close_menu()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                break 

            lista_opçoes[opçao]()


                




