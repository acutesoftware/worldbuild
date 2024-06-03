/* notes_worldbuild.sql      written by Duncan Murray 31/5/2024

Tips on automating data collection from existing lists

*/

select * from ItemList;

-- item_types
select ItemType, count(*) as num_recs from ItemList group by ItemType;


-- item_quality
select Quality, count(*) as num_recs from ItemList group by Quality;

-- healing things
select ID, quality, health from ItemList where health > 0 order by health desc, ID;






