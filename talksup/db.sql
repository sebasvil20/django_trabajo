CREATE DATABASE talksupdb;

USE talksupdb;

CREATE TABLE podcasts
(
    podcast_id     VARCHAR(36)  DEFAULT (UUID()) PRIMARY KEY,
    name           varchar(100) NOT NULL,
    description    varchar(800) NOT NULL,
    cover_pic_url  varchar(1000),
    trailer_url    varchar(1000),
    rating         float DEFAULT 0,
    total_episodes int,
    total_length   varchar(20),
    release_date   date
);

INSERT INTO podcasts(name, description, cover_pic_url, trailer_url, total_episodes, total_length, release_date)
VALUES ('Colombia Paranormal', 'Investigaciones, audios, noticias y todo un mundo visto desde la fantasía, el terror,
        el cielo y el infierno. Soy Cristian Díaz un joven colombiano que ama todo lo paranormal y quiero que ustedes 
        me acompañen en este viaje extra dimensional y escuche los horrores que nadie se atreve a escuchar.',
        'https://i.scdn.co/image/f87fb665cf17b6332cd51c8f3076e5613cbf2d08',
        'https://open.spotify.com/episode/5pJJYf5rxQIWYTnBsf75tg?si=tPDe2CT3Su-sGI9XV7lZJA', 75, '15h', '2020-06-01');

INSERT INTO podcasts(name, description, cover_pic_url, trailer_url, total_episodes, total_length, release_date)
VALUES ('Filosofía, Psicología e Historias varias',
        'Relatos breves de filosofía, Psicología e Historias varias, con biografías y algunas reflexiones, leyendas y fantasías.',
        'https://i.scdn.co/image/2bc2a9e504540994ea5bfbe55e8c358c8db5c96b',
        'https://open.spotify.com/episode/4sv9Pu5rH4hgr6bBZ4i5s0?si=vVnRH4UZTH2oi4fdSbzIRQ', 177, '36h','2020-03-01');


INSERT INTO podcasts(name, description, cover_pic_url, trailer_url, total_episodes, total_length, release_date)
VALUES ('Psicologia al desnudo',
        'En este podcast hablamos de emociones. De tus mecanismos internos: ¿Por qué hacés lo que hacés? ¿Por qué no podés expresar ciertas emociones y otras sí? ¿Por qué te sentís mal a veces? ¿Por qué hay cosas que te angustian, que te generan miedo, nostalgia, o que te dan placer? ¿Cómo regular tus emociones para sentirte equilibrado La gestión emocional es la CLAVE para vivir una vida con sentido. ¡Y está en tus manos aprenderlo! ¿La puerta de entrada a este proceso? Psicología al Desnudo',
         'https://i.scdn.co/image/ab6765630000ba8a412808f7b7b39ba17f687936', '', 71, '27h', '2020-06-20');


INSERT INTO podcasts(name, description, cover_pic_url, trailer_url, total_episodes, total_length, release_date)
VALUES ('Sospechosamente light',
        'Los han llamado inmaduros, malcrecidos, adolescentes eternos y no les choca, el tiempo perdido los trajo justo donde no querían al punto donde están muy jóvenes para morir pero muy viejos para vivir.',
         'https://i.scdn.co/image/f2f2024adc4de90952b05e64c80a16cbd3cf92b5', '', 50, '35h', '2020-03-01');