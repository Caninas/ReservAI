import PySimpleGUI as sg


class TelaReserva():
    def __init__(self):
        pass

    def menu_reservar(self, quarto, dia):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o CPF do Hóspede principal: ', font=("Arial", 15)), sg.Input(key="cpf")],
            [sg.Text(f"Quarto {quarto}")],
            [sg.Text('Data de Entrada: '), sg.Input(dia, key='data_entrada',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data de entrada', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_entrada', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data de Saída: '), sg.Input(key='data_saida', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data de saída', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_saida', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            
            [sg.Button('Confirmar', key="reservar")],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__windows_menu_reservar = sg.Window('MENU RESERVAR', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_hoje_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Check-in', key="check-in"), sg.Button('Editar Reserva', key="editar"), sg.Button('Excluir Reserva', key="excluir")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_hoje_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_hoje_ocupado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Editar Reserva', key="editar"), sg.Button('Finalizar Reserva (checkout)', key="chekout")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_hoje_ocupado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_outro_reservado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Editar Reserva', key="editar"), sg.Button('Excluir Reserva', key="excluir")],
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_outro_reservado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def menu_reserva_outro_ocupado(self, reserva):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text(f'Reserva número: {reserva.cod} ', font=("Arial", 15))],
            [sg.Text(f'Hóspede principal: {reserva.lista_hospedes[0].nome} ({reserva.lista_hospedes[0].cpf}) ', font=("Arial", 15))],
            [sg.Text(f'Data de Entrada: {reserva.data_entrada}')],
            [sg.Text(f'Data de Saída: {reserva.data_saida}')],
            
            [sg.Button('Voltar', key=0)]
        ]
        self.__windows_menu_reserva_outro_ocupado = sg.Window('MENU RESERVA', size=(800, 450), element_justification="c").Layout(layout)

    def opçoes_menu_reserva_hoje_reservado(self, reserva):
        self.menu_reserva_hoje_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_hoje_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values

    def opçoes_menu_reserva_hoje_ocupado(self, reserva):
        self.menu_reserva_hoje_ocupado(reserva)
            
        button, values = self.__windows_menu_reserva_hoje_ocupado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def opçoes_menu_reserva_outro_reservado(self, reserva):
        self.menu_reserva_outro_reservado(reserva)
            
        button, values = self.__windows_menu_reserva_outro_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values
    
    def opçoes_menu_reserva_outro_ocupado(self, reserva):
        self.menu_reserva_outro_ocupado(reserva)
            
        button, values = self.__windows_menu_reserva_outro_reservado.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        return button, values

    def opçoes_reservar(self, quarto, dia, retornar=False):
        if retornar == False:
            self.menu_reservar(quarto, dia)
        while True:
            button, values = self.__windows_menu_reservar.Read()
            print(values)
            values.pop("Abrir Calendário")      #tirar o campo do calendario q é inutil (e sao 2)
            values.pop("Abrir Calendário0")

            vazio = False
            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    print(valor)
                    vazio = True
                    break

            if not values["cpf"].isnumeric():
                self.msg("O CPF deve ser digitado apenas com números")
                continue

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_entrada"].split("-")
            data2 = values["data_saida"].split("-")
            print(data1, data2)
            if any([len(x) != 2 or len(data1) != 3 for x in data1]) or any([len(x) != 2 or len(data2) != 3 for x in data2]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue

            return button, values

    def close_menu_reservar(self):
        self.__windows_menu_reservar.Close()

    def close_menu_reserva_hoje_reservado(self):
        self.__windows_menu_reserva_hoje_reservado.Close()

    def close_menu_reserva_hoje_ocupado(self):
        self.__windows_menu_reserva_hoje_ocupado.Close()

    def close_menu_reserva_outro_reservado(self):
        self.__windows_menu_reserva_outro_reservado.Close()

    def msg(self, msg):
        sg.Popup(msg)