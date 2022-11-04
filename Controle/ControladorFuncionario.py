from Limite.TelaFuncionario import TelaFuncionario
from Entidade.Funcionario import Funcionario

import PySimpleGUI as sg


class ControladorFuncionario:
    def __init__(self, controlador_sistema, controlador_hospede, controlador_reserva, dao_funcionario, cript):
        self.__funcionario_dao = dao_funcionario
        self.__controlador_sistema = controlador_sistema
        self.__fernet = cript

        self.__controlador_hospede = controlador_hospede
        self.__controlador_reserva = controlador_reserva
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
        lista_opçoes = {"menu_hospede": self.__controlador_hospede.abre_tela, "reservar": self.__controlador_reserva.abre_tela}

        while True:
            opçao, valores = self.__tela_funcionario.opçoes_menu()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_funcionario.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break

            self.__tela_funcionario.close_menu()

            if opçao == "deslogar":
                break

            lista_opçoes[opçao]()
