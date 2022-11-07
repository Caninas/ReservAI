from Persistencia.DAOgerente import DAOgerente
from Limite.TelaGerente import TelaGerente

import PySimpleGUI as sg
from datetime import datetime as dt
from datetime import timedelta


class ControladorGerente:
    def __init__(self, controlador_sistema, controlador_hospede, controlador_reserva, dao_gerente, dao_funcionario, cript):
        self.__gerente_dao = dao_gerente
        self.__controlador_sistema = controlador_sistema
        self.__controlador_hospede = controlador_hospede
        self.__controlador_reserva = controlador_reserva
        self.__fernet = cript

        self.__dia_selecionado = dt.today().date()

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
                        "menu_hospede": self.__controlador_hospede.abre_tela, 
                        "reservar": self.__controlador_reserva.abre_tela,
                        "listar_reservas": self.__controlador_reserva.listar_reservas}

        dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100} (hoje)"
        refresh = False

        cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
        
        while True:
            print(self.__dia_selecionado)

            opçao, valores = self.__tela_gerente.opçoes_menu(dia, cores_quartos, refresh)

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_gerente.close_menu()
                self.__controlador_sistema.encerrar_sistema()
                break


            if opçao == "deslogar":
                self.__tela_gerente.close_menu()
                break
            
            if opçao == "sd":
                self.__dia_selecionado = self.__dia_selecionado + timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"
                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_gerente.window_menu['data'].update(dia)

                cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
                for i in range(len(cores_quartos)):
                    self.__tela_gerente.window_menu[f'c{i+1}'].update(background_color=cores_quartos[i])

                refresh = True
                continue
            elif opçao == "se":
                self.__dia_selecionado = self.__dia_selecionado - timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"
                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_gerente.window_menu['data'].update(dia)

                cores_quartos = self.__controlador_reserva.getStatusQuartos(self.__dia_selecionado)
                for i in range(len(cores_quartos)):
                    self.__tela_gerente.window_menu[f'c{i+1}'].update(background_color=cores_quartos[i])

                refresh = True
                continue

            if opçao == "menu_hospede" or opçao == "menu_funcionario":
                self.__tela_gerente.close_menu()
                lista_opçoes[opçao]()
            elif opçao == "listar_reservas":
                self.__tela_gerente.close_menu()
                lista_opçoes[opçao](self.__dia_selecionado)
            else:
                self.__tela_gerente.close_menu()
                lista_opçoes["reservar"](opçao, self.__dia_selecionado)
            refresh = False
