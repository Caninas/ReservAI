from Entidade.Funcionario import Funcionario


class DAOfuncionario():
    def __init__(self, dataSource, cript):
        self.__main = dataSource
        self.__cache = []

        self.abrir("funcionarios")

    def abrir(self, tipo):
        self.__cache = self.__main.abrir(tipo)

    def get_all(self):
        return self.__cache

    def getFuncionario(self, usuario):
        objFuncionarios = 0
        for funcionario in self.__cache:
            if funcionario.usuario == usuario:
                objFuncionarios = funcionario

        return objFuncionarios

    def getFuncionarioCPF(self, cpf):
        objFuncionarios = 0
        for funcionario in self.__cache:
            if funcionario.cpf == int(cpf):
                objFuncionarios = funcionario

        return objFuncionarios

    def atualizar(self):
        self.__main.guardar(["funcionarios", self.__cache])

    def add(self, objeto: Funcionario):
        if objeto != None and isinstance(objeto, Funcionario):
            self.__cache.append(objeto)  # guarda no cache local
            self.__main.guardar(["funcionarios", self.__cache])  # guarda no cache principal e no disco

    def remove(self, objeto: Funcionario):
        if objeto != None and isinstance(objeto, Funcionario):
            self.__cache.remove(objeto)  # guarda no cache local
            self.__main.guardar(["funcionarios", self.__cache])  # guarda no cache principal e no disco
