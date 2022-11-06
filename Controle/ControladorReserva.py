from Limite.TelaReserva import TelaReserva
from Entidade.ReservaQuarto import ReservaQuarto
from Entidade.Quarto import Quarto
from Persistencia.DAOquarto import DAOquarto   # temporario para testes
import PySimpleGUI as sg


class ControladorReserva:
    def __init__(self, controlador_sistema, controlador_hospede, dao_reserva):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_hospede = controlador_hospede

        self.__reserva_dao = dao_reserva
        self.__quarto_dao = DAOquarto()      # temporario para testes
        self.__tela_reserva = TelaReserva()
        self.criar_quartos()

    @property
    def reservas(self):
        return self.__reserva_dao.get_all()

    def criar_quartos(self):                                                        # temporario para teste
        if self.__quarto_dao.cache["quartos"] == []:                                
            for i in range(1,5):
                quarto = Quarto(i, 2, 1, 0, 500, "Quarto Casal (2 lugares)", 0)
                self.__quarto_dao.add(quarto)
            for i in range(5,9):
                quarto = Quarto(i, 4, 1, 2, 1000, "Quarto Familia (4 lugares)", 0)
                self.__quarto_dao.add(quarto)

    #def checar_data_livre(self):
        # loop reservas / datas, data livre?

        # if data livre break / else voltar tela com preenchimento para alterar

    def realizar_reserva(self, valores):
        # if self.checar_data_livre:
        hospede = self.__controlador_hospede.buscar_hospede(valores["cpf"])
        if hospede:    # existe
            self.__tela_reserva.close_menu_reserva()
        else:     # nao existe
            hospede = self.__controlador_hospede.cadastrar()

        quarto = self.__quarto_dao.getQuarto(int(valores["n_quarto"]))

        cod = self.__reserva_dao.getCodUltimaReserva() + 1
        reserva = ReservaQuarto(cod, 1, quarto, [hospede], "10/07/22",                          # mesmo hospede com endereços de mem diferentes?
                                valores["data_entrada"], valores["data_saida"])
        self.__reserva_dao.add(reserva)

        self.__tela_reserva.msg("Reserva criada com sucesso!")
        self.__tela_reserva.close_menu_reserva()

        for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
            print(i.info_basica())                      
        return 1

    # def realizar_checkin(self, valores):
    #     # if self.checar_data_livre:
    #     #todo pegar cpfs
    #     #todo pegar numero do quarto e reserva
    #     hospedes = []
    #     if hospedes
    #     hospedes.append(self.__controlador_hospede.buscar_hospede(valores["cpf1"]))
    #     hospedes.append(self.__controlador_hospede.buscar_hospede(valores["cpf2"]))
    #     if quarto.tipo == 'familia':
    #         hospedes.append(self.__controlador_hospede.buscar_hospede(valores["cpf3"]))
    #         hospedes.append(self.__controlador_hospede.buscar_hospede(valores["cpf4"]))
    #     hospedes = [x for x in hospedes if x and x != None]
    #     hospede_principal = self.__controlador_hospede.buscar_hospede(valores["cpf"])
    #     if hospede_principal:    # existe
    #         self.__tela_reserva.close_menu_reserva()
    #     else:     # nao existe
    #         hospede = self.__controlador_hospede.cadastrar()
    #
    #     quarto = self.__quarto_dao.getQuarto(int(valores["n_quarto"]))
    #
    #     cod = self.__reserva_dao.getCodUltimaReserva() + 1
    #     reserva = ReservaQuarto(cod, 1, quarto, [hospede], "10/07/22",                          # mesmo hospede com endereços de mem diferentes?
    #                             valores["data_entrada"], valores["data_saida"])
    #     self.__reserva_dao.add(reserva)
    #
    #     self.__tela_reserva.msg("Reserva criada com sucesso!")
    #     self.__tela_reserva.close_menu_reserva()
    #
    #     for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
    #         print(i.info_basica())
    #     return 1

    def abre_tela(self):                            # clica quarto mapa (recebe numero dele aqui)
        lista_opçoes = {1: self.realizar_reserva}
        while True:
            opçao, valores = self.__tela_reserva.opçoes_reserva()
            print(opçao,valores)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                 self.__tela_reserva.close_menu_reserva()
                 break
            if opçao == 1:
                o = lista_opçoes[opçao](valores)

                if o == 1:
                    break
