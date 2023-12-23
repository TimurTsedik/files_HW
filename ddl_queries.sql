CREATE TABLE IF NOT EXISTS genres (
    id serial PRIMARY KEY, 
    genre_name varchar(30) NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS musicians (
    id serial PRIMARY KEY, 
    musician_name varchar(100) NOT NULL UNIQUE, 
    musician_nick varchar(100) UNIQUE);
    
CREATE TABLE IF NOT EXISTS genres_musicians (
    genres_id integer REFERENCES genres(id), 
    musician_id integer REFERENCES musicians(id), 
    CONSTRAINT genres_musicians_pk PRIMARY KEY (genres_id, musician_id));    

CREATE TABLE IF NOT EXISTS albums (
    id serial PRIMARY KEY, 
    album_name varchar(100) NOT NULL, 
    album_year integer NOT NULL);
    
CREATE TABLE IF NOT EXISTS albums_musicians (
    albums_id integer REFERENCES albums(id), 
    musician_id integer REFERENCES musicians(id), 
    CONSTRAINT albums_musicians_pk PRIMARY KEY (albums_id, musician_id));

CREATE TABLE IF NOT EXISTS tracks (
    id serial PRIMARY KEY, 
    track_name varchar(100) NOT NULL, 
    track_duration integer NOT NULL, 
    album_id integer REFERENCES albums(id));

CREATE TABLE IF NOT EXISTS collections (
    id serial PRIMARY KEY, 
    collection_name varchar(100) NOT NULL, 
    collection_year integer NOT NULL);

CREATE TABLE IF NOT EXISTS tracks_collections (
    track_id integer REFERENCES tracks(id), 
    collection_id integer REFERENCES collections(id), 
    CONSTRAINT track_collection_pk PRIMARY KEY (track_id, collection_id));
