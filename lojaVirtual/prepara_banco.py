import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `lojavirtual`;")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `lojavirtual` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `lojavirtual`;
    CREATE TABLE `jogo` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      `preco` varchar(10) NOT NULL,
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
      'INSERT INTO lojavirtual.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from lojavirtual.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO lojavirtual.jogo (nome, categoria, console, preco) VALUES (%s, %s, %s, %s)',
      [
            ('God of War 4', 'Ação', 'PS4', 'R$ 20,00'),
            ('NBA 2k18', 'Esporte', 'Xbox One', 'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'PS4', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'SNES', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'SNES', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS', 'R$ 20,00'),
      ])

cursor.execute('select * from lojavirtual.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()