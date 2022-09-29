
#TODO FAZER IMPORTS
from Limite.TelaPrincipal import TelaPrincipal

class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        #TODO IMPORTAR TELAS E CONTROLADORES

    def inicializa_sistema(self):
        self.__tela_principal.mostra_mensagem("BEM VINDO AO RESERVAI")