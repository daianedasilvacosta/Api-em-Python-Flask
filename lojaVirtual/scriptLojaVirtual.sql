
CREATE DATABASE lojaVirtual;
drop database lojavirtual;
USE lojavirtual;
CREATE TABLE jogo (
id int(11) NOT NULL AUTO_INCREMENT,
nome varchar(50) COLLATE utf8_bin NOT NULL,
categoria varchar(40) COLLATE utf8_bin NOT NULL,
console varchar(20) NOT NULL,
preco varchar(10) NOT NULL,
PRIMARY KEY (id)
) ;

CREATE TABLE usuario (
id varchar(8) COLLATE utf8_bin NOT NULL,
nome varchar(20) COLLATE utf8_bin NOT NULL,
senha varchar(8) COLLATE utf8_bin NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO lojavirtual.usuario (id, nome, senha) VALUES 
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas'),
            ('dai', 'Daiane', '123');
            
INSERT INTO lojavirtual.jogo (nome, categoria, console, preco) VALUES
            ('God of War 4', 'Ação', 'PS4', 'R$ 20,00'),
            ('NBA 2k18', 'Esporte', 'Xbox One', 'R$ 20,00'),
            ('Rayman Legends', 'Indie', 'PS4', 'R$ 20,00'),
            ('Super Mario RPG', 'RPG', 'SNES', 'R$ 20,00'),
            ('Super Mario Kart', 'Corrida', 'SNES', 'R$ 20,00'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS', 'R$ 20,00');