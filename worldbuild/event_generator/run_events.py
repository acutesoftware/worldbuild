#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run_events.py

import sys
import os 

import csv
import random
from pprint import pprint

hours = ['0600','0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300']

fname_chance = 'all_event_chances.csv'
fname_events = 'all_events_occurred.csv'

def main():

    tbl_chance = read_csv_to_list(fname_chance)
    run_time(tbl_chance)

def run_time(tbl_chance):
    """
    loops through calculated list, running events
    """
    tbl_events_occurred = []
    event_counts = make_empty_count_array(tbl_chance)
    print(event_counts)
    tbl_events_occurred.append(['Day', 'Time', 'Event_id', 'Length', 'Units'])
    for ev in tbl_chance:
        ev_day = ev[0]
        ev_hh = ev[1]
        ev_id = ev[2]
        ev_chance = ev[3]
        ev_min = int(ev[4])
        ev_max = int(ev[5])
        ev_units = ev[6]

        ev_length = random.randint(ev_min, ev_max)
        if chance_event(ev_chance):
            tbl_events_occurred.append([ev_day, ev_hh, ev_id, ev_length, ev_units])
            event_counts[ev_id] += 1

    pprint(event_counts)
    save_list_to_csv(tbl_events_occurred, fname_events)    

def make_empty_count_array(tbl_chance):
    event_counts = {}
    all_events = []
    uniq_events = []
    for ev in tbl_chance:
        all_events.append(ev[2])
    for uniq_event in list(set(all_events)):
        uniq_events.append([uniq_event, 0])
    event_counts = dict(uniq_events)
    return event_counts



def chance_event(rate):
    """
    this takes a param and time and runs a probability to see if
    the event occurrs - returns True or False
    """
    if random.randint(0,99) < int(rate):
        return True
    return False




def read_csv_to_list(filename):
    """
    reads a CSV file to a list
    """
    import csv

    rows_to_load = []
    with open(filename, 'r', encoding='cp1252') as csvfile: # sort of works with , encoding='cp65001'
        #csvreader = csv.reader(csvfile, delimiter = ',' )

        reader = csv.reader(csvfile)

        rows_to_load = list(reader)
    return rows_to_load

def save_list_to_csv(lst, filename):
    """
    takes a list and saves to CSV
    """

    with open(filename, 'w', encoding='UTF-8') as f:
        for row in lst:
            for col in row:
                if col:
                    f.write( '"' + str(col) + '",')
                else:
                    f.write('"",')
            f.write('\n')


main()