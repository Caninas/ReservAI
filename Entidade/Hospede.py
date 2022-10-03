class Hospede:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, telefone: str,
                 email: str, sexo: str, nacionalidade: str, end_rua: str, end_num: str,
                 end_cidade: str, end_estado: str, end_pais: str):

        self.__nome = nome.strip()
        self.__cpf = int(cpf.strip())
        self.__data_nascimento = data_nascimento.strip()
        self.__sexo = sexo.strip()
        self.__telefone = telefone.strip()
        self.__email = email.strip()
        self.__nacionalidade = nacionalidade.strip()
        self.__end_rua = end_rua.strip()
        self.__end_num = end_num.strip()
        self.__end_cidade = end_cidade.strip()
        self.__end_estado = end_estado.strip()
        self.__end_pais = end_pais.strip()

    def atualizar(self, valores):
        self.__nome = valores["nome"].strip()
        self.__cpf = int(valores["cpf"].strip())
        self.__data_nascimento = valores["data_nascimento"].strip()
        self.__sexo = valores["sexo"].strip()
        self.__telefone = valores["telefone"].strip()
        self.__email = valores["email"].strip()
        self.__nacionalidade = valores["nacionalidade"].strip()
        self.__end_rua = valores["rua"].strip()
        self.__end_num = valores["num"].strip()
        self.__end_cidade = valores["cidade"].strip()
        self.__end_estado = valores["estado"].strip()
        self.__end_pais = valores["pais"].strip()

    @property
    def nome(self):
        return self.__nome

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

    @property
    def sexo(self):
        return self.__sexo

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def end_rua(self):
        return self.__end_rua

    @property
    def end_num(self):
        return self.__end_num

    @property
    def end_cidade(self):
        return self.__end_cidade

    @property
    def end_estado(self):
        return self.__end_estado

    @property
    def end_pais(self):
        return self.__end_pais
