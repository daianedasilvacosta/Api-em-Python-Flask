from models import Cliente, Funcionario

SQL_DELETA_CLIENTE = 'delete from cliente where id = %s'
SQL_CLIENTE_POR_ID = 'SELECT id, nomecliente, cpfcliente, enderecocliente, emailcliente from cliente where id = %s'
SQL_FUNCIONARIO_POR_ID = 'SELECT id, nome, senha from funcionario where id = %s'
SQL_ATUALIZA_CLIENTE = 'UPDATE cliente SET nomecliente=%s, cpfcliente=%s, enderecocliente=%s, emailcliente=%s where id = %s'
SQL_BUSCA_CLIENTES = 'SELECT id,nomecliente, cpfcliente, enderecocliente, emailcliente from cliente'
SQL_CRIA_CLIENTE = 'INSERT into cliente (nomecliente, cpfcliente, enderecocliente, emailcliente) values (%s, %s, %s, %s)'


class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()

        if (cliente.id):
            cursor.execute(SQL_ATUALIZA_CLIENTE, (cliente.nomecliente, cliente.cpfcliente, cliente.enderecocliente, cliente.emailcliente, cliente.id))
        else:
            cursor.execute(SQL_CRIA_CLIENTE, (cliente.nomecliente, cliente.cpfcliente, cliente.enderecocliente, cliente.emailcliente))
            cliente.id = cursor.lastrowid
        self.__db.connection.commit()
        return cliente

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CLIENTES)
        clientes = traduz_clientes(cursor.fetchall())
        return clientes

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CLIENTE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Cliente(tupla[1], tupla[2], tupla[3],tupla[4], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_CLIENTE, (id, ))
        self.__db.connection.commit()


class FuncionarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FUNCIONARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        funcionario = traduz_funcionario(dados) if dados else None
        return funcionario


def traduz_clientes(clientes):
    def cria_cliente_com_tupla(tupla):
        return Cliente(tupla[1], tupla[2], tupla[3],tupla[4], id=tupla[0])
    return list(map(cria_cliente_com_tupla, clientes))


def traduz_funcionario(tupla):
    return Funcionario(tupla[0], tupla[1], tupla[2])
