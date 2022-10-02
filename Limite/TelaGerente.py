import PySimpleGUI as sg


class TelaGerente():
    def __init__(self):
        self.__windows_menu = None
        self.menu()
        self.menu_cadastrar_func()

    def menu(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('MENU'), sg.Button("Sair", key="deslogar")],
            [sg.Button('Cadastrar Funcionário', key="cadastrar_func")],
            [sg.Text('MAPA')],
                ]
        self.__windows_menu = sg.Window('MENU').Layout(layout)

    def menu_cadastrar_func(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Cadastro Funcionário')],
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('Usuário'), sg.Input(key="usuario")],
            [sg.Text('Senha'), sg.Input(key="senha")],
            [sg.Text('CPF'), sg.Input(key="cpf")],
            [sg.Text('Data de Nascimento'), sg.Input(key="data_nascimento")],
            [sg.Text('Telefone'), sg.Input(key="telefone")],
            [sg.Text('E-mail'), sg.Input(key="email")],
            [sg.Button('Cadastrar', key="cadastrar")],
            [sg.Button('Sair', key=0)]
        ]

        self.__windows_cadastro_func = sg.Window('Cadastro Funcionário').Layout(layout)

    def cadastrar_func(self):
        self.menu_cadastrar_func()
        while True:
            button, values = self.__windows_cadastro_func.Read()
            
            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True

            if vazio == True or not values["cpf"].isnumeric():
                self.msg("Todos os campos devem ser preenchidos!")
                continue

                
            return button, values

    def opçoes_menu(self):
        self.menu()
        button, values = self.__windows_menu.Read()
        if button is None:
            button = 0
        return button, values

    def close_cadastro_func(self):
        self.__windows_cadastro_func.Close()

    def close_menu(self):
        self.__windows_menu.Close()
        #self.login()

    def msg(self, msg):
        sg.Popup(msg)