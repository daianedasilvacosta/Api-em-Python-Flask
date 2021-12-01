import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `artigo`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `artigo` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `artigo`;
    CREATE TABLE `produto` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nomeproduto` varchar(50) COLLATE utf8_bin NOT NULL,
      `descricaoproduto` varchar(40) COLLATE utf8_bin NOT NULL,
      `precoproduto varchar(10) NOT NULL,
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
      'INSERT INTO artigo.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas'),
            ('dai', 'Daiane', '123')
      ])

cursor.execute('select * from artigo.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo produtos
cursor.executemany(
      'INSERT INTO artigo.produto (nomeproduto, descricaoproduto, precoproduto) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Ação' 'R$ 20,00'),
            ('NBA 2k18', 'Esporte', 'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia', 'R$ 20,00'),
      ])

cursor.execute('select * from artigo.produto')
print(' -------------  Produtos:  -------------')
for produto in cursor.fetchall():
    print(produto[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()