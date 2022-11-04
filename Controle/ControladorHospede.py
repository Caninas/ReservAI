from Limite.TelaHospedes import TelaHospedes
from Entidade.Hospede import Hospede

import PySimpleGUI as sg


class ControladorHospede:
    def __init__(self, controlador_sistema, dao_hospede):
        self.__hospede_dao = dao_hospede
        self.__controlador_sistema = controlador_sistema

        self.__tela_hospede = TelaHospedes()

    @property
    def hospedes(self):
        return self.__hospede_dao.get_all()

    def verificar_se_nome_existe(self, cpf):
        for hospede in self.__hospede_dao.get_all():
            if hospede.cpf == cpf:
                return True
        return False

    def buscar_hospede(self, cpf):
        return self.__hospede_dao.getHospede(cpf)

    def cadastrar(self):
        opçao, valores = self.__tela_hospede.opçoes_cadastro()

        if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_hospede.close_cadastro()
            return

        hospede = Hospede(valores["nome"], valores["cpf"], valores["data_nascimento"],
                          valores["telefone"], valores["email"], valores["sexo"], valores["nacionalidade"],
                          valores["rua"], valores["num"], valores["cidade"], valores["estado"], valores["pais"])
        self.__hospede_dao.add(hospede)

        self.__tela_hospede.msg("Hóspede Cadastrado")
        self.__tela_hospede.close_cadastro()

        return hospede

    def alterar_hospede(self):
        opçao, valores = self.__tela_hospede.buscar_hospede()

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_hospede.close_busca()
            return

        hospede = self.buscar_hospede(valores["cpf"])
        self.__tela_hospede.close_busca()

        if hospede == 0:
            self.__tela_hospede.msg("Hóspede não encontrado!")
            return

        opçao, valores = self.__tela_hospede.alt_hospede(hospede)

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_hospede.close_alt_hospede()
            return

        hospede.atualizar(valores)
        self.__hospede_dao.atualizar()

        self.__tela_hospede.msg("Hospede alterado com sucesso")
        self.__tela_hospede.close_alt_hospede()

    def excluir_hospede(self):
        opçao, valores = self.__tela_hospede.buscar_hospede()

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_hospede.close_busca()
            return

        hospede = self.buscar_hospede(valores["cpf"])
        self.__tela_hospede.close_busca()

        if hospede == 0:
            self.__tela_hospede.msg("Hóspede não encontrado!")
            return

        opçao, valores = self.__tela_hospede.excluir_hospede(hospede)

        if opçao == 0 or opçao == sg.WIN_CLOSED:
            self.__tela_hospede.close_excluir_hospede()
            return

        self.__hospede_dao.remove(hospede)
        self.__tela_hospede.msg("Hospede excluído com sucesso")
        self.__tela_hospede.close_excluir_hospede()

    def abre_tela(self):
        lista_opçoes = {"cadastrar_hospede": self.cadastrar, "alterar_hospede": self.alterar_hospede,
                        "excluir_hospede": self.excluir_hospede}

        while True:
            opçao, valores = self.__tela_hospede.opçoes_menu()

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_hospede.close_menu()
                break

            self.__tela_hospede.close_menu()

            lista_opçoes[opçao]()
