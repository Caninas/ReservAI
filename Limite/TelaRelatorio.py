import PySimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        pass

    @property
    def window_menu_rel_reservas(self):
        return self.__window_menu_rel_reservas

    @property
    def window_menu_rel_hospedes(self):
        return self.__window_menu_rel_hospedes

    def menu(self):
        layout = [
            [sg.Text("Relatórios", font=("Arial", 20))],
            [sg.Button('Reservas', key="rel_reservas", size=(10, 2)), sg.Button('Hóspedes', key="rel_hospedes", size=(10, 2))],
            [sg.Button('Passeios', key="rel_passeios", size=(10, 2))],
            [sg.Button("Voltar", size=(22, 1), key=0)],
        ]


        self.__window_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)

    def menu_rel_reservas(self):
        layout = [
            [sg.Text("Selecione o período desejado: ", font=("Arial", 15))],
            [sg.Text('Data Inicial: '), sg.Input(key='data_inicial',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data inicial', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_inicial', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data Final: '), sg.Input(key='data_final', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data do final', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_final', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Button("Visualizar", key=1, size=(20,1), pad=((0,0),(10,0)))],
            [sg.Button("Voltar", size=(20, 1), key=0)],
            [sg.Button("Exportar", size=(20, 1), key='exportar', disabled=True)],
            
            [sg.Text(key="total_reservas", font=("Arial", 16), pad=((0,0),(25,0)))],
            [sg.Text(key="tempo_medio", font=("Arial", 16))],
            [sg.Text(key="ocupaçao_media", font=("Arial", 16))],
            [sg.Text(key="receita_total", font=("Arial", 16))],
            [sg.Text(key="receita_media_dia", font=("Arial", 16))],
        ]
        

        self.__window_menu_rel_reservas = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    
    def opçoes_menu_rel_reservas(self, update=False):
        if not update:
            self.menu_rel_reservas()
        while True:    
            button, values = self.__window_menu_rel_reservas.Read()

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            values.pop("Abrir Calendário")      #tirar o campo do calendario q é inutil (e sao 2)
            values.pop("Abrir Calendário0")

            vazio = False

            for valor in values.values():
                if valor == "" or valor == None:
                    print(valor)
                    vazio = True
                    break

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_inicial"].split("-")
            data2 = values["data_final"].split("-")

            if any([len(x) != 2 or len(data1) != 3 for x in data1]) or any([len(x) != 2 or len(data2) != 3 for x in data2]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue


            return button, values





    def menu_rel_hospedes(self):
        layout = [
            [sg.Text("Selecione o período desejado: ", font=("Arial", 15))],
            [sg.Text('Data Inicial: '), sg.Input(key='data_inicial',size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data inicial', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_inicial', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Text('Data Final: '), sg.Input(key='data_final', size=(20,1)), sg.CalendarButton('Abrir Calendário', title='Selecione a data do final', no_titlebar=False, format='%d-%m-%y', close_when_date_chosen=False, target='data_final', month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('S', 'T', 'Q', 'Q', 'S', 'S', 'D'))],
            [sg.Button("Visualizar", key=1, size=(20,1), pad=((0,0),(10,0)))],
            [sg.Button("Voltar", size=(20, 1), key=0)],
            [sg.Button("Exportar", size=(20, 1), key='exportar', disabled=True)],
            
            [sg.Text(key="total_hospedes", font=("Arial", 12), pad=((0,0),(25,0)))],
            [sg.Text(key="idade_media", font=("Arial", 12))],
            [sg.Text(key="sexo_masc", font=("Arial", 12))],
            [sg.Text(key="sexo_fem", font=("Arial", 12))],
            [sg.Text(key="sexo_outros", font=("Arial", 12))],
            [sg.Text(key="cidade1", font=("Arial", 12))],
            [sg.Text(key="cidade2", font=("Arial", 12))],
            [sg.Text(key="cidade3", font=("Arial", 12))],
        ]
        

        self.__window_menu_rel_hospedes = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)
    
    def opçoes_menu_rel_hospedes(self, update=False):
        if not update:
            self.menu_rel_hospedes()
        while True:    
            button, values = self.__window_menu_rel_hospedes.Read()

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            values.pop("Abrir Calendário") 
            values.pop("Abrir Calendário0")

            vazio = False

            for valor in values.values():
                if valor == "" or valor == None:
                    print(valor)
                    vazio = True
                    break

            if vazio == True:
                self.msg("Todos os campos devem ser preenchidos!")
                continue

            data1 = values["data_inicial"].split("-")
            data2 = values["data_final"].split("-")

            if any([len(x) != 2 or len(data1) != 3 for x in data1]) or any([len(x) != 2 or len(data2) != 3 for x in data2]):
                self.msg("O formato da data deve ser Ex: '29-12-22'")
                continue


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

    def close_menu_rel_hospedes(self):
        self.__window_menu_rel_hospedes.Close()

    def msg(self, msg):
        sg.Popup(msg)
