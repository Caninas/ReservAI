import PySimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        pass

    @property
    def window_menu_rel_reservas(self):
        return self.__window_menu_rel_reservas
        
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
            [sg.Button("Confirmar", key=1, size=(20,1))],
            
            [sg.Text(key="total_reservas", font=("Arial", 16))],
            [sg.Text(key="tempo_medio", font=("Arial", 16))],
            [sg.Text(key="ocupaçao_media", font=("Arial", 16))],
            [sg.Text(key="receita_total", font=("Arial", 16))],
            [sg.Text(key="receita_media_dia", font=("Arial", 16))],
        ]
        

        self.__window_menu_rel_reservas = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    
    def opçoes_menu_rel_reservas(self, update=False):
        if not update:
            self.menu_rel_reservas()
            
        button, values = self.__window_menu_rel_reservas.Read()

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

    def close_menu_rel_reservas(self):
        self.__window_menu_rel_reservas.Close()

    def msg(self, msg):
        sg.Popup(msg)
