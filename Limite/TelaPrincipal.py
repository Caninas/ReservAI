import PySimpleGUI as sg

# tela inicial do sistema

class TelaPrincipal():

    def __init__(self):
        self.__window_login = None
        self.login()

    def login(self):
        sg.ChangeLookAndFeel('Reddit') 
        layout = [
            [
                sg.Frame("", [
            [sg.Text('LOGIN', font=("Arial", 15), justification="c")],
            [sg.Text('Usuário'), sg.Input(key="usuario")],
            [sg.Text('Senha'), sg.Input(key="senha", password_char="*")],
            [sg.Button('Entrar', key="entrar", bind_return_key=True)],
            [sg.Button('Sair', key=0)]
                            ], border_width=0, pad=((0,0),(130,0)), element_justification="c")
            ]
                ]
        self.__window_login = sg.Window('Login no sistema', size=(800, 450), element_justification="c").Layout(layout)

    def mostra_mensagem(self, msg):
        sg.Popup(msg)

    def cadastro_gerente_primeira_vez(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Bem vindo ao sistema ReservAI, porfavor gerente, faca seu cadastro!')],
            [sg.Text('Cadastro Gerente')],
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('Usuário'), sg.Input(key="usuario")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Button('Cadastrar', key="cadastrar", bind_return_key=True)],
            [sg.Button('Sair', key=0)]
        ]

        window = sg.Window('Cadastro de Funcionário', layout, size=(800, 450), element_justification="c")

        event, values = window.read()

        window.close()
        if event == 0 or event == sg.WIN_CLOSED:
            return None
        return {"nome": values['nome'], "usuario": values['usuario'], "senha": values['senha']}

    def opcoes_login(self):
        self.login()
        button, values = self.__window_login.Read()
        if button is None:
            button = 0
        return button, values

    def close_login(self):
        self.__window_login.Close()
        self.login()

    def msg(self, msg):
        sg.Popup(msg)