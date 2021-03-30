# fishing.py

import sys
import os 

import csv
import random

hours = ['0600','0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300']

fname_chance = 'all_event_chances.csv'
fname_events = 'all_events_occurred.csv'

id_length = 6

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


def create_change_table(events_annual, events_daily):
    """
    loops through year, building the chance table 
    (the table will be loaded to UE4 as data table
     for simple lookup to process)
    """
    rowid = 0
    tbl_chance = []
    for day in range(1,28*4):
        for ev in events_annual:
            if ev == []:
                pass
            elif ev[0] == 'Any':
                hh = random.choice(hours)
                chance = int(ev[2])
                rowid += 1
                tbl_chance.append([get_id(rowid), day,hh, ev[1],chance, ev[3], ev[4], 'days'])
            else:
                if day == int(ev[0]):
                    hh = random.choice(hours)
                    chance = int(ev[2])
                    rowid += 1
                    tbl_chance.append([get_id(rowid), day,'0000',ev[1],chance, ev[3], ev[4], 'days'])
        
        
        # now loop through the daily events for this day
        daily_events, rowid = loop_day(rowid, day,events_annual, events_daily)
        tbl_chance.extend(daily_events)
    tbl_chance.sort()
    tbl_chance.insert(0,['RowName', 'Day', 'HHMM', 'event_id', 'chance', 'min_length', 'max_length', 'time_unit'])

    #TODO - aggregate multiple chances at same time?
    #"3","0700","env_fog","0.2",
    #"3","0700","env_light_god_rays","0.01",
    #"3","0700","env_light_god_rays","0.1",  <-- should be 1 row = 0.11
    #"3","1000","meteor","0.01",

    save_list_to_csv(tbl_chance, fname_chance)
    
def get_id(rowid):
    return str(rowid).zfill(id_length)

def loop_day(rowid_start, day, events_annual, events_daily):
    """
    loops through a day, checking daily events and running randomly
    """
    tbl_chance = []
    rowid = rowid_start
    for hh in hours:
        for ev in events_daily:
            if hh == ev[0]:
                chance = int(ev[2]) #get_chance_day_event_modified_by_year(ev, events_annual)
                rowid += 1
                tbl_chance.append([get_id(rowid), day,hh,ev[1],chance, ev[3], ev[4], 'minutes'])
                
    for ev in events_daily:
        if ev[0] == 'Any':
            hh = random.choice(hours)
            chance = int(ev[2]) #get_chance_day_event_modified_by_year(ev, events_annual)
            rowid += 1
            tbl_chance.append([get_id(rowid), day,hh,ev[1],chance, ev[3], ev[4], 'minutes'])


    return tbl_chance, rowid




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