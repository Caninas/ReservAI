import PySimpleGUI as sg

# tela inicial do sistema

class TelaPrincipal():

    def __init__(self):
        self.__window_login = None
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
        self.__window_login = sg.Window('Login no sistema').Layout(layout)

    def cadastro_gerente_primeira_vez(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Bem vindo ao sistema ReservAI, porfavor gerente, faca seu cadastro!')],
            [sg.Text('Cadastro Gerente')],
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Button('Cadastrar', key="cadastrar")],
            [sg.Button('Sair', key=0)]
        ]

        window = sg.Window('Cadastro de Funcionário', layout, element_justification='center')

        event, values = window.read()

        window.close()
        if event == "Sair" or event == sg.WIN_CLOSED:
            return None
        return {"nome": values['nome'], "senha": values['senha']}


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