import PySimpleGUI as sg

# tela inicial do sistema

class TelaPrincipal():

    def __init__(self):
        self.__window = None
        self.cadastro_gerente()
        self.login()

    def cadastro_gerente(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Cadastro Gerente')],
            [sg.Text('Nome'), sg.Input(key="Nome")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Button('Cadastrar', key="cadastrar")],
            [sg.Button('Sair', key=0)]
                ]
        self.__window_cadastro_gerente = sg.Window('Cadastro Gerente').Layout(layout)

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

    def opcoes(self):
        button, values = self.__window.Read()
        if button is None:
            button = 0
        return button


    def close_login(self):
        self.__window_login.Close()
        self.login()

    def close_cadastro_gerente(self):
        self.__window_cadastro_gerente.Close()
        self.cadastro_gerente()