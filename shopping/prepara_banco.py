import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `shopping';")
#conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `shopping` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `shopping`;
    CREATE TABLE `cliente` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nomecliente` varchar(50) COLLATE utf8_bin NOT NULL,
      `cpfcliente` varchar(40) COLLATE utf8_bin NOT NULL,
      `enderecocliente` varchar(20) NOT NULL,
      `emailcliente` varchar(10) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `funcionario` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `nome` varchar(20) COLLATE utf8_bin NOT NULL,
      `senha` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`nome`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo funcionarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO shopping.funcionario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from shopping.funcionario')
print(' -------------  Funcionario:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo clientes
cursor.executemany(
      'INSERT INTO shopping.cliente (nomecliente, cpfcliente, enderecocliente, emailcliente) VALUES (%s, %s, %s, %s)',
      [
            ('Camila Dias', '12345678901', 'rua das flores 123', 'camila.dias@gmail.com'),
            ('Claudio Dias', '09876543212', 'rua das flores 123', 'cladio.dias@gmail.com'),
            ('Karen Dias', '12345679876', 'rua das flores 123', 'karen.dias@gmail.com'),
            ('Sandra Dias', '12345676543', 'rua das flores 123', 'sandra.dias@gmail.com'),
            ('Olivia Dias', '09876543210', 'rua das flores 123', 'olivia.dias@gmail.com')
      ])

cursor.execute('select * from shopping.cliente')
print(' -------------  Cliente:  -------------')
for cliente in cursor.fetchall():
    print(cliente[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()