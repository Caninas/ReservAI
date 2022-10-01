import PySimpleGUI as sg


class TelaFuncionario():
    def __init__(self):
        self.__windows_menu = None
        self.menu()

    def menu(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MENU'), sg.Button(key="DESLOGAR")],
            [sg.Button('Cadastrar Funcionário', key="cadastrar_func")],
            [sg.Text('MAPA')],
            [sg.Button('Sair', key=0)]
                ]
        self.__windows_menu = sg.Window('MENU').Layout(layout)

    def opçoes_menu(self):
        button, values = self.__windows_menu.Read()
        if button is None:
            button = 0
        return button, values

    def close_menu(self):
        self.__windows_menu.Close()
        #self.login()

    def msg(self, msg):
        sg.Popup(msg)