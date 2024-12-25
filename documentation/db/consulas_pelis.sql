




CREATE DATABASE app_movies;

CREATE TABLE usuarios(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100),
	correo VARCHAR(100),
	contrasena VARCHAR(100),
	tipo VARCHAR(1),
	url_perfil VARCHAR(255)
	
)

CREATE TABLE Comentarios
(
	id SERIAL PRIMARY KEY,
	id_usuario integer,
	id_pelicula integer,
	descripcion varchar(255),
	fecha DATE
)

DROP TABLE comentarios;


CREATE TABLE Peliculas
(
	id SERIAL PRIMARY KEY,
	titulo varchar(255),
	descripcion varchar(255),
	fecha date,
	calificacion int,
	url_fondo varchar(255),
	url_portada varchar(255),
	url_video varchar(255),
	tipo varchar(1)
)

INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('Smallville','La vida de clack ken en smallville','02/12/2024',2,'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2017/05/smallville-como-acabo-serie-tv-joven-superman.jpg',
'https://static.cinepolis.com/resources/mx/movies/posters/414x603/48461-436544-20241217084917.jpg','https://www.youtube.com/watch?v=jYGUYAaqmlU&t=21s&ab_channel=DisneyStudiosLA',
'p');

INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('Troya','Pelicula que cuenta la vida del heroe griego aquilles','23/12/2024',1,'https://i.blogs.es/0ae59c/troya/1366_2000.jpeg',
'https://pics.filmaffinity.com/Troya-263366287-large.jpg','https://www.youtube.com/watch?v=znTLzRJimeY&ab_channel=RottenTomatoesClassicTrailers',
's');

INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('La Ciudad del Pecado','Sin City es una serie de historietas creadas por el guionista y dibujante Frank Miller. Todas se desarrollan en la ciudad ficticia de Basin City','23/12/2024',0,'https://reactormag.com/wp-content/uploads/2019/05/SinCityDame01.jpg',
'https://pics.filmaffinity.com/Sin_City_Ciudad_del_pecado-677469240-large.jpg','https://www.youtube.com/watch?v=aOsObc1QrgY&ab_channel=Tr%C3%A1ilersconDoblajeEspa%C3%B1olLatinobySoldierBoy',
'p');



INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('Perfume historia de un asesino','Ambientada en Francia en el siglo XVIII, poco antes de la Revolución francesa','14/12/2024','1','https://www.mundopeliculas.tv/wp-content/uploads/2018/12/el-perfume-1024x576.jpg',
'https://es.web.img3.acsta.net/medias/nmedia/18/67/53/01/20064123.jpg','https://www.youtube.com/watch?v=_-qv0EnGhJU&ab_channel=RottenTomatoesClassicTrailers','p');


INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('Dragon Ball Daima','serie creada por akira torillama','28/12/2024','1','https://areajugones.sport.es/wp-content/uploads/2024/12/dragon-ball-daima-ep-12.jpg',
'https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=480,height=720/catalog/crunchyroll/298acc932735d9a731ea39a3db6a613c.jpg','https://www.youtube.com/watch?v=oIwNHuu7yCM&ab_channel=Cin%C3%A9polis','s');


INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('Silicon Valley','serie sobre programadores','23/12/2024','1','https://culturaca.com/wp-content/uploads/2017/05/silicon-valley.jpg',
'https://m.media-amazon.com/images/I/814uptxbBOL._AC_UF894,1000_QL80_.jpg','https://www.youtube.com/watch?v=4eMYiDaY3-Q&ab_channel=ChannelofInterest','s');

INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('The Play List','serie sobre la creacion de spotyfly','23/12/2024','1','https://occ-0-8407-1361.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABZwG8o8R5MEBU9GQ5eGNFgAtmt6EWVF2mskogvPYVYgGW0ARtB7LIQUJENgo47cATFF7o40_MELxCQ97DpaBNW-oy3m0MziW55OK.jpg?r=74f',
'https://m.media-amazon.com/images/M/MV5BNDExODQ3OGMtOWVlMC00NjgzLWE4YmEtNzY0MGQ2ZjM2NzRhXkEyXkFqcGc@._V1_.jpg','https://www.youtube.com/watch?v=VtvfbGRDJbY&ab_channel=Netflix','s');






SELECT * FROM Peliculas WHERE tipo='p'

SELECT * FROM Peliculas ORDER BY fecha DESC LIMIT 8;

SELECT * FROM Peliculas ORDER BY calificacion DESC LIMIT 8;

INSERT INTO usuarios(nombre, correo, contrasena, tipo, url_perfil) VALUES('Manuel Luna', 'detodopcs@hotmail.com', 'nosferatus123', 'm', 'https://w7.pngwing.com/pngs/825/857/png-transparent-computer-icons-user-profile-user-silhouette-apple-icon-image-format-user-profile-thumbnail.png' )


UPDATE Peliculas SET Url_video='https://www.youtube.com/embed/_-qv0EnGhJU?si=d0wwc0AvhwizZ856' WHERE id=5;

UPDATE Peliculas SET Url_portada='https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=contain,format=auto,quality=85,width=480,height=720/catalog/crunchyroll/298acc932735d9a731ea39a3db6a613c.jpg' WHERE id=13;


SELECT COUNT(*) AS total_usuarios FROM usuarios WHERE correo='detodopcs@hotmail.com' AND contrasena='salmo150';



INSERT INTO Comentarios(id_usuario, id_pelicula, descripcion, fecha)VALUES(8, 4, 'esta muy pecadora esta peli', '23/12/2024');


SELECT * FROM Peliculas;

TRUNCATE Peliculas;




SELECT c.*, u.nombre, p.titulo FROM Comentarios c INNER JOIN usuarios u ON c.id_usuario = u.id INNER JOIN Peliculas p ON c.id_pelicula = p.id;

SELECT * FROM usuarios;

TRUNCATE TABLE usuarios;

SELECT * FROM Comentarios;

SELECT id FROM usuarios WHERE correo = 'juanlimones@gmail.com' AND contrasena ='salmo150';
SELECT id FROM usuarios WHERE correo = 'detodopcs@hotmail.com' AND contrasena = 'salmo150';

