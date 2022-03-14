#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ai_goals.py

import os 
import sys
import random 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)

npc_file = 'random_npc.csv'
goals = ['money', 'family','fun', 'learn']


plans_money = ['work','business','forage', 'craft']
plans_love = ['family','friends','charity']
plans_fun = ['family', 'friends','chat','pub', 'fish', 'games']
plans_learn = ['work','craft','study', 'train', 'craft']

"""
['npc_name', 'age', 'location', 'born', 'attitude', 'profession',  'childhood']
"Jennie","16","doctade","Elkite","-1","cook","privileged",
"Gabriela","20","draeton","Isakite","2","cook","poor",
"Denise","43","draeton","Wollest","0","angler","poor",
"Isabis","31","doctade","Isased","-2","vet","normal",

actions = [
{"name":"walk", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.08,"reward_item":"herb", "exp_gain":0.0},
{"name":"run", "cost_energy":0.05, "cost_gold":0, "reward_chance":0.0002,"reward_item":"herb", "exp_gain":0.0},
{"name":"rest", "cost_energy":-1, "cost_gold":0, "reward_chance":0.09,"reward_item":"recipe", "exp_gain":0.0},
{"name":"mining", "cost_energy":1, "cost_gold":0, "reward_chance":0.9,"reward_item":"stone", "exp_gain":0.1},
{"name":"herb", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"herb", "exp_gain":0.1},
{"name":"think", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
{"name":"study", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
{"name":"tinker", "cost_energy":0.01, "cost_gold":0, "reward_chance":0.5,"reward_item":"recipe", "exp_gain":0.1},
]

"""



def main():
    print('Generating Goals, Plans and Actions for NPCs from ' + npc_file)
    with open(npc_file, 'r') as fip:
        for line_num, line in enumerate(fip):
            if line_num > 0:
                npc = extract_npc_raw_data(line)
                goals, plans = assign_goals(npc)
                display_npc_goals(npc, goals, plans)
                

def display_npc_goals(npc, goals, plans):
    print(npc['nme'] + ' goals = ' + str(goals))
    for plan in plans:
        print('plan = ' + str(plan))

def extract_npc_raw_data(line):
    op = {}
    npc = line.split('","')
    npc[0] = npc[0].strip('"')
    op['nme'] = npc[0].strip('"')
    op['age'] = npc[1]
    op['location'] = npc[2]
    op['born'] = npc[3]
    op['attitude'] = npc[4]
    op['profession'] = npc[5]
    op['childhood'] = npc[6]
    return op #, nme, age, location, born, attitude, profession, childhood
   



def assign_goals(npc):
    """
    all NPC's have ALL goals but are weighted from 0 to 10 depending
    on how important they are to them (based on random + upbringing).

    plans_money = ['work','business','forage', 'craft']
    plans_love = ['family','friends','charity']
    plans_fun = ['family', 'friends','chat','pub', 'fish', 'games']
    plans_learn = ['work','craft','study', 'train', 'craft']

    """
    print('generating goals for ' + npc['nme'] + ' born in ' + npc['born'])
    goal = random.choice(goals)

    npc_goals = {}
    npc_goals['money'] = random.randint(1,10)
    npc_goals['love'] = random.randint(1,10)
    npc_goals['fun'] = random.randint(1,10)
    npc_goals['learn'] = random.randint(1,10)
    
    plans = []
    plans.append(get_top_plan_for_goal('money', npc_goals))
    plans.append(get_top_plan_for_goal('love', npc_goals))
    plans.append(get_top_plan_for_goal('fun', npc_goals))
    plans.append(get_top_plan_for_goal('learn', npc_goals))
    #print(npc_goals)


    return npc_goals, plans

def get_top_plan_for_goal(goal, npc_goals):
    if goal == 'money':
        plan = random.choice(plans_money)
        weight = npc_goals[goal]
    elif goal == 'love':
        plan = random.choice(plans_love)
        weight = npc_goals[goal]
    elif goal == 'fun':
        plan = random.choice(plans_fun)
        weight = npc_goals[goal]
    elif goal == 'learn':
        plan = random.choice(plans_learn)
        weight = npc_goals[goal]
        
    return {"plan_name":plan, "weight":weight}


if __name__ == '__main__':
    main()

