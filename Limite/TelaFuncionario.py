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
            [sg.Text('MAPA', font=("Arial", 15), pad=((0, 0),(180,0)))],
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
        sg.Popup(msg)