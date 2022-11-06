import PySimpleGUI as sg


class TelaFuncionario():
    def __init__(self):
        self.__windows_menu = None
        self.menu()

    def menu(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MENU', font=("Arial", 20)), sg.Button("Sair", key="deslogar", pad=((640, 0),(10,0)))],
            [sg.Button('Menu Hóspede', key="menu_hospede")],
            [sg.Button('Reservar', key="reservar")],

            [sg.Button('QUARTO 1', key=1, pad=((0, 0),(130,0))), sg.Button('QUARTO 2', key=2, pad=((0, 0),(130,0))), sg.Button('QUARTO 3', key=3, pad=((0, 0),(130,0))), sg.Button('QUARTO 4', key=4, pad=((0, 0),(130,0)))],
            [sg.Button('QUARTO 5', key=5, pad=((0, 0),(10,0))), sg.Button('QUARTO 6', key=6, pad=((0, 0),(10,0))), sg.Button('QUARTO 7', key=7, pad=((0, 0),(10,0))), sg.Button('QUARTO 8', key=8, pad=((0, 0),(10,0)))]
                ]
        self.__windows_menu = sg.Window('MENU', size=(800, 450), element_justification="c").Layout(layout)

    def opçoes_menu(self):
        self.menu()
        button, values = self.__windows_menu.Read()
        if button is None:
            button = 0
        return button, values

    def close_menu(self):
        self.__windows_menu.Close()

    def msg(self, msg):
        sg.Popup(msg, any_key_closes=True)