import PySimpleGUI as sg

# tela inicial do sistema

class TelaPrincipal():

    def __init__(self):
        self.__window = None
        self.cadastro_gerente()
        self.login()

    def login(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('LOGIN')],
            [sg.Text('Usuário'), sg.Input(key="usuario")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Button('Entrar', key="entrar")],
            [sg.Button('Sair', key=0)]
                ]
        self.__window_login = sg.Window('Cadastro Gerente').Layout(layout)


    def opcoes_login(self):
        button, values = self.__window_login.Read()
        if button is None:
            button = 0
        return button, values

    def close_login(self):
        self.__window_login.Close()
        self.login()

    def msg(self, msg):
        sg.Popup(msg)