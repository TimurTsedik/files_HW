#Доработка
#1
select t.track_name, t.track_duration 
from tracks t 
where t.track_duration =(select max(track_duration) from tracks)

#3
select collection_name 
from collections c 
where c.collection_year between 2018 and 2020
#7
select count(t.track_name)  
from tracks t 
join tracks_collections tc on t.id = tc.track_id 
join collections c on c.id = tc.collection_id 
where c.collection_year between 2019 and 2020 
#9
select m.musician_name 
from musicians m 
where m.id not in (select m.id 
from musicians m 
join albums_musicians am on m.id = am.musician_id 
join albums a on a.id = am.albums_id 
where a.album_year =2020)
#10
select distinct c.collection_name  
from collections c 
join tracks_collections tc on c.id = tc.collection_id 
join tracks t on tc.track_id = t.id 
join albums a on t.album_id = a.id 
join albums_musicians am on a.id = am.albums_id 
join musicians m on m.id = am.musician_id 
where m.musician_name = 'Angus Young'
#11
select a.album_name as name, count(gm.genres_id)
from albums a 
join albums_musicians am on a.id = am.albums_id 
join musicians m on am.musician_id = m.id 
join genres_musicians gm on m.id = gm.musician_id 
group by a.album_name
having count(gm.genres_id) > 1
#14
select a.album_name as name, count(t.id) as cnt
from albums a 
join tracks t on a.id = t.album_id 
group by a.album_name
having count(t.id) = (select min(cnt)
from (select a.album_name, count(t.id) as cnt
from albums a 
join tracks t on a.id = t.album_id 
group by a.album_name))
