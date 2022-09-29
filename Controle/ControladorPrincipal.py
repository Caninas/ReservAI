
#TODO FAZER IMPORTS
        
from Limite.TelaPrincipal import TelaPrincipal

from Controle.ControladorGerente import ControladorGerente
from Controle.ControladorFuncionario import ControladorFuncionario
from Controle.ControladorHospede import ControladorHospede


class ControladorPrincipal:
    def __init__(self):   

        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_hospede = ControladorHospede(self)
        
        self.__tela_principal = TelaPrincipal()

    def iniciar_sistema(self):
        self.__tela_principal.mostra_mensagem("BEM VINDO AO RESERVAI")


    def encerrar_sistema(self):
        exit(0)

    def tela_gerente(self):
        self.__controlador_gerente.abre_tela()

    def tela_funcionario(self):
        self.__controlador_funcionario.abre_tela()

    def tela_hospede(self):
        self.__controlador_hospede.abre_tela()

    # def abre_tela(self):
        # lista_opçoes = {1: self.tela_funcionario, 2: self.tela_hospede, 0: self.encerrar_sistema}

        # while True:
        #     opçao = self.__tela_principal.opcoes()
        #     funçao = lista_opçoes[opçao]
        #     self.__tela_principal.close()
        #     funçao()
