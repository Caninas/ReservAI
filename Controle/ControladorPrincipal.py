
#TODO FAZER IMPORTS
        
from Limite.TelaPrincipal import TelaPrincipal

# from Controle.ControladorGerente import ControladorGerente
# from Controle.ControladorFuncionario import ControladorFuncionario
# from Controle.ControladorHospede import ControladorHospede


class ControladorPrincipal:
    def __init__(self):   

        # self.__controlador_gerente = ControladorGerente(self)
        # self.__controlador_funcionario = ControladorFuncionario(self)
        # self.__controlador_hospede = ControladorHospede(self)
        
        self.__tela_principal = TelaPrincipal()

    def iniciar_sistema(self):
        # if gerente existe:
            self.abre_login()
        #else:
            #self.abre_cadastro_gerente()

    def encerrar_sistema(self):
        exit(0)

    def tela_gerente(self):
        self.__controlador_gerente.abre_tela()

    def tela_funcionario(self):
        self.__controlador_funcionario.abre_tela()

    def tela_hospede(self):
        self.__controlador_hospede.abre_tela()


    def abre_cadastro_gerente(self):
        lista_opçoes = {"cadastrar": self.abre_login, 0: self.encerrar_sistema}

        while True:
            opçao = self.__tela_principal.cadastro_gerente()
            print(opçao)
            # validar, criar gerente e abrir login normal
            funçao = lista_opçoes[opçao]()
            self.__tela_principal.close_cadastro_gerente()


    # def abre_login(self):
    #     lista_opçoes = {1: self.tela_gerente, 2: self.tela_hospede, 3: self.tela_funcionario0: self.encerrar_sistema}

    #     while True:
    #         opçao = self.__tela_principal.login()
    #         print(opçao)
    #         funçao = lista_opçoes[opçao]()
    #         self.__tela_principal.close()
