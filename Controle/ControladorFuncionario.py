from Limite.TelaFuncionario import TelaFuncionario
from Entidade.Funcionario import Funcionario

import PySimpleGUI as sg
from datetime import datetime as dt
from datetime import timedelta

class ControladorFuncionario:
    def __init__(self, controlador_sistema, controlador_hospede, controlador_reserva, dao_funcionario, cript, controlador_barco, controlador_relatorio):
        self.__funcionario_dao = dao_funcionario
        self.__controlador_sistema = controlador_sistema
        self.__fernet = cript

        self.__dia_selecionado = dt.today().date()

        self.__controlador_hospede = controlador_hospede
        self.__controlador_reserva = controlador_reserva
        self.__controlador_barco = controlador_barco
        self.__controlador_relatorio = controlador_relatorio
        self.__tela_funcionario = TelaFuncionario()

    @property
    def funcionarios(self):
        return self.__funcionario_dao.get_all()

    def verificar_se_nome_existe(self, nome):
        for funcionario in self.__funcionario_dao.get_all():
            if funcionario.nome == nome:
                return True
        return False

    def cadastrar(self, valores):
        senha = self.__fernet.encrypt(valores['senha'].encode())
        funcionario = Funcionario(valores["nome"], valores["usuario"], senha, valores["cpf"],
                                  valores["data_nascimento"], valores["telefone"], valores["email"])
        self.__funcionario_dao.add(funcionario)
        print("adicionado")
    
    def abre_tela(self):
        lista_opçoes = {"menu_hospede": self.__controlador_hospede.abre_tela, "reservar": self.__controlador_reserva.abre_tela,
                        "listar_reservas": self.__controlador_reserva.listar_reservas,
                        "menu_barco": self.__controlador_barco.abre_tela,
                        "relatorio": self.__controlador_relatorio.abre_tela}
        
        dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100} (hoje)"
        refresh = False

        cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)

        while True:
            print(self.__dia_selecionado)
            
            opçao, valores = self.__tela_funcionario.opçoes_menu(dia, cores_quartos, refresh)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_funcionario.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break

            if opçao == "deslogar":
                self.__tela_funcionario.close_menu()
                break

            if opçao == "sd":
                self.__dia_selecionado = self.__dia_selecionado + timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"

                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_funcionario.window_menu['data'].update(dia)

                cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
                for i in range(len(cores_quartos)):
                    self.__tela_funcionario.window_menu[f'c{i+1}'].update(background_color=cores_quartos[i])

                refresh = True
                continue

            elif opçao == "se":
                self.__dia_selecionado = self.__dia_selecionado - timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"

                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_funcionario.window_menu['data'].update(dia)

                cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
                for i in range(len(cores_quartos)):
                    self.__tela_funcionario.window_menu[f'c{i+1}'].update(background_color=cores_quartos[i])

                refresh = True
                continue

            self.__tela_funcionario.close_menu()

            if opçao == "menu_hospede" or opçao == "menu_barco" or opçao == "relatorio":
                lista_opçoes[opçao]()
            elif opçao == "listar_reservas":
                lista_opçoes[opçao](self.__dia_selecionado)
            else:
                lista_opçoes["reservar"](opçao, self.__dia_selecionado)
                cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
            refresh = False


