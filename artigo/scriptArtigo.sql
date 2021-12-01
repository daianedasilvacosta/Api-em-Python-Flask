CREATE DATABASE artigo;
drop database artigo;
USE artigo;
CREATE TABLE produto (
id int(11) NOT NULL AUTO_INCREMENT,
nomeproduto varchar(50) COLLATE utf8_bin NOT NULL,
descricaoproduto varchar(40) COLLATE utf8_bin NOT NULL,
precoproduto varchar(10) NOT NULL,
PRIMARY KEY (id)
) ;

CREATE TABLE usuario (
id varchar(8) COLLATE utf8_bin NOT NULL,
nome varchar(20) COLLATE utf8_bin NOT NULL,
senha varchar(8) COLLATE utf8_bin NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO artigo.usuario (id, nome, senha) VALUES 
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas'),
            ('dai', 'Daiane', '123');
            
INSERT INTO artigo.produto (nomeproduto, descricaoproduto, precoproduto) VALUES
            ('God of War 4', 'Ação', 'R$ 20,00'),
            ('NBA 2k18', 'Esporte',  'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia','R$ 20,00');