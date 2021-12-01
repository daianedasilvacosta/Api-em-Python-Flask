from models import Pedido, Usuario

SQL_DELETA_PEDIDO = 'delete from pedido where id = %s'
SQL_PEDIDO_POR_ID = 'SELECT id, nomepedido, categoriapedido, descricaopedido, precopedido from pedido where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_PEDIDO = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s, preco=%s where id = %s'
SQL_BUSCA_PEDIDOS = 'SELECT id, nomepedido, categoriapedido, descricaopedido, precopedido from pedido'
SQL_CRIA_PEDIDO = 'INSERT into pedido (nomepedido, categoriapedido, descricaopedido, precopedido) values (%s, %s, %s, %s)'


class PedidoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, pedido):
        cursor = self.__db.connection.cursor()

        if (pedido.id):
            cursor.execute(SQL_ATUALIZA_PEDIDO, (pedido.nomepedido, pedido.categoriapedido, pedido.descricaopedido, pedido.precopedid, pedido.id))
        else:
            cursor.execute(SQL_CRIA_PEDIDO, (pedido.nomepedido, pedido.categoriapedido, pedido.descricaopedido, pedido.precopedido))
            pedido.id = cursor.lastrowid
        self.__db.connection.commit()
        return pedido

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_PEDIDOS)
        pedidos = traduz_pedidos(cursor.fetchall())
        return pedidos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PEDIDO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Pedido(tupla[1], tupla[2], tupla[3],tupla[4], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_PEDIDO, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_pedidos(pedidos):
    def cria_jogo_com_tupla(tupla):
        return Pedido(tupla[1], tupla[2], tupla[3],tupla[4], id=tupla[0])
    return list(map(cria_jogo_com_tupla, pedidos))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])