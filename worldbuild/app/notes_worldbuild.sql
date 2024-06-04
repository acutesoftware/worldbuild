/* notes_worldbuild.sql      written by Duncan Murray 31/5/2024

Tips on automating data collection from existing lists

*/

select * from ItemList where ID like 'plant%';

-- item_types
select ItemType, count(*) as num_recs from ItemList group by ItemType;


-- item_quality
select Quality, count(*) as num_recs from ItemList group by Quality;

-- healing things
select ID, quality, health from ItemList where health > 0 order by health desc, ID;

select * from o_env_plants;

select ID, WorldMesh from ItemList where ID like 'plant%'; 

-- plant_berry_Blueberry_01	StaticMesh'/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_01.Blueberry_01'

select plant_type, description, SM_plant_stage from o_env_plants where SM_plant_stage like '%Blueberry_01%';
-- blueberry	BlueBerry	(StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_01.Blueberry_01"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_02.Blueberry_02"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_03.Blueberry_03"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_04.Blueberry_04"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_05.Blueberry_05"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_06.Blueberry_06"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_07.Blueberry_07"',StaticMesh'"/Game/_DJM/Environment/PN_WildBerries/Meshes/Blueberry/Blueberry_08.Blueberry_08"')


-- mapping plants.csv to UE plants mesh list (doesnt fully work)

select pl.plant_type, pl.description, itm.ID, itm.WorldMesh,
pl.SM_plant_stage 
from o_env_plants pl, ItemList itm 
where itm.ID like 'plant%'
and replace(replace(pl.SM_plant_stage, '''', ''), '"', '') like '%' || replace(itm.WorldMesh, '''', '') || '%'  ;

select ID, 
replace(substr(WorldMesh, instr(WorldMesh, '.')+1, 88), '''','') as msh,
WorldMesh from ItemList where ID like 'plant%' order by id;


-- extract mapping list from inventory of plants and subset to make JOIN

DROP TABLE o_env_plant_mesh;

CREATE TABLE o_env_plant_mesh AS
select plant_type, plant_name, item_id, description, health, icon, worldMesh FROM ( 
select replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(
replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(ID, 'plant_', '') ,'_01', '')
 ,'_02', '') ,'_03', '') ,'_04', '') ,'_05', '') ,'_06', '') ,'_07', '') ,'_08', '') ,'_09', ''),'_10', '')
 ,'_11', ''),'_12', ''),'_13', ''),'_14', ''),'_15', ''),'_16', ''),'_17', ''),'_18', ''),'_19', ''),'_20', '')
as plant_name, ID as item_id, description, health, icon, 
case 
  when ID like 'plant_berry_%' then 'berry'
  when ID like 'plant_flower_%' then 'flower'
  when ID like 'plant_mushroom_%' then 'mushroom'
  when ID like 'plant_tree_%' then 'tree'
  when ID like 'plant_herb_%' then 'herb'
  when ID like 'plant_farm_%' then 'crop'
  when ID like 'plant_jungle_%' then 'jungle'
  else 'plant' end as plant_type,
  WorldMesh from ItemList where ID like 'plant%'
 ) order by 1,2,3;


select * from o_env_plant_mesh
 where plant_type = 'tree' and plant_name like '%ine%';

-- group into a list of plants o_env_plant -- plant_type, plant_name, plant_desc, num_meshes, grown_mesh, icon
select plant_type, plant_name, max(description) as plant_desc, 
count(*) as num_meshes, max(item_id) as grown_mesh, max(icon) as icon 
from o_env_plant_mesh
group by plant_type, plant_name
order by plant_type, plant_name;

SELECT tree_name, max(plant_desc) as tree_desc, sum(num_meshes) as num_meshes, max(grown_mesh) as grown_mesh, max(icon) as icon FROM (
select 
case when length(plant_name) > 10 then substr(plant_name, 6, instr(substr(plant_name, 7, 99), '_'))
else replace(plant_name, 'tree_', '') end as tree_name,
pl.* from o_env_plant pl where plant_type = 'tree'
) group by tree_name
order by tree_name;




