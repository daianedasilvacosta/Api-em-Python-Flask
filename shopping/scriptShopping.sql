CREATE DATABASE shopping;
drop database shopping;
USE shopping;
CREATE TABLE cliente (
id int(11) NOT NULL AUTO_INCREMENT,
nomecliente varchar(50) COLLATE utf8_bin NOT NULL,
cpfcliente varchar(11) COLLATE utf8_bin NOT NULL,
enderecocliente varchar(100) NOT NULL,
emailcliente varchar(40) NOT NULL,
PRIMARY KEY (id)
) ;

CREATE TABLE funcionario (
id varchar(8) COLLATE utf8_bin NOT NULL,
nome varchar(20) COLLATE utf8_bin NOT NULL,
senha varchar(8) COLLATE utf8_bin NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO shopping.funcionario (id, nome, senha) VALUES 
            ('luana', 'Luana Marques', 'flask'),
            ('nick', 'Nicolas', '7a1'),
            ('Lu', 'Lucas', 'vegas'),
            ('dai', 'Daiane', '123');
            
INSERT INTO shopping.cliente (nomecliente, cpfcliente, enderecocliente, emailcliente) VALUES
            ('Camila Dias', '12345678901', 'rua das flores 123', 'camila.dias@gmail.com'),
            ('Claudio Dias', '09876543212', 'rua das flores 123', 'cladio.dias@gmail.com'),
            ('Karen Dias', '12345679876', 'rua das flores 123', 'karen.dias@gmail.com'),
            ('Sandra Dias', '12345676543', 'rua das flores 123', 'sandra.dias@gmail.com'),
            ('Olivia Dias', '09876543210', 'rua das flores 123', 'olivia.dias@gmail.com');