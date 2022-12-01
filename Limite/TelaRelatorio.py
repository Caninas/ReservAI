import PySimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        pass

    @property
    def window_menu(self):
        return self.__window_menu
        
    def menu(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Button('Voltar (seta)', key=0, font=("Arial", 20)), sg.Text("Relatórios", font=("Arial", 20))],
            [sg.Button('Reservas', key="rel_reservas"), sg.Button('Hóspedes', key="rel_hospedes")],
            [sg.Button('Passeios', key="rel_passeios")]
        ]


        self.__window_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)

    def menu_rel_reservas(self):
        layout = [
            [sg.Button('Voltar (seta)', key=0, font=("Arial", 20)), sg.Text("Selecione o período desejado: ")],
            [sg.Text('Data Inicial: '), sg.Input(key='data_inicial',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data inicial', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_inicial', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data Final: '), sg.Input(key='data_final', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data do final', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_final', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Button("Confirmar", key=1, size=(20,1))]
        ]

        self.__window_menu_rel_reservas = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    
    def menu_rel_reservas_dados(self, dados):
        layout = [
            [sg.Button('Voltar (seta)', key=0, font=("Arial", 20)), sg.Text("Selecione o período desejado: ")],
            [sg.Text('Data Inicial: '), sg.Input(key='data_inicial',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data inicial', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_entrada', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data Final: '), sg.Input(key='data_final', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data do final', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_saida', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Input("Confirmar", key=1, size=(20,1))],
            # data
            [sg.Text(f'Total de Reservas: ${dados}')],
        ]
        self.__window_menu_rel_reservas_dados = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    
    
    def opçoes_menu_rel_reservas(self):
        self.menu_rel_reservas()
        button, values = self.__window_menu_rel_reservas.Read()

        if button is None:
            button = 0

        return button, values

    def opçoes_menu_rel_reservas_dados(self, dados):
        self.menu_rel_reservas_dados(dados)
        button, values = self.__window_menu_rel_reservas_dados.Read()

        if button is None:
            button = 0

        return button, values
    def opçoes_menu(self):
        self.menu()
        button, values = self.__window_menu.Read()

        if button is None:
            button = 0

        return button, values

    def close_menu(self):
        self.__window_menu.Close()

    def close_window_menu_rel_reservas_dados(self):
        self.__window_menu_rel_reservas_dados.close()

    def close_menu_rel_reservas(self):
        self.__window_menu_rel_reservas.Close()

    def msg(self, msg):
        sg.Popup(msg)
