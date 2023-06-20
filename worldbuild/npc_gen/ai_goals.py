#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ai_goals.py

import os 
import sys
import random 

import npc_gen

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)

npc_file = 'random_npc.csv'

goal_filename = 'op_npc_goals.csv'
plan_filename = 'op_npc_plans.csv'
task_filename = 'op_npc_tasks.csv'

goals = ['money', 'family','fun', 'learn']


plans_money = ['work','business','forage', 'craft']
plans_love = ['family','friends','charity']
plans_fun = ['family', 'friends','chat','pub', 'fish', 'games']
plans_learn = ['work','craft','study', 'train', 'craft']

interests = ['people','outdoors', 'fashion', 'food', 'building', 'books', 'games','sports' ]

tasks = ['fishing','library', 'job', 'run_stall', 'run_shop', 'talk', 'make_clothes', 'dressup', 'cafe', 'restaurant', 'events', 'party', 'pub', 'crafting', 'help_others', 'forage', 'shopping', 'explore', 'cook', 'cards', 'soccer']

tasks_for_plans = [   # plan_id, task_id, weight
    ['work', 'job', 9 ], 
    ['work', 'run_stall', 8 ], 
    ['work', 'forage', 4 ], 
    ['work', 'forage', 4 ], 
    ['business', 'run_stall', 9 ], 
    ['business', 'run_shop', 10 ], 
    ['forage', 'forage', 9 ],
    ['forage', 'explore', 8 ],
    ['forage', 'fishing', 7 ],
    ['craft', 'make_clothes', 5 ],
    ['craft', 'crafting', 10 ],
    ['craft', 'cook', 7 ],
    ['family', 'cafe', 7 ],
    ['family', 'restaurant', 7 ],
    ['family', 'shopping', 7 ],    
    ['friends', 'cafe', 7 ],
    ['friends', 'restaurant', 7 ],
    ['friends', 'shopping', 7 ],    
    ['charity', 'run_stall', 5 ],
    ['charity', 'help_others', 10 ],
    ['chat', 'talk', 10 ],
    ['pub', 'pub', 10 ],
    ['fish', 'fishing', 10 ],
    ['games', 'cards', 5 ],
    ['games', 'soccer', 5 ],
    ['study', 'study', 10 ],
    ['train', 'train', 10 ],
    ['craft', 'craft', 10 ],
]

tasks_for_interests = [   # interest_id , task_id, weighting
    ['people', 'talk_friends', 9],
    ['people', 'meet_strangers', 4],
    ['people', 'events', 9],
    ['people', 'restaurant', 6],
    ['people', 'cafe', 5],
    ['people', 'pub', 5],
    ['outdoors', 'fishing', 7 ],
    ['outdoors', 'forage', 7 ],
    ['outdoors', 'explore', 7 ],
    ['fashion', 'make_clothes', 7 ],
    ['fashion', 'dressup', 7],
    ['fashion', 'events', 7],
    ['fashion', 'restaurant', 6],
    ['food', 'cook', 9],
    ['food', 'restaurant', 8],
    ['food', 'cafe', 7],
    ['building', 'crafting', 7],
    ['building', 'forage', 7],
    ['books', 'reading', 9],
    ['books', 'library', 8],
    ['books', 'shopping', 7],
    ['games', 'cards', 9],
    ['sports', 'cards', 8],
    ['sports', 'soccer', 8],    
]

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



----------------------------------------
Elin goals = {'money': 3, 'love': 2, 'fun': 10, 'learn': 9}
----------------------------------------
plan = {'plan_name': 'work', 'weight': 3}
plan = {'plan_name': 'charity', 'weight': 2}
plan = {'plan_name': 'games', 'weight': 10}
plan = {'plan_name': 'craft', 'weight': 9}
getting tasks based on top plan : {'plan_name': 'games', 'weight': 10}
['games', 'cards', 5]
['games', 'soccer', 5]
getting random tasks based on some interests : ['relax', 'building', 'fashion', 'games', 'sports']
['building', 'crafting', 7]

"""



def main():
    print('Generating Goals, Plans and Actions for NPCs from ' + npc_file)
    npc_gen.save_list_to_csv(["NPC","Goal","Weight"], goal_filename)
    npc_gen.save_list_to_csv(["NPC","Goal","Plan", "Plan_weight"], plan_filename)
    npc_gen.save_list_to_csv(["NPC","Goal","Plan", "Plan_weight", "Task"], task_filename)

    with open(npc_file, 'r') as fip:
        for line_num, line in enumerate(fip):
            if line_num > 0:
                npc = extract_npc_raw_data(line)
                my_interests = get_random_interests(npc)
                goals, plans = assign_goals(npc)
                my_tasks = get_tasks(npc, goals, plans, my_interests)
                display_npc_goals(npc, goals, plans)
                save_all(npc, goals, plans, my_tasks)

            

def save_all(npc, goals, plans, my_tasks):
    """
    saves 3 files at different grains showing goals, 
    plans and tasks and how they are linked.
    """
    all_goals = []
    all_plans = []
    all_tasks = []    

    for goal in goals:
        all_goals.append([npc['nme'], goal[0], goal[1]])
        for plan in plans:
            all_plans.append([npc['nme'], goal[0], goal[1], plan[0], plan[1]])
            for task in my_tasks:
                all_tasks.append([npc['nme'], goal[0], goal[1], plan[0], plan[1], task])

    npc_gen.append_list_to_csv(all_goals, goal_filename)
    npc_gen.append_list_to_csv(all_plans, plan_filename)
    npc_gen.append_list_to_csv(all_tasks, task_filename)
    

def display_npc_goals(npc, goals, plans):
    print('\n----------------------------------------')
    print(npc['nme'] + ' goals = ' + str(goals))
    print('----------------------------------------')
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
   
def get_random_interests(npc):
    #print('getting interests for ' + str(npc))
    npc_interests = ['relax']
    num_interests = random.randint(2,7)
    for n in range(num_interests):
        new_interest = random.choice(interests)
        if new_interest not in npc_interests:
            npc_interests.append(new_interest)
    return npc_interests


def assign_goals(npc):
    """
    all NPC's have ALL goals but are weighted from 0 to 10 depending
    on how important they are to them (based on random + upbringing).

    plans_money = ['work','business','forage', 'craft']
    plans_love = ['family','friends','charity']
    plans_fun = ['family', 'friends','chat','pub', 'fish', 'games']
    plans_learn = ['work','craft','study', 'train', 'craft']

    """
    #print('generating goals for ' + npc['nme'] + ' born in ' + npc['born'])
    #goal = random.choice(goals)

    #npc_goals = {}
    #npc_goals['money'] = random.randint(1,10)
    #npc_goals['love'] = random.randint(1,10)
    #npc_goals['fun'] = random.randint(1,10)
    #npc_goals['learn'] = random.randint(1,10)
    
    npc_goals = []
    npc_goals.append(['money', random.randint(1,10)])
    npc_goals.append(['love', random.randint(1,10)])
    npc_goals.append(['fun', random.randint(1,10)])
    npc_goals.append(['learn', random.randint(1,10)])


    plans = []
    plans.append(get_top_plan_for_goal('money', npc_goals))
    plans.append(get_top_plan_for_goal('love', npc_goals))
    plans.append(get_top_plan_for_goal('fun', npc_goals))
    plans.append(get_top_plan_for_goal('learn', npc_goals))
    #print(npc_goals)


    return npc_goals, plans

def get_top_plan_for_goal(goal, npc_goals):
    weight = 0
    plan = ''
    print('getting plan for goal : ' + str(goal))
    if goal == 'money':
        plan = random.choice(plans_money)
        weight = random.randint(1,10)
    elif goal == 'love':
        plan = random.choice(plans_love)
        weight = random.randint(1,10)
    elif goal == 'fun':
        plan = random.choice(plans_fun)
        weight =random.randint(1,10)
    elif goal == 'learn':
        plan = random.choice(plans_learn)
        weight = random.randint(1,10) # npc_goals[goal[1]]
        
    print('plan = ' + str(plan) + " weight = " + str(weight))
    return [plan, weight]

def get_top_plan(plan_list):
    #return max(plan_list, key= lambda x: plan_list[x])
    max_val = 0
    highest_plan = ''
    for plan in plan_list:
        if plan[1] > max_val:
            max_val = plan[1]
            highest_plan = plan
    return highest_plan
    

def get_tasks(npc, goals, plans, my_interests):
    my_tasks = []
    num_tasks_added_for_interest = 0
    plan  = get_top_plan(plans)

    
    print('getting tasks based on top plan : ' + str(plan))

    # add all tasks for my TOP plan
    
    for task_plan in tasks_for_plans:
        if plan[0] == task_plan[0]:
            my_tasks.append(task_plan[1])
            print(task_plan)
    
    """

    # add all tasks for TOP interest
    print('getting random tasks based on some interests : ' + str(my_interests))
    todays_interest = random.choice(my_interests)
    for intr in tasks_for_interests:
        if intr[0] == todays_interest:
            if num_tasks_added_for_interest == 0:
                my_tasks.append(intr[1])
                num_tasks_added_for_interest += 1
                print(intr)
            else:
                if random.randint(1,10) > 5:
                    my_tasks.append(intr[1])
                    num_tasks_added_for_interest += 1
                    print(intr)

    """

    return my_tasks



if __name__ == '__main__':
    main()

