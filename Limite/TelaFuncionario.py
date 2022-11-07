import PySimpleGUI as sg


class TelaFuncionario():
    def __init__(self):
        pass

    @property
    def window_menu(self):
        return self.__window_menu
        
    def menu(self, cores, data="00/00/00"):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MENU', font=("Arial", 20)), sg.Button("Sair", key="deslogar", pad=((640, 0),(10,0)))],
            [sg.Button('Menu Hóspede', key="menu_hospede"),  sg.Button('Menu barco', key="menu_barco")],
            
            [sg.Button("Dia anterior", key="se"), sg.Text(f"{data}", key="data"),sg.Button("Próximo dia", key="sd")],

            [sg.Button('QUARTO 1', key=1, pad=((0, 30),(130,0))), sg.Button('QUARTO 2', key=2, pad=((0, 30),(130,0))), sg.Button('QUARTO 3', key=3, pad=((0, 30),(130,0))), sg.Button('QUARTO 4', key=4, pad=((0, 0),(130,0)))],
            [sg.Text("          ", key="c1", background_color=cores[0], pad=((0, 61),(0,0))), sg.Text("          ", key="c2", background_color=cores[1], pad=((0, 61),(0,0))), sg.Text("          ", key="c3", background_color=cores[2], pad=((0, 61),(0,0))), sg.Text("          ", key="c4", background_color=cores[3], pad=((0, 0),(0,0)))],
            [sg.Button('QUARTO 5', key=5, pad=((0, 30),(30,0))), sg.Button('QUARTO 6', key=6, pad=((0, 30),(30,0))), sg.Button('QUARTO 7', key=7, pad=((0, 30),(30,0))), sg.Button('QUARTO 8', key=8, pad=((0, 0),(30,0)))],
            [sg.Text("          ", key="c5", background_color=cores[4], pad=((0, 61),(0,0))), sg.Text("          ", key="c6", background_color=cores[5], pad=((0, 61),(0,0))), sg.Text("          ", key="c7", background_color=cores[6], pad=((0, 61),(0,0))), sg.Text("          ", key="c8", background_color=cores[7], pad=((0, 0),(0,0)))],
                ]
        self.__window_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)

    def opçoes_menu(self, data, cores, refresh=False):
        if refresh == False:
            self.menu(cores, data)
        button, values = self.__window_menu.Read()
        if button is None:
            button = 0
        return button, values

    def close_menu(self):
        self.__window_menu.Close()

    def msg(self, msg):
        sg.Popup(msg)
