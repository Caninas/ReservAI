from Persistencia.DAObarco import DAObarco
from Persistencia.DAOreserva_barco import DAOreserva_barco
from Persistencia.DAOreserva import DAOreserva
from Limite.TelaBarco import TelaBarco
from Entidade.Reserva_Barco import Reserva_Barco
from Entidade.Barco import Barco
import PySimpleGUI as sg
from datetime import datetime as dt
from datetime import timedelta


class ControladorBarco:
    def __init__(self, controlador_sistema, dao_reserva, dao_barco, dao_reservabarco):
        self.__controlador_sistema = controlador_sistema
        self.__dao_reserva = dao_reserva
        self.__dao_barco = dao_barco
        self.__dao_reservabarco = dao_reservabarco
        self.__dia_selecionado = dt.today().date()
        self.__tela_barco = TelaBarco()
        self.criar_barcos()

    @property
    def barcos(self):
        return self.__dao_barco.get_all()

    @property
    def reservas_barcos(self):
        return self.__dao_reservabarco.get_all()
    
    def criar_barcos(self):                               
        barco = Barco('barco de luxo', 1, 0, 120)
        self.__dao_barco.add(barco)
        barco = Barco('barco normal', 2, 0, 70)
        self.__dao_barco.add(barco)
        barco = Barco('barco humilde', 3, 0, 50)
        self.__dao_barco.add(barco)
    
    
    



    def abre_tela(self):
        lista_opçoes = {"reservar": self.abre_tela_reserva}
        
        dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100} (hoje)"
        refresh = False

        cores_barcos = self.getStatusBarcos(self.__dia_selecionado)

        while True:
            print(self.__dia_selecionado)
            
            opçao, valores = self.__tela_barco.opçoes_menu(dia, cores_barcos, refresh)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED or opçao == "voltar":
                self.__tela_barco.close_menu()
                break

            if opçao == "sd":
                self.__dia_selecionado = self.__dia_selecionado + timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"

                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_barco.window_menu['data'].update(dia)

                cores_barcos = self.getStatusBarcos(self.__dia_selecionado)
                for i in range(len(cores_barcos)):
                    self.__tela_barco.window_menu[f'c{i+1}'].update(background_color=cores_barcos[i])

                refresh = True
                continue
            elif opçao == "se":
                self.__dia_selecionado = self.__dia_selecionado - timedelta(1)
                dia = f"{self.__dia_selecionado.day:02d}-{self.__dia_selecionado.month:02d}-{self.__dia_selecionado.year%100}"

                if self.__dia_selecionado == dt.today().date():
                    dia = dia + " (hoje)"

                self.__tela_barco.window_menu['data'].update(dia)

                cores_barcos = self.getStatusBarcos(self.__dia_selecionado)
                for i in range(len(cores_barcos)):
                    self.__tela_barco.window_menu[f'c{i+1}'].update(background_color=cores_barcos[i])

                refresh = True
                continue
 
            self.__tela_barco.close_menu()
            lista_opçoes["reservar"](opçao, self.__dia_selecionado)
            cores_barcos = self.getStatusBarcos(self.__dia_selecionado)
            refresh = False

    def abre_tela_reserva(self, botao, dia):
        lista_opçoes = {"reservar": self.realizar_reservabarco}
        
        while True:
            for i in self.__dao_reservabarco.get_all(): 
                print(i.barco.numero, i.data_reserva)   
            reserva = self.getReservadoDia(botao, dia)

            print(reserva)
            if reserva:
                if dia == dt.today().date():
                    if reserva.status == 1:
                        opçao, valores = self.__tela_barco.opçoes_menu_reservabarco_hoje_reservado(reserva)
                        self.__tela_barco.close_menu_reservabarco_hoje_reservado()

                else:
                    if reserva.status == 1:
                        opçao, valores = self.__tela_barco.opçoes_menu_reservabarco_outro_reservado(reserva)
                        self.__tela_barco.close_menu_reservabarco_outro_reservado()

            else:
                self.realizar_reservabarco(botao, dia)
                break

            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                break


    def getStatusBarcos(self, dia):
        cores = [0 for x in range(0,3)]

        for reserva in self.reservas_barcos:
            data = reserva.data_reserva
            if dt.strptime(data, "%d-%m-%y").date() == dia:
                if reserva.status == 1:
                    cores[reserva.barco.numero-1] = "red"
        cores = [cor if cor != 0 else "green" for cor in cores]
        print(cores)
        return cores
    
    def getReservadoDia(self, n_barco, dia):
        for reserva in self.reservas_barcos:
            if reserva.barco.numero == n_barco and reserva.status != 0:
                data = reserva.data_reserva
                if dt.strptime(data, "%d-%m-%y").date() == dia:
                    return reserva
        return 0
    
    def checar_data_livre(self, n_barco, valores): #verificar aqui
        livre = True
        for reserva in self.reservas_barcos:
            print('aqui as datas')
            print(reserva.data_reserva)
            print(valores['data_entrada'])
            if reserva.barco.numero == n_barco and reserva.status == 1:
                data = dt.strptime(reserva.data_reserva, "%d-%m-%y").date()
                

                if data == dt.strptime(valores['data_entrada'], "%d-%m-%y").date():
                    livre = False
                    break
                
        
        reservadoquarto = self.__dao_reserva.getReservaCod(valores["cpf"])
        if reservadoquarto:
            inicio = dt.strptime(reservadoquarto.data_entrada, "%d-%m-%y").date()
            fim = dt.strptime(reservadoquarto.data_saida, "%d-%m-%y").date()
            if dt.strptime(valores['data_entrada'], "%d-%m-%y").date() < inicio:
                livre = False
            if dt.strptime(valores['data_entrada'], "%d-%m-%y").date() >= fim:
                livre = False

        if not livre:
            self.__tela_barco.msg("A data é inválida")
            return 0

        return 1

    
    def realizar_reservabarco(self, n_barco, dia):
        print(dia)
        retornar = False
        dia = f"{dia.day:02d}-{dia.month:02d}-{dia.year%100}"

        while True:
            opçao, valores = self.__tela_barco.opçoes_reservar(n_barco, dia, retornar)
            print(opçao,valores)
            
            if opçao == None or opçao == 0 or opçao == sg.WIN_CLOSED:
                self.__tela_barco.close_menu_reservar()
                return

            if self.checar_data_livre(n_barco, valores):
                reservadoquarto = self.__dao_reserva.getReservaCod(valores["cpf"])

                if not reservadoquarto:    # não existe
                    self.__tela_barco.msg("reserva não encontrada")
                    return 

                if reservadoquarto.status == 2:
                    
                    barco = self.__dao_barco.getBarco(n_barco)

                    cod = self.__dao_reservabarco.getCodUltimaReservaBarco() + 1
                    reserva = Reserva_Barco(barco, cod, reservadoquarto.cod, 1,                      
                                    valores["data_entrada"], barco.valor)
                    self.__dao_reservabarco.add(reserva)
                    reservadoquarto.add_reserva_barco(reserva)
                    self.__dao_reserva.atualizar()

                    self.__tela_barco.msg("Reserva realizada com sucesso!")
                    self.__tela_barco.close_menu_reservar()

                    for i in self.__dao_reservabarco.get_all():
                        print(i.info_basica())                      
                    return 1
                else:
                    self.__tela_barco.msg("Reservas de barco só serão feitas após check-in")
            retornar = True