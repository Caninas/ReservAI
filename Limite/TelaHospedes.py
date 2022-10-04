import PySimpleGUI as sg


class TelaHospedes():
    def __init__(self):
        self.cadastro()
        sg.ChangeLookAndFeel('Reddit')

    def menu(self):
        layout = [
            [sg.Text('Menu Hóspede', font=("Arial", 20))], # trocar para imagem photoshop

            [sg.Button('Cadastrar', key="cadastrar_hospede")],
            [sg.Button('Alterar Informações', key="alterar_hospede")],
            [sg.Button('Excluir', key="excluir_hospede")],

            [sg.Button('Voltar', key=0)]
        ]
        self.__window_menu = sg.Window('Menu Hóspede', element_justification="c").Layout(layout)

    def cadastro(self):
        layout = [
            [sg.Text('Cadastro Hóspede', font=("Arial", 15))],
            [sg.Text('Nome'), sg.Input(key="nome")],
            [sg.Text('CPF'), sg.Input(key="cpf")],
            [sg.Text('Data de Nascimento'), sg.Input(key="data_nascimento")],
            [sg.Text('Sexo'), sg.Input(key="sexo")],
            [sg.Text('Telefone'), sg.Input(key="telefone")],
            [sg.Text('E-mail'), sg.Input(key="email")],
            [sg.Text('Nacionalidade'), sg.Input(key="nacionalidade")],
            [sg.Text('Endereço:')],
            [sg.Text('Rua'), sg.Input(key="rua")],
            [sg.Text('Numero e apartamento'), sg.Input(key="num")],
            [sg.Text('Cidade'), sg.Input(key="cidade")],
            [sg.Text('Estado'), sg.Input(key="estado")],
            [sg.Text('Pais'), sg.Input(key="pais")],
            [sg.Button('Cadastrar', key="cadastrar")],
            [sg.Button('Cancelar', key=0)]
        ]
        self.__window_cadastro = sg.Window('Cadastro Hóspede').Layout(layout)

    def alterar(self, hospede):
        layout = [
            [sg.Text('Alterar Hóspede', font=("Arial", 15))],
            [sg.Text('Nome'), sg.Input(hospede.nome, key="nome")],
            [sg.Text('CPF'), sg.Input(hospede.cpf, key="cpf")],
            [sg.Text('Data de Nascimento'), sg.Input(hospede.data_nascimento, key="data_nascimento")],
            [sg.Text('Sexo'), sg.Input(hospede.sexo, key="sexo")],
            [sg.Text('Telefone'), sg.Input(hospede.telefone, key="telefone")],
            [sg.Text('E-mail'), sg.Input(hospede.email, key="email")],
            [sg.Text('Nacionalidade'), sg.Input(hospede.nacionalidade, key="nacionalidade")],
            [sg.Text('Endereço:')],
            [sg.Text('Rua'), sg.Input(hospede.end_rua, key="rua")],
            [sg.Text('Numero e apartamento'), sg.Input(hospede.end_num, key="num")],
            [sg.Text('Cidade'), sg.Input(hospede.end_cidade, key="cidade")],
            [sg.Text('Estado'), sg.Input(hospede.end_estado, key="estado")],
            [sg.Text('Pais'), sg.Input(hospede.end_pais, key="pais")],
            [sg.Button('Alterar', key="alterar")],
            [sg.Button('Cancelar', key=0)]
            ]

        self.__window_alterar_hospede = sg.Window('Alterar Hóspede').Layout(layout)
        
    def excluir(self, nome_hospede=None):
        confirmar = [
            [sg.Text('Tem certeza que deseja excluir:', font=("Arial", 15))],
            [sg.Text(nome_hospede, font=("Arial", 15), justification="c")],

            [sg.Button('Sim', key="sim")],
            [sg.Button('Cancelar', key=0)]
        ]
        
        self.__window_excluir = sg.Window('Excluir Hóspede').Layout(confirmar)

    def busca(self):
        layout = [
            [sg.Text('Buscar Hóspede', font=("Arial", 15))],
            [sg.Text('CPF'), sg.Input(key="cpf")],

            [sg.Button('Buscar', key="buscar")],
            [sg.Button('Cancelar', key=0)]
        ]

        self.__window_busca = sg.Window('Buscar Hóspede').Layout(layout)

    def opçoes_menu(self):
        self.menu()
        button, values = self.__window_menu.Read()
        if button is None:
            button = 0
        return button, values

    def buscar_hospede(self):
        self.busca()
        button, values = self.__window_busca.Read()
        if button is None:
            button = 0
        return button, values

    def opçoes_cadastro(self):
        self.cadastro()
        while True:
            button, values = self.__window_cadastro.Read()
            
            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True
                    break

            if vazio == True or not values["cpf"].isnumeric():
                self.msg("Todos os campos devem ser preenchidos corretamente!")
                continue
                
            return button, values
    
    def alt_hospede(self, hospede):
        self.alterar(hospede)
        while True:
            button, values = self.__window_alterar_hospede.Read()
            
            vazio = False

            if button == None or button == 0 or button == sg.WIN_CLOSED:
                return button, values

            for valor in values.values():
                if valor == "" or valor == None:
                    vazio = True
                    break

            if vazio == True or not values["cpf"].isnumeric():
                self.msg("Todos os campos devem ser preenchidos corretamente!")
                continue
                
            return button, values
        
    def excluir_hospede(self, hospede):
        self.excluir(hospede.nome)
        button, values = self.__window_excluir.Read()

        if button == None or button == 0 or button == sg.WIN_CLOSED:
            return button, values

        for valor in values.values():
            if valor == "" or valor == None:
                vazio = True
            
        return button, values

    def close_menu(self):
        self.__window_menu.Close()
        
    def close_busca(self):
        self.__window_busca.Close()

    def close_cadastro(self):
        self.__window_cadastro.Close()

    def close_alt_hospede(self):
        self.__window_alterar_hospede.Close()
        
    def close_excluir_hospede(self):
        self.__window_excluir.Close()

    def msg(self, msg):
        sg.Popup(msg)