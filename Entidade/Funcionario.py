class Funcionario:
    def __init__(self, nome: str, usuario: str, senha: str, cpf: str, data_nascimento: str, telefone: str, email: str):
        self.__nome = nome.strip()
        self.__usuario = usuario.strip()
        self.__senha = senha.strip()
        self.__cpf = int(cpf.strip())
        self.__data_nascimento = data_nascimento.strip()
        self.__telefone = telefone.strip()
        self.__email = email.strip()

    def atualizar(self, valores):
        self.__usuario = valores["usuario"].strip()
        self.__senha = valores["senha"].strip()
        self.__telefone = valores["telefone"].strip()
        self.__email = valores["email"].strip()

    @property
    def nome(self):
        return self.__nome

    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email