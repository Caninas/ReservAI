from Limite.TelaReserva import TelaReserva
from Entidade.ReservaQuarto import ReservaQuarto
from Entidade.Quarto import Quarto
from Persistencia.DAOquarto import DAOquarto   # temporario para testes
from Persistencia.DAOreserva_barco import DAOreserva_barco
from datetime import datetime as dt

import PySimpleGUI as sg


class ControladorReserva:
    def __init__(self, controlador_sistema, controlador_hospede, dao_reserva, dao_reserva_barco):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_hospede = controlador_hospede

        self.__reserva_dao = dao_reserva
        self.__quarto_dao = DAOquarto()      # temporario para testes
        self.__tela_reserva = TelaReserva()
        self.__reserva_barco_dao = dao_reserva_barco
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

    def calcula_passeio(self, reserva):
        passeios = 0
        for reserva_barco in self.__reserva_barco_dao.get_all():
            if reserva_barco.cod_reserva == reserva.cod:
                passeios += reserva_barco.valor
                print(reserva_barco.valor)
        return passeios

    def cancela_passeios(self, reserva):
        for reserva_barco in self.__reserva_barco_dao.get_all():
            if reserva_barco.cod_reserva == reserva.cod:
                if dt.strptime(reserva_barco.data_reserva, "%d-%m-%y").date() > dt.today().date():
                    reserva_barco.status = 0
                    self.__reserva_barco_dao.remove(reserva_barco)
                    print("apaguei", reserva_barco)

    def calcula_diarias(self, reserva):  
        inicio = reserva.data_entrada
        fim = reserva.data_saida
        diarias = (dt.strptime(fim, "%d-%m-%y") - dt.strptime(inicio, "%d-%m-%y")).days
        print(f"A reserva durou {diarias} dias!")

        return diarias

    def calcular_valor(self, reserva):
        valor_diarias = self.calcula_diarias(reserva)*reserva.quarto.valor
        valor_barco = self.calcula_passeio(reserva)
        valor_total = (valor_diarias) + (valor_barco)

        return valor_total
    
    def checkout(self, reserva):
        self.cancela_passeios(reserva)
        valor = self.calcular_valor(reserva)
        opçao, valores = self.__tela_reserva.menu_check_out(reserva, valor)
        if opçao == "check-out":
            reserva.status = 0
            self.__tela_reserva.msg("Check-out realizado com sucesso!")
            self.__tela_reserva.close_menu_check_out()
            opçao = 0
            self.__reserva_dao.atualizar()
            return 1
            

    def checar_data_livre(self, n_quarto, valores):
        livre = True
        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto and reserva.status != 0:
                inicio = dt.strptime(reserva.data_entrada, "%d-%m-%y").date()
                fim = dt.strptime(reserva.data_saida, "%d-%m-%y").date()

                if inicio <= dt.strptime(valores['data_entrada'], "%d-%m-%y").date() < fim:
                    livre = False
                    break
                if inicio < dt.strptime(valores['data_saida'], "%d-%m-%y").date() < fim:
                    livre = False
                    break
                if dt.strptime(valores['data_entrada'], "%d-%m-%y").date() < inicio <= dt.strptime(valores['data_saida'], "%d-%m-%y").date():
                    livre = False
                    break
                if dt.strptime(valores['data_entrada'], "%d-%m-%y").date() < fim <= dt.strptime(valores['data_saida'], "%d-%m-%y").date():
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
                    hospede = self.__controlador_hospede.cadastrar()

                    if hospede == None:
                        return

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


    def finalizar_check_in(self, reserva, hospedes):
        for hospede in hospedes:
            if hospede not in reserva.lista_hospedes:
                reserva.lista_hospedes.append(hospede)
        reserva.status = 2
        self.__reserva_dao.atualizar()


    def check_in(self, reserva):
        hospedes = [reserva.lista_hospedes[0]]
        while True:
            opçao, valores = self.__tela_reserva.menu_check_in(reserva, hospedes)
            if opçao == "add_hospede":
                hospede = self.__controlador_hospede.buscar_hospede(valores["cpf"])
                if not hospede:  # não existe
                    self.__tela_reserva.msg("Hóspede com esse CPF não foi encontrado no banco dados, favor cadastrar:")
                    hospede = self.__controlador_hospede.cadastrar()
                if hospede != None:
                    hospedes.append(hospede)

            elif opçao == "check-in":
                self.finalizar_check_in(reserva, hospedes)
                self.__tela_reserva.msg("check-in realizado com sucesso!")
                opçao = 0
            self.__tela_reserva.close_menu_check_in()
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED or opçao == "voltar":
                return 1


    def getReservadoDia(self, n_quarto, dia):
        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto and reserva.status != 0:
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


    def listar_reservas(self, dia):
        cores = [(row, cor) for row, cor in enumerate(self.getStatusQuartos(dia))]
        lista = [[reserva.cod, "Concluída" if reserva.status == 0 else "Reservado" if reserva.status == 1 else "Ocupado", reserva.quarto.numero, reserva.data_entrada, reserva.data_saida, reserva.lista_hospedes[0].nome] for reserva in self.reservas]

        button, values = self.__tela_reserva.opçoes_menu_lista_reservas(lista, cores)
        self.__tela_reserva.close_menu_lista_reservas()

    def excluir_reserva(self, n_quarto, dia_selecionado):
        print(dia_selecionado)

        for reserva in self.reservas:
            if reserva.quarto.numero == n_quarto:
                if dt.strptime(reserva.data_entrada, "%d-%m-%y").date() <= dia_selecionado <= dt.strptime(reserva.data_saida, "%d-%m-%y").date():
                    inicio = dt.strptime(reserva.data_entrada, "%d-%m-%y").date()
                    hoje = dt.today().date()
                    if inicio <= hoje:
                        multa = 600 + (hoje - inicio).days * 600

                    opçao, valores = self.__tela_reserva.opçao_cancelar(multa)
                    if opçao == 1:
                        self.reservas.remove(reserva)
                        self.__reserva_dao.atualizar()
                        self.__tela_reserva.msg(f"Reserva cancelada!")

                    return 1


    def abre_tela(self, botao, dia):                 # clica quarto mapa (recebe numero dele aqui (botao) e dia selecionado)
        lista_opçoes = {"reservar": self.realizar_reserva, "excluir": self.excluir_reserva,
                        "check-in": self.check_in , "check-out": self.checkout}
        
        while True:
            for i in self.__reserva_dao.get_all():                        
                print(i.quarto.numero, i.data_entrada, i.data_saida)   
            reserva = self.getReservadoDia(botao, dia)

            print(reserva)
            if reserva:
                if dia == dt.today().date():
                    if reserva.status == 1:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_reservado(reserva)
                        self.__tela_reserva.close_menu_reserva_hoje_reservado()
                    elif reserva.status == 2:
                        opçao, valores = self.__tela_reserva.opçoes_menu_reserva_hoje_ocupado(reserva)
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

            if opçao == "excluir":
                if lista_opçoes[opçao](botao, dia):
                    break

            elif opçao in ['check-out', 'check-in']:
                if lista_opçoes[opçao](reserva):
                    break
                




