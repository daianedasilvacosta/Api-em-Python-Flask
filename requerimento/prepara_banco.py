import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `requerimento`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `requerimento` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `requerimento`;
    CREATE TABLE `pedido` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nomepedido` varchar(50) COLLATE utf8_bin NOT NULL,
      `categoriapedido` varchar(40) COLLATE utf8_bin NOT NULL,
      `descricaopedido` varchar(20) NOT NULL,
      `precopedido` varchar(10) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `usuario` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `nome` varchar(20) COLLATE utf8_bin NOT NULL,
      `senha` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`nome`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO equerimento.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
            ('dai', 'Daiane', '123')
      ])

cursor.execute('select * from requerimento.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo pedidos
cursor.executemany(
      'INSERT INTO requerimento.jogo (nomepedido, categoriapedido, descricaopedido, precopedido) VALUES (%s, %s, %s, %s)',
      [
            ('God of War 4', 'Ação', 'PS4', 'R$ 20,00'),
            ('NBA 2k18', 'Esporte', 'Xbox One', 'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'PS4', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'SNES', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'SNES', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS', 'R$ 20,00'),
      ])

cursor.execute('select * from requerimento.pedido')
print(' -------------  Pedidos:  -------------')
for pedido in cursor.fetchall():
    print(pedido[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()