insert into genres 
(genre_name)
values ('Jazz');
insert into genres 
(genre_name)
values ('Rock');
insert into genres 
(genre_name)
values ('Pop');
insert into genres 
(genre_name)
values ('House');

insert into musicians  
(musician_name, musician_nick)
values ('Louis Armstrong', 'Lui');

insert into musicians  
(musician_name)
values ('Angus Young');

insert into musicians  
(musician_name)
values ('Shakira');

insert into musicians  
(musician_name)
values ('David Guetta');

insert into genres_musicians
(genres_id, musician_id)
values (1, 6);
insert into genres_musicians
(genres_id, musician_id)
values (2, 7);
insert into genres_musicians
(genres_id, musician_id)
values (3, 8);
insert into genres_musicians
(genres_id, musician_id)
values (4, 9);

insert into albums  
(album_name, album_year)
values ('Highway to hell', '1979');
insert into albums  
(album_name, album_year)
values ('What a wonderfull world', '1968');
insert into albums  
(album_name, album_year)
values ('Magia', '1991');
insert into albums  
(album_name, album_year)
values ('Nothing but beat', '2011');

insert into albums_musicians
(albums_id, musician_id)
values (1, 7);
insert into albums_musicians
(albums_id, musician_id)
values (2, 6);
insert into albums_musicians
(albums_id, musician_id)
values (3, 8);
insert into albums_musicians
(albums_id, musician_id)
values (4, 9);

insert into tracks 
(track_name, track_duration, album_id)
values ('Highway to hell', 270, 1);
insert into tracks 
(track_name, track_duration, album_id)
values ('Girls got rhythm', 305, 1);
insert into tracks 
(track_name, track_duration, album_id)
values ('What a wonderfull world', 345, 2);
insert into tracks 
(track_name, track_duration, album_id)
values ('Suenos', 255, 3);
insert into tracks 
(track_name, track_duration, album_id)
values ('Sweat', 270, 4);
insert into tracks 
(track_name, track_duration, album_id)
values ('Without you', 270, 4);
insert into tracks 
(track_name, track_duration, album_id)
values ('Turn me on', 330, 4);

insert into collections 
(collection_name, collection_year)
values ('The best of AC/DC', 2005);
insert into collections 
(collection_name, collection_year)
values ('The best of Luios Armstrong', 2011);
insert into collections 
(collection_name, collection_year)
values ('The best of Shakira', 2015);
insert into collections 
(collection_name, collection_year)
values ('The best of David Guetta', 2020);

insert into tracks_collections
(track_id, collection_id)
values (1, 2);
insert into tracks_collections
(track_id, collection_id)
values (2, 2);
insert into tracks_collections
(track_id, collection_id)
values (3, 3);
insert into tracks_collections
(track_id, collection_id)
values (4, 4);
insert into tracks_collections
(track_id, collection_id)
values (5, 5);
insert into tracks_collections
(track_id, collection_id)
values (6, 5);
