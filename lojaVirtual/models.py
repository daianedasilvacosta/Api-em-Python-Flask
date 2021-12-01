
class Jogo:
    def __init__(self, nome, categoria, console, preco, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.preco = preco

class Usuario:
    def __init__(self,id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha