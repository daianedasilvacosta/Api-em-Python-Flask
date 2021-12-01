
class Cliente:
    def __init__(self, nomecliente, cpfcliente, enderecocliente, emailcliente, id=None):
        self.id = id
        self.nomecliente = nomecliente
        self.cpfcliente = cpfcliente
        self.enderecocliente = enderecocliente
        self.emailcliente = emailcliente

class Funcionario:
    def __init__(self,id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha