
#TODO FAZER IMPORTS
import PySimpleGUI as sg

from cryptography.fernet import Fernet

from Limite.TelaPrincipal import TelaPrincipal

from Entidade.Gerente import Gerente

from Controle.ControladorGerente import ControladorGerente
from Controle.ControladorFuncionario import ControladorFuncionario
from Controle.ControladorHospede import ControladorHospede

from Persistencia.DAOgerente import DAOgerente
from Persistencia.DAOfuncionario import DAOfuncionario
from Persistencia.DAOhospede import DAOhospede
from Persistencia.DataSource import DataSource

class ControladorPrincipal:
    def __init__(self):
        self.__fernet = Fernet(b'DqaysoWHxzFAoi4ZUM5GeMYZitArP5lBiGOUEooEgwk=')

        self.__usuario_logado = None
        self.__privilegio = None

        self.__dataSource = DataSource()
        self.__DAOgerente = DAOgerente(self.__dataSource, self.__fernet)
        self.__DAOhospede = DAOhospede(self.__dataSource)
        self.__DAOfuncionario = DAOfuncionario(self.__dataSource, self.__fernet)
        
        self.__controlador_hospede = ControladorHospede(self, self.__DAOhospede)
        self.__controlador_gerente = ControladorGerente(self, self.__controlador_hospede, self.__DAOgerente, self.__DAOfuncionario)
        self.__controlador_funcionario = ControladorFuncionario(self, self.__controlador_hospede, self.__DAOfuncionario, self.__fernet)
        
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    def iniciar_sistema(self):
        if len(self.__DAOgerente.get_all()) > 0:
            self.abre_login()
        else:
            if self.abre_cadastro_gerente_primeira_vez():
                self.abre_login()

    def encerrar_sistema(self, *args):
        exit(0)

    def abre_cadastro_gerente_primeira_vez(self):

        dados_gerente = self.__tela_principal.cadastro_gerente_primeira_vez()

        if dados_gerente == None:
            return None

        senha_crip = self.__fernet.encrypt( dados_gerente['senha'].encode())
        gerente = Gerente(dados_gerente["nome"], dados_gerente["usuario"], senha_crip)
        self.__DAOgerente.add(gerente)
        return True


    def abre_cadastro_gerente(self):
        lista_opçoes = {"cadastrar": "a", 0: self.encerrar_sistema}

        while True:
            opçao = self.__tela_principal.cadastro_gerente()
            print(opçao)
            # validar, criar gerente e abrir login normal
            funçao = lista_opçoes[opçao]()
            self.__tela_principal.cadastro_gerente()

    # def tela_funcionario(self):
    #     self.__controlador_funcionario.abre_tela()

    # def tela_hospede(self):
    #     self.__controlador_hospede.abre_tela()


    def validar_usuario(self, valores):
        print("validando usuario")
        gerente = self.__DAOgerente.getGerente(valores["usuario"])
        funcionario = self.__DAOfuncionario.getFuncionario(valores["usuario"])
        
        if gerente != 0:
            self.__usuario_logado = gerente
            self.__privilegio = 1
            senha = gerente.senha
            print("usuario:", gerente.usuario)
        else:
            if funcionario != 0:
                self.__usuario_logado = funcionario
                self.__privilegio = 0
                senha = funcionario.senha
                print("usuario:", funcionario.usuario)
            else:
                print("nao achou usuario")
                return 0

        return self.validar_senha(senha, valores["senha"])
        
    def validar_senha(self, senha_og, senha_input):
        if self.__fernet.decrypt(senha_og).decode() == senha_input:
            print("senha correta")
            return 1
        else:
            print("senha errada")
            return 0


    def abrir_menu(self):
        if self.__privilegio:
            self.__controlador_gerente.abre_tela()  # TelaGerente
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
                self.__tela_principal.msg("ERROR: USUARIO OU SENHA ERRADOS")
            else:
                self.__tela_principal.close_login()
                lista_opçoes[opçao]()
                

