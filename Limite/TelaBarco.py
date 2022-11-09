import PySimpleGUI as sg


class TelaBarco:
    def __init__(self):
        #self.menu()
        pass

    @property
    def window_menu(self):
        return self.__window_menu


    def msg(self, msg):
        sg.Popup(msg)

    def close_menu(self):
        self.__window_menu.Close()



    def menu(self, cores, data="00/00/00"):
        sg.ChangeLookAndFeel('Reddit')
        layout = [

            [sg.Button("Dia anterior", key="se", pad=((0, 15), (30, 0))), sg.Text(f"{data}", font=("Arial", 13), key="data", pad=((0, 0), (30, 0))),sg.Button("Próximo dia", key="sd", pad=((15, 0), (30, 0)))],

            [sg.Button('BARCO 1', key=1, pad=((0, 30),(70,0))), sg.Button('BARCO 2', key=2, pad=((0, 30),(70,0))), sg.Button('BARCO 3', key=3, pad=((0, 30),(70,0)))],
            [sg.Text("          ", key="c1", background_color=cores[0], pad=((0, 60),(0,0))), sg.Text("          ", key="c2", background_color=cores[1], pad=((0, 50),(0,0))), sg.Text("          ", key="c3", background_color=cores[2], pad=((0, 40),(0,0)))],
            [sg.Button("Voltar", key="voltar", pad=((0, 0), (20, 0)))]   
                ]
        self.__window_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    

    def opçoes_menu(self, data, cores, refresh=False):
        if refresh == False:
            self.menu(cores, data)

        button, values = self.__window_menu.Read()
        if button is None:
            button = 0
        return button, values
    
    def menu_reservar(self, barco, dia):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o número da reserva: ', font=("Arial", 15)), sg.Input(key="cpf")],
            [sg.Text(f"Barco {barco}")],
            [sg.Text('Data da Reserva: '), sg.Input(dia, key='data_entrada',size=(20,1))],
            
            [sg.Button('Confirmar', key="reservar")],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__windows_menu_reservar = sg.Window('MENU RESERVAR', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reservabarco_hoje_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva do quarto número: {reserva.cod_reserva} ', font=("Arial", 15))],
            [sg.Text(f'Data da Reserva: {reserva.data_reserva}')],
            
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_hoje_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)
    
    def menu_reservabarco_outro_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Data da Reserva: {reserva.data_reserva}')],
            
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_outro_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)
    
    def opçoes_menu_reservabarco_hoje_reservado(self, reserva):
        self.menu_reservabarco_hoje_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_hoje_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def opçoes_menu_reservabarco_outro_reservado(self, reserva):
        self.menu_reservabarco_outro_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_outro_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def close_menu_reservabarco_outro_reservado(self):
        self.__windows_menu_reserva_outro_reservado.Close()
    
    def close_menu_reservabarco_hoje_reservado(self):
        self.__windows_menu_reserva_hoje_reservado.Close()

    def close_menu_reservar(self):
        self.__windows_menu_reservar.Close()

    def opçoes_reservar(self, barco, dia, retornar=False):
        if retornar == False:
            self.menu_reservar(barco, dia)
        while True:
            button, values = self.__windows_menu_reservar.Read()
            print(values)

            vazio = False
            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    print(valor)
                    vazio = True
                    break

            if not values["cpf"].isnumeric():
                self.msg("O código deve ser digitado apenas com números")
                continue

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_entrada"].split("-")
            print(data1)
            if any([len(x) != 2 or len(data1) != 3 for x in data1]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue

            return button, values