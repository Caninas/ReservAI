
#TODO FAZER IMPORTS


from cryptography.fernet import Fernet
from Limite.TelaPrincipal import TelaPrincipal

# from Controle.ControladorGerente import ControladorGerente
# from Controle.ControladorFuncionario import ControladorFuncionario
# from Controle.ControladorHospede import ControladorHospede

from Persistencia.DAOgerente import DAOgerente
#from Persistencia.DAOfuncionario.py import DAOfuncionario
from Persistencia.DataSource import DataSource

class ControladorPrincipal:
    def __init__(self):
        self.__fernet = Fernet(b'DqaysoWHxzFAoi4ZUM5GeMYZitArP5lBiGOUEooEgwk=')
        # self.__controlador_gerente = ControladorGerente(self)
        # self.__controlador_funcionario = ControladorFuncionario(self)
        # self.__controlador_hospede = ControladorHospede(self)
        self.__usuario_logado = None
        self.__privilegio = None

        self.__dataSource = DataSource()
        self.__DAOgerente = DAOgerente(self.__dataSource, self.__fernet)
        
        self.__tela_principal = TelaPrincipal()

    def iniciar_sistema(self):
        #if exite_gerente:
            self.abre_login()
        #else:
          #  self.abre_cadastro_gerente()

    def encerrar_sistema(self, *args):
        exit(0)


    # def tela_funcionario(self):
    #     self.__controlador_funcionario.abre_tela()

    # def tela_hospede(self):
    #     self.__controlador_hospede.abre_tela()


    def validar_usuario(self, valores):
        print("validando usuario")
        gerente = self.__DAOgerente.getGerente(valores["usuario"])
        funcionario = 0#self.__DAOfuncionario.getFuncionario(valores["usuario"])
        
        if gerente != 0:
            self.__usuario_logado = gerente
            self.__privilegio = 1
            print("usuario:", gerente.usuario)
        else:
            if funcionario != 0:
                self.__usuario_logado = funcionario
                self.__privilegio = 0
            else:
                print("nao achou usuario")
                return 0

        return self.validar_senha(gerente.senha, valores["senha"])
        
    def validar_senha(self, senha_og, senha_input):
        if self.__fernet.decrypt(senha_og).decode() == senha_input:
            print("senha correta")
            return 1
        else:
            print("senha errada")
            return 0


    def abrir_menu(self):
        if self.__privilegio:
            self.__controlador_gerente.abre_tela()  # TelaMenu
        else:
            self.__controlador_funcionario.abre_tela()

    def abre_login(self):
        lista_opçoes = {"entrar": self.abrir_menu, 0: self.encerrar_sistema}

        while True:
            opçao, valores = self.__tela_principal.opcoes_login()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_principal.close_login()
                self.encerrar_sistema()
                break
            
            print(opçao, valores)
            if self.validar_usuario(valores) == 0:
                print("ERROR: USUARIO OU SENHA ERRADOS")
                #self.__tela_principal.error()
            else:                    
                self.__tela_principal.msg("USUARIO ENTROU")
                lista_opçoes[opçao]()
                
            self.__tela_principal.close_login()

