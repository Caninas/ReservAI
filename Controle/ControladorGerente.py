from Persistencia.DAOgerente import DAOgerente
from Limite.TelaGerente import TelaGerente

import PySimpleGUI as sg


class ControladorGerente:
    def __init__(self, controlador_sistema, dao_gerente, f):
        self.__gerente_dao = dao_gerente
        self.__controlador_sistema = controlador_sistema
        self.__funcionarios_dao = f
        self.__tela_gerente = TelaGerente()

    @property
    def gerentes(self):
        return self.__gerente_dao.get_all()

    def verificar_se_nome_existe(self, nome):
        for gerente in self.__gerente_dao.get_all():
            if gerente.nome == nome:
                return True
        return False

    def cadastrar_funcionario(self):
        lista_opçoes = {}

        opçao, valores = self.__tela_gerente.cadastrar_func()
        print(opçao,valores)
        if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_gerente.close_cadastro_func()
            return
        
        print(opçao, valores)
        
        self.__controlador_sistema.controlador_funcionario.cadastrar(valores)

        self.__tela_gerente.msg("Funcionário Cadastrado")
        print(self.__funcionarios_dao.get_all())
        
        self.__tela_gerente.close_cadastro_func()

    def abre_tela(self):
        lista_opçoes = {"cadastrar_func": self.cadastrar_funcionario}

        while True:
            opçao, valores = self.__tela_gerente.opçoes_menu()
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break
            
            self.__tela_gerente.close_menu()

            print(opçao, valores)
            if opçao == "deslogar":
                break

            lista_opçoes[opçao]()