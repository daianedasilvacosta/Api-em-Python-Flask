
class Produto:
    def __init__(self, nomeproduto, descricaoproduto, precoproduto, id=None):
        self.id = id
        self.nomeproduto = nomeproduto
        self.descricaoproduto = descricaoproduto
        self.precoproduto =precoproduto

class Usuario:
    def __init__(self,id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha