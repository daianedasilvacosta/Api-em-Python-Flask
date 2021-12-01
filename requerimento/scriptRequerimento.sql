CREATE DATABASE requerimento;
drop database requerimento;
USE requerimento;
CREATE TABLE pedido (
id int(11) NOT NULL AUTO_INCREMENT,
nomepedido varchar(50) COLLATE utf8_bin NOT NULL,
categoriapedido varchar(40) COLLATE utf8_bin NOT NULL,
descricaopedido varchar(20) NOT NULL,
precopedido varchar(10) NOT NULL,
PRIMARY KEY (id)
) ;

CREATE TABLE usuario (
id varchar(8) COLLATE utf8_bin NOT NULL,
nome varchar(20) COLLATE utf8_bin NOT NULL,
senha varchar(8) COLLATE utf8_bin NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO requerimento.usuario (id, nome, senha) VALUES 
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas'),
            ('dai', 'Daiane', '123');
            
INSERT INTO requerimento.pedido (nomepedido, categoriapedido, descricaopedido, precopedido) VALUES
            ('God of War 4', 'Ação', 'PS4', 'R$ 20,00'),
            ('NBA 2k18', 'Esporte', 'Xbox One', 'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'PS4', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'SNES', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'SNES', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS', 'R$ 20,00');