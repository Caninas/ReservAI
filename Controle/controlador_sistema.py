
#TODO FAZER IMPORTS
from Limite.tela_sistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        #TODO IMPORTAR TELAS E CONTROLADORES

    def inicializa_sistema(self):
        self.__tela_sistema.mostra_mensagem("BEM VINDO AO RESERVAI")