#!/usr/bin/python3
# -*- coding: utf-8 -*-
# create_worldbuild_database.py
"""
Creates a full worldbuild database for development.

Imports existing tables from CSV.


"""
import os
import sys
import glob
import sqlite3
import if_sqllite
import pandas as pd
import config_app as mod_cfg

db_file = mod_cfg.db_file
csv_folder = mod_cfg.fldr_data

def_lp_tables = [ # [table_name, description, grain_cols, col_list, cols_INT, cols_REAL, cols_BLOB]
   ['o_env_plant_mesh', 'Plant stages of growth ', 'item_id', 'plant_type, plant_name, item_id, description, health, icon, worldMesh', [],  [], []],
   ['o_env_plant', 'Plant List', 'plant_name', 'plant_type, plant_name, plant_desc, num_meshes, grown_mesh, icon', [],  [], []],

]

def_lp_jobs = [ # proj_id, job_num, job_id, details
    ['FL', 1, 'LOAD_CSV', 'Load Raw CSV Files'],

]


def_lp_job_steps = [ # job_id, job_num, step_num, job_type, details, sql_to_run
#    [ 'LOAD_APPS', 0, 1, 'CSV', r'N:\duncan\LifePIM_Data\DATA\notes\_data\australian_public_holidays_raw.csv', '', 'Load raw dates ', '', ''],

]



def main():

    # define CSV files to be loaded for world build
    res = get_list_of_csv_files(csv_folder)

    for r in res:
        print(str(r))
    
    print(str(len(res)) + ' csv files to be loaded')        
    def_lp_job_steps = [] # job_id, job_num, step_num, job_type, details, sql_to_run
    for fnum, fname in enumerate(res):
        def_lp_job_steps.append([1, 'LOAD_CSV',fnum, 'CSV', fname, '', 'Load CSV file', '', ''])
  
  

    # REBUILD DATABASE
    try:
        os.remove(db_file)
    except:
        pass
    if_sqllite.create_database(db_file)
    conn = sqlite3.connect(db_file)
    if_sqllite.init_metadata_tables(conn)




    # create tables

    for tbl in def_lp_tables:
        if_sqllite.create_table_from_definition(conn, tbl)

    if_sqllite.lg(conn, if_sqllite.LOG_DATA, 'defining jobs')
    for job in def_lp_jobs:
        if_sqllite.job_create(conn, job[0], job[1], job[2], job[3])

    for step in def_lp_job_steps:  # job_id, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run
        print('adding step = ' + str(step))
        if_sqllite.job_add_step(conn, step[0],step[1],step[2],step[3],step[4], step[5], step[6], step[7], step[8])
        if_sqllite.run_job_step(conn, step)


    populate_sample_prod_data(conn)

def get_list_of_csv_files(fldr):
    return glob.glob(fldr + os.sep + '**' + os.sep + '*.csv', recursive=True)


def populate_sample_prod_data(conn):
    sql = []


    sql.append("""INSERT INTO o_env_plant_mesh (plant_type, plant_name, item_id, description, health, icon, worldMesh)
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
""")

    sql.append("""INSERT INTO o_env_plant (plant_type, plant_name, plant_desc, num_meshes, grown_mesh, icon)    
select plant_type, plant_name, max(description) as plant_desc, 
count(*) as num_meshes, max(item_id) as grown_mesh, max(icon) as icon 
from o_env_plant_mesh
group by plant_type, plant_name
order by plant_type, plant_name
""")


    sql.append("""INSERT INTO o_env_tree (tree_name, tree_desc, num_meshes, grown_mesh, icon)
SELECT tree_name, tree_desc, num_meshes, grown_mesh, icon FROM (
SELECT tree_name, max(plant_desc) as tree_desc, sum(num_meshes) as num_meshes, max(grown_mesh) as grown_mesh, max(icon) as icon FROM (
select 
case when length(plant_name) > 10 then substr(plant_name, 6, instr(substr(plant_name, 7, 99), '_'))
else replace(plant_name, 'tree_', '') end as tree_name,
pl.* from o_env_plant pl where plant_type = 'tree'
) group by tree_name
) order by tree_name
""")
    
    # Build Views
    #sql.append("DROP VIEW U_ITEM_RECIPE")

    sql.append("""CREATE VIEW U_ITEM_RECIPE AS
select itm.ID, itm.Name, itm.Description, rec.recipe_name, rec.num_produced_per_craft , GROUP_CONCAT(ing.item_id) as rec_ingred --CASE WHEN ing.item_id = itm.ID then 'Y' else 'N' end as used_as_ingred
from ItemList itm left join DT_craft_recipe rec on itm.ID = rec.recipe_id
left join DT_craft_recipe_ingredients ing on ing.recipe_id = itm.ID
group by itm.ID
""")

    # not needed as we build from scratch sql.append("DROP VIEW U_ITEM_RECIPE_INGRED")

    sql.append("""CREATE VIEW U_ITEM_RECIPE_INGRED AS
select itm.ID, itm.Name, ing.recipe_id, item_id as ingred_name, count(*) as num_recipes,
GROUP_CONCAT(ing.recipe_id) as recipes_used --CASE WHEN ing.item_id = itm.ID then 'Y' else 'N' end as used_as_ingred
from ItemList itm left join DT_craft_recipe_ingredients ing on ing.item_id = itm.ID
group by itm.ID
""")


    sql.append("""CREATE VIEW U_MAP_ITEMS_TO_COLOURS AS
select 'colour.red' as tag, id from Itemlist where description like '%Red %' and description not like 'Covered %' and description not like 'Battered %' UNION ALL
select 'colour.green' as tag, id from Itemlist where description like '%Green %' UNION ALL
select 'colour.yellow' as tag, id from Itemlist where description like '%Yellow %' UNION ALL
select 'colour.orange' as tag, id from Itemlist where description like '%Orange %' UNION ALL
select 'colour.blue' as tag, id from Itemlist where description like '%Blue %' UNION ALL
select 'colour.purple' as tag, id from Itemlist where description like '%Purple %' UNION ALL
select 'colour.pink' as tag, id from Itemlist where description like '%Pink %' UNION ALL
select 'colour.white' as tag, id from Itemlist where description like '%White %' UNION ALL
select 'colour.black' as tag, id from Itemlist where description like '%Black %'
""")
    

    sql.append("""CREATE VIEW U_MAP_ITEMS_TO_types AS
select 'item.type.fish' as tag, 'Fish - some edible, all can be bait' as description, id from Itemlist where id like 'fish_%' and substr(id, 5,1) = '_' and id not like '%frog%' UNION ALL
select 'item.type.clothes' as tag, 'Clothes can be worn by Player or NPC USC Characters' as description, id from Itemlist  where WorldMesh like '%/UCS/Cloth%' or WorldMesh like '%z_djm_items/cloth%' UNION ALL 
select 'item.type.tool' as tag, 'Tools to make things' as description, id from Itemlist where id like 'tool_%' UNION ALL 
select 'item.type.food' as tag, 'Edible things' as description, id from Itemlist where id like 'food_%' UNION ALL 
select 'item.type.furniture' as tag, 'Furniture for your house' as description, id from Itemlist where id like 'furn_%' UNION ALL 
select 'loot.plant.harvest' as tag, 'Harvestable Plants' as description, id from Itemlist where id like 'plant_%' and (description like '%herb%' or description like '%harv%' or description like '%berry%' or description like '%mustard%' or description like '%(Corn%') UNION ALL
select 'item.container.jar' as tag, 'Jar for Storage' as description, id from Itemlist where id like 'jar_%' or id like 'kitchen_jar%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'item.crockery.plate' as tag, 'Plate for serving' as description, id from Itemlist where id like 'kitchen_plat%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'item.crockery.bowl' as tag, 'Bowl for serving' as description, id from Itemlist where id like 'kitchen_bowl%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'mat.wood' as tag, 'Made of Wood' as description, id from Itemlist where  id like '%wood%' or description like '%tree%' and id not like '%flower%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'mat.stone' as tag, 'Made of Stone' as description, id from Itemlist where  id like '%stone%' or description like '%rock%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'mat.organic' as tag, 'Plants, trees, organic matter' as description, id from Itemlist where  id like 'plant%' or id like 'Food_Fruit%' or id like 'Food_Veg%' UNION ALL -- select 'item.container.chest' as tag, 'Chest for Storage' as description, id from Itemlist where id like 'chest_%' UNION ALL 
select 'mat.ore' as tag, 'Ore to be mined and smelted' as description, id from Itemlist where id like 'ore_%' UNION ALL 
select 'ingred.flour' as tag, 'Flour for cooking' as description, id from Itemlist where id like '%flour%' UNION ALL
select 'ingred.milk' as tag, 'Milk for cooking' as description, id from Itemlist where id like '%milk%' or id like 'food_cream%' UNION ALL
select 'ingred.egg' as tag, 'Eggs for cooking' as description, id from Itemlist where id like '%egg%' UNION ALL
select 'ingred.butter' as tag, 'Butter for cooking' as description, id from Itemlist where id like '%butter%' or id like 'food_oil%' UNION ALL
select 'ingred.bread' as tag, 'Bread for sandwiches' as description, id from Itemlist where id like '%food_bread%' and description not like '%Pizza%' and description not like '%Muffin%' and description not like '%Chocolate%' and description not like '%Brownie%' and description not like '%Biscuit%' UNION ALL
select 'ingred.vege' as tag, 'Vegetables for cooking' as description, id from Itemlist where id like '%Food_Veg%' UNION ALL
select 'ingred.fruit' as tag, 'Fruit for eating / cooking' as description, id from Itemlist where id like '%Food_Fruit%' UNION ALL
select 'ingred.yeast' as tag, 'Yeast for baking' as description, id from Itemlist where id like '%Food_yeast%' UNION ALL
select 'ingred.cheese' as tag, 'Cheese' as description, id from Itemlist where id like '%Food_cheese%' UNION ALL
select 'ingred.sweet' as tag, 'Sweetening ingredients' as description, id from Itemlist where id like '%Food_jam%' or id like 'food_sugar%' or id like '%honey%' or id like '%food_sprinkles%' UNION ALL
select 'ingred.seasoning' as tag, 'Seasoning ingredients for cooking' as description, id from Itemlist where id like '%Food_salt%' or id like 'food_vinegar%' or id like 'food_sauce%' or id like 'food_cream_sour%' or id like 'food_herb%'
""")

  


    # now run all the SQL commands
    for s_num, s in enumerate(sql):
        step = [ 'WB', 3, 10+s_num, 'UPD', '', 'table_name', 'build worldbuild', s, '']
        if_sqllite.job_add_step(conn, step[0],step[1],step[2],step[3],step[4], step[5], step[6], step[7], step[8])
        if_sqllite.run_job_step(conn, step)




if __name__ == '__main__':
    main()
    
