from Persistencia.DAOgerente import DAOgerente
#from Limite.TelaGerente import TelaGerente

class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__gerente_dao = DAOgerente()
        self.__controlador_sistema = controlador_sistema
        #self.__tela_gerente = TelaGerente()

    @property
    def gerentes(self):
        return self.__gerente_dao.get_all()

    def verificar_se_nome_existe(self, nome):
        for gerente in self.__gerente_dao.get_all():
            if gerente.nome == nome:
                return True
        return False
