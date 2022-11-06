from Persistencia.DAOgerente import DAOgerente
from Limite.TelaGerente import TelaGerente

import PySimpleGUI as sg
from datetime import datetime as dt

class ControladorGerente:
    def __init__(self, controlador_sistema, controlador_hospede, controlador_reserva, dao_gerente, dao_funcionario, cript):
        self.__gerente_dao = dao_gerente
        self.__controlador_sistema = controlador_sistema
        self.__controlador_hospede = controlador_hospede
        self.__controlador_reserva = controlador_reserva
        self.__fernet = cript

        data = dt.today()
        self.__dia_selecionado = f"{data.day:02d}-{data.month:02d}-{data.year%100}"#dt.strftime("03-11-22", "%d-%m-%y")
        print(self.__dia_selecionado)
        #dt.strptime(f"{dt.today().day}-{dt.today().month}-{str(dt.today().year)}", "%d-%m-%Y")

        self.__funcionarios_dao = dao_funcionario
        self.__tela_gerente = TelaGerente()

    @property
    def gerentes(self):
        return self.__gerente_dao.get_all()

    def verificar_se_nome_existe(self, nome):
        for gerente in self.__gerente_dao.get_all():
            if gerente.nome == nome:
                return True
        return False

    def buscar_funcionario(self, cpf):
        return self.__funcionarios_dao.getFuncionarioCPF(cpf)

    def menu_funcionario(self):
        lista_opçoes = {"cadastrar_funcionario": self.cadastrar_funcionario,
                        "alterar_funcionario": self.alterar_funcionario, "excluir_funcionario": self.excluir_funcionario}

        while True:
            opçao, valores = self.__tela_gerente.opçoes_funcionario()

            if opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_opçoes_funcionario()
                return

            self.__tela_gerente.close_opçoes_funcionario()

            lista_opçoes[opçao]()

    def cadastrar_funcionario(self):
        while True:
            opçao, valores = self.__tela_gerente.cadastrar_funcionario()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_cadastrar_funcionario()
                return

            if self.buscar_funcionario(valores["cpf"]) != 0:
                self.__tela_gerente.msg("cpf já existente")
            elif self.__funcionarios_dao.getFuncionario(valores["usuario"]) != 0 or self.__gerente_dao.getGerente(valores["usuario"]) != 0:
                self.__tela_gerente.msg("usuário já existente")

            else:
                self.__controlador_sistema.controlador_funcionario.cadastrar(
                    valores)
                self.__tela_gerente.msg("Funcionário Cadastrado")
                print(self.__funcionarios_dao.get_all())
                
            self.__tela_gerente.close_cadastrar_funcionario()
            return

    def alterar_funcionario(self):
        opçao, valores = self.__tela_gerente.buscar_funcionario()

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_gerente.close_busca_funcionarios()
            return

        funcionario = self.buscar_funcionario(valores["cpf"])
        self.__tela_gerente.close_busca_funcionarios()

        if funcionario == 0:
            self.__tela_gerente.msg("Funcionário não encontrado!")
            return

        senha = self.__fernet.decrypt(funcionario.senha).decode()
        opçao, valores = self.__tela_gerente.alterar_funcionario(
            funcionario, senha)

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_gerente.close_alterar_funcionario()
            return

        valores["senha"] = self.__fernet.encrypt(valores["senha"].encode())

        funcionario.atualizar(valores)
        self.__funcionarios_dao.atualizar()

        self.__tela_gerente.msg("Funcionário alterado com sucesso")
        self.__tela_gerente.close_alterar_funcionario()

    def excluir_funcionario(self):
        opçao, valores = self.__tela_gerente.buscar_funcionario()

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_gerente.close_busca_funcionarios()
            return

        funcionario = self.buscar_funcionario(valores["cpf"])
        self.__tela_gerente.close_busca_funcionarios()

        if funcionario == 0:
            self.__tela_gerente.msg("Funcionário não encontrado!")
            return

        opçao, valores = self.__tela_gerente.excluir_funcionario(
            funcionario.nome)

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_gerente.close_excluir_funcionario()
            return

        self.__funcionarios_dao.remove(funcionario)
        self.__tela_gerente.msg("Funcionário excluído com sucesso")
        self.__tela_gerente.close_excluir_funcionario()

    def abre_tela(self):
        
        lista_opçoes = {"menu_funcionario": self.menu_funcionario,
                        "menu_hospede": self.__controlador_hospede.abre_tela, "reservar": self.__controlador_reserva.abre_tela}

        while True:
            print(self.__dia_selecionado)
            opçao, valores = self.__tela_gerente.opçoes_menu(self.__dia_selecionado)
            # funçao mudar dia e atualizar na tela!

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break

            self.__tela_gerente.close_menu()

            if opçao == "deslogar":
                break

            lista_opçoes["reservar"](opçao, self.__dia_selecionado)
