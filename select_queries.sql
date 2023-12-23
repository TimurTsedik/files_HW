#Задание 2

select track_name, track_duration from tracks
order by track_duration desc 
limit 1

select track_name , round(track_duration/60, 1) as minutes
from tracks t 
where track_duration /60 >=3.5

select collection_name 
from collections c 
where c.collection_year >=2018 and c.collection_year <=2020

select m.musician_name 
from musicians m 
where m.musician_name not like '% %'

select t.track_name 
from tracks t 
where t.track_name like '%my%' or t.track_name like '%мой%'

#Задание 3

select g.genre_name, count(gm.musician_id) 
from genres g 
join genres_musicians gm on g.id = gm.genres_id 
group by g.genre_name 

select count(t.track_name)  
from tracks t 
join tracks_collections tc on t.id = tc.track_id 
join collections c on c.id = tc.collection_id 
where c.collection_year >= 2019 and c.collection_year >= 2020 

select a.album_name, avg(t.track_duration)
from albums a 
join tracks t on a.id = t.album_id 
group by a.album_name 

select m.musician_name 
from musicians m 
join albums_musicians am on m.id = am.musician_id 
join albums a on a.id = am.albums_id 
where a.album_year <> 2020

select c.collection_name  
from collections c 
join tracks_collections tc on c.id = tc.collection_id 
join tracks t on tc.track_id = t.id 
join albums a on t.album_id = a.id 
join albums_musicians am on a.id = am.albums_id 
join musicians m on m.id = am.musician_id 
where m.musician_name = 'Angus Young'
group by c.collection_name  

#Задание 4

select name
from  (select a.album_name as name, count(gm.genres_id) as cnt
from albums a 
join albums_musicians am on a.id = am.albums_id 
join musicians m on am.musician_id = m.id 
join genres_musicians gm on m.id = gm.musician_id 
group by a.album_name)
where cnt > 1

select name
from 
(select t.track_name as name, tc.collection_id as id
from tracks t 
left join tracks_collections tc on t.id = tc.track_id)
where id is null

select m.musician_name, t.track_duration 
from musicians m
join albums_musicians am on m.id = am.musician_id 
join albums a on a.id = am.albums_id 
join tracks t on a.id = t.album_id 
where t.track_duration = (select min(t.track_duration) 
from tracks t)

select name
from (select a.album_name as name, count(t.id) as cnt
from albums a 
join tracks t on a.id = t.album_id 
group by a.album_name)
where cnt = (select min(cnt)
from (select a.album_name, count(t.id) as cnt
from albums a 
join tracks t on a.id = t.album_id 
group by a.album_name))
