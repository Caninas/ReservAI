from Persistencia.DAOgerente import DAOgerente
from Limite.TelaGerente import TelaGerente

import PySimpleGUI as sg


class ControladorGerente:
    def __init__(self, controlador_sistema, dao_gerente):
        self.__gerente_dao = dao_gerente
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerente = TelaGerente()

    @property
    def gerentes(self):
        return self.__gerente_dao.get_all()

    def verificar_se_nome_existe(self, nome):
        for gerente in self.__gerente_dao.get_all():
            if gerente.nome == nome:
                return True
        return False

    def abre_tela(self):
        lista_opçoes = {}

        while True:
            opçao, valores = self.__tela_gerente.opçoes_menu()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break
            
            print(opçao, valores)
            lista_opçoes[opçao]()
                
            self.__tela_gerente.close_menu()

