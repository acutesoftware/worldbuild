# fishing.py

import sys
import os 

import csv
import random

hours = ['0600','0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300']

fname_chance = 'all_event_chances.csv'
fname_events = 'all_events_occurred.csv'

def main():
    print('running simulation')
    events_daily = read_csv_to_list('../data/events_daily.csv')
    events_weekly = read_csv_to_list('../data/events_weekly.csv')
    events_seasonal = read_csv_to_list('../data/events_seasonal.csv')
    events_annual = read_csv_to_list('../data/events_annual.csv')
    #print(events_daily)
    #print(events_weekly)
    #print(events_seasonal)
    #print(events_annual)

    create_change_table(events_annual[1:], events_daily[1:])

    tbl_chance = read_csv_to_list(fname_chance)
    run_time(tbl_chance)

def run_time(tbl_chance):
    """
    loops through calculated list, running events
    """
    tbl_events_occurred = []
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
    save_list_to_csv(tbl_events_occurred, fname_events)    


def create_change_table(events_annual, events_daily):
    """
    loops through year, building the chance table 
    (the table will be loaded to UE4 as data table
     for simple lookup to process)
    """
    tbl_chance = []
    for day in range(1,28*4):
        for ev in events_annual:
            if ev == []:
                pass
            elif ev[0] == 'Any':
                hh = random.choice(hours)
                chance = int(ev[2])
                tbl_chance.append([day,hh, ev[1],chance, ev[3], ev[4], 'days'])
            else:
                if day == int(ev[0]):
                    hh = random.choice(hours)
                    chance = int(ev[2])
                    tbl_chance.append([day,'0000',ev[1],chance, ev[3], ev[4], 'days'])
        
        
        # now loop through the daily events for this day
        tbl_chance.extend(loop_day(day,events_annual, events_daily))
    tbl_chance.sort()

    #TODO - aggregate multiple chances at same time?
    #"3","0700","env_fog","0.2",
    #"3","0700","env_light_god_rays","0.01",
    #"3","0700","env_light_god_rays","0.1",  <-- should be 1 row = 0.11
    #"3","1000","meteor","0.01",

    save_list_to_csv(tbl_chance, fname_chance)
    


def loop_day(day, events_annual, events_daily):
    """
    loops through a day, checking daily events and running randomly
    """
    tbl_chance = []
    for hh in hours:
        for ev in events_daily:
            if hh == ev[0]:
                chance = int(ev[2]) #get_chance_day_event_modified_by_year(ev, events_annual)
                tbl_chance.append([day,hh,ev[1],chance, ev[3], ev[4], 'minutes'])
                if chance_event(chance):
                    print('Day ' + str(day) + ' - ' + hh + ' = ' + ev[1])
                    
    for ev in events_daily:
        if ev[0] == 'Any':
            hh = random.choice(hours)
            chance = int(ev[2]) #get_chance_day_event_modified_by_year(ev, events_annual)
            tbl_chance.append([day,hh,ev[1],chance, ev[3], ev[4], 'minutes'])
            if chance_event(chance):
                print('Day ' + str(day) + ' - ' + hh + ' = ' + ev[1])


    return tbl_chance

def get_chance_day_event_modified_by_year(ev, events_annual):
    """
    takes a days event and modifies the chance based on 
    the day of the year and the complete annual events
    (eg change of rain at 0900 may be 0.03 but in winter
    this increases by 0.2)
    NO - dont do this
    """
    chance = int(ev[2])/100
    for ann_ev in events_annual:
        if ann_ev[1] == ev[1]:
            print('modifying event')
            chance += int(ann_ev[2])/100
    return chance


def chance_event(rate):
    """
    this takes a param and time and runs a probability to see if
    the event occurrs - returns True or False
    """
    if random.randint(0,99) < int(rate):
        return True
    return False



def today_as_string():
    """
    returns current date and time like oracle
    """
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def append_to_file(fname, txt):
    """
    appends a line of text to a file
    """
    try:
        with open(fname, 'a') as f:
            f.write(txt + '\n')
    except Exception as ex:
        print('error appending to file ' + fname + str(ex))


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