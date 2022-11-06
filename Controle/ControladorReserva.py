from Limite.TelaReserva import TelaReserva
from Entidade.ReservaQuarto import ReservaQuarto
from Entidade.Quarto import Quarto
from Persistencia.DAOquarto import DAOquarto   # temporario para testes
import PySimpleGUI as sg
from datetime import datetime as dt


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

    def alterar_status_res(self, reserva, status):
        pass

    def calcula_passeio(self, reserva):
        passeios = 0
        for reserva_barco in self.__reserva_barco_dao.get_all():
            if reserva_barco.cod_reserva == reserva:
                passeios += 1
        return passeios

    def calcula_diarias(self, reserva):  
        inicio = reserva.data_entrada
        fim = reserva.data_saida
        diarias = (dt.strptime(inicio, "%d/%m/%y") - dt.strptime(fim, "%d/%m/%y")).days
        print(f"A reserva durou {diarias} dias!")

        return diarias

    def calcular_valor(self, reserva):
        valor_diarias = self.calcula_diarias(reserva)*reserva.quarto.valor
        valor_barco = self.calcula_passeio(reserva.cod)
        valor_total = (valor_diarias) + (valor_barco)

        return valor_total
    

    def checar_data_livre(self, n_quarto, valores):
        livre = True
        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto:
                inicio = dt.strptime(reserva.data_entrada, "%d-%m-%y")
                fim = dt.strptime(reserva.data_saida, "%d-%m-%y")

                if inicio <= dt.strptime(valores['data_entrada'], "%d-%m-%y") < fim:
                    livre = False
                    break
                if inicio < dt.strptime(valores['data_saida'], "%d-%m-%y") < fim:
                    livre = False
                    break
                if dt.strptime(valores['data_entrada'], "%d-%m-%y") < inicio <= dt.strptime(valores['data_saida'], "%d-%m-%y"):
                    livre = False
                    break
                if dt.strptime(valores['data_entrada'], "%d-%m-%y") < fim <= dt.strptime(valores['data_saida'], "%d-%m-%y"):
                    livre = False
                    break

        if not livre:
            self.__tela_reserva.msg("Já existe uma reserva no período selecionado")
            return 0

        return 1

    def realizar_reserva(self, n_quarto, dia):
        print(dia)
        retornar = False
        dia = f"{dia.day:02d}-{dia.month:02d}-{dia.year%100}"
        while True:
            opçao, valores = self.__tela_reserva.opçoes_reservar(n_quarto, dia, retornar)
            print(opçao,valores)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_reserva.close_menu_reservar()
                return

            if self.checar_data_livre(n_quarto, valores):
                hospede = self.__controlador_hospede.buscar_hospede(valores["cpf"])

                if not hospede:    # não existe
                    while True:
                        hospede = self.__controlador_hospede.cadastrar()
                            
                        if hospede != None:
                            break

                quarto = self.__quarto_dao.getQuarto(n_quarto)

                cod = self.__reserva_dao.getCodUltimaReserva() + 1
                reserva = ReservaQuarto(cod, 1, quarto, [hospede], "10-07-22",                          # mesmo hospede com endereços de mem diferentes?
                                        valores["data_entrada"], valores["data_saida"])
                self.__reserva_dao.add(reserva)

                self.__tela_reserva.msg("Reserva realizada com sucesso!")
                self.__tela_reserva.close_menu_reservar()

                for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
                    print(i.info_basica())                      
                return 1
            retornar = True

    def editar_reserva(self, n_quarto):
        print("editar")
        pass

    def excluir_reserva(self, n_quarto):
        print("excluir")
        pass

    def getReservadoDia(self, n_quarto, dia):
        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto:
                inicio = reserva.data_entrada
                fim = reserva.data_saida
                if dt.strptime(inicio, "%d-%m-%y").date() <= dia <= dt.strptime(fim, "%d-%m-%y").date():
                    return reserva

        return 0
    
    def getStatusQuartos(self, dia):
        cores = [0 for x in range(0,8)]

        for reserva in self.reservas:
            inicio = reserva.data_entrada
            fim = reserva.data_saida
            if dt.strptime(inicio, "%d-%m-%y").date() <= dia <= dt.strptime(fim, "%d-%m-%y").date():
                if reserva.status == 1:
                    cores[reserva.quarto.numero-1] = "yellow"
                elif reserva.status == 2:
                    cores[reserva.quarto.numero-1] = "red"
        cores = [cor if cor != 0 else "green" for cor in cores]
        print(cores)
        return cores

    def abre_tela(self, botao, dia):                 # clica quarto mapa (recebe numero dele aqui (botao))
        lista_opçoes = {"reservar": self.realizar_reserva, "editar": self.editar_reserva, "excluir": self.excluir_reserva,
                        "check-in": print("self.check-in"), "checkout": print("self.checkout")}
        
        while True:
            for i in self.__reserva_dao.get_all():                              # mesmo quarto com endereços de mem diferentes?
                print(i.quarto.numero, i.data_entrada, i.data_saida)   
            reserva = self.getReservadoDia(botao, dia)

            print(reserva)
            if reserva:              #checkin e checkout aqui
                if dia == dt.today().date():
                    if reserva.status == 1:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_reservado(reserva)
                        self.__tela_reserva.close_menu_reserva_hoje_reservado()
                    elif reserva.status == 2:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_ocupada(reserva)
                        self.__tela_reserva.close_menu_reserva_hoje_ocupado()

                else:
                    if reserva.status == 1:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_outro_reservado(reserva)
                        self.__tela_reserva.close_menu_reserva_outro_reservado()
                    elif reserva.status == 2:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_outro_ocupado(reserva)
                        self.__tela_reserva.close_menu_reserva_outro_ocupado()

            else:
                self.realizar_reserva(botao, dia)
                break

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                break

            if opçao in ["editar", "excluir"]:      # e checkin checkout
                lista_opçoes[opçao](botao)




