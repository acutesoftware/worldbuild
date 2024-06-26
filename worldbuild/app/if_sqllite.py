#!/usr/bin/python3
# -*- coding: utf-8 -*-
# if_sqllite.py
"""
This module manages standard functions and automatic ETL processes
via SQLLite.

Basic Management
-----------------
- log
- error
- report
- exception
- read_CSV
- write_CSV
- import_SQLLITE
- import_Oracle
- export_SQLLITE
- export_Oracle


Metadata
-----------------
- tables for standard metadata, used for ETL and glossary
- export Glossary
- edit tables for glossary and business rules
- mapping for MDM
- auto metadata collecting

ETL
----------------------
- type 1 update
- type 2 update
- copy table
- aggregate




"""

DEBUG_NUM_FILELISTS_TO_LOAD = 99

####################################################################
# IMPORTS and  Global Variables
import os 
import sys
import sqlite3
import pandas as pd

import table_definitions as tbl_def


LOG_ERROR = 3
LOG_DATA = 2
LOG_INFO = 1

#test_db_file = r'D:\dev\src\PROCGEN\data\test_sqllite.db'
test_db_file = r'N:\duncan\LifePIM_Data\DATA\SQL\test_sqllite.db'

def SELF_TEST():
    print('Self testing SQLLite... TODO - delete current database first?')
    try:
        os.remove(test_db_file)
    except:
        pass
    create_database(test_db_file)
    conn = sqlite3.connect(test_db_file)

    init_metadata_tables(conn)  # defines the table definitions

    print(get_all_metadata(conn))


####################################################################
# Utility Functions

def lg(conn, log_level, txt):
    #print(str(LOG_INFO) + ' : ' + str(txt))

    sql_tbl = '''INSERT INTO sys_log (log_date, log_level, details) VALUES (datetime('now'), ?, ?)'''
    data = ( log_level, txt)
    c = conn.cursor()
    c.execute(sql_tbl, data)
    conn.commit()



####################################################################
# Database Functions


def create_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.sqlite_version)

    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

def exec_ddl(conn, sql, log_entry='Y'):
    """
    runs SQL against a db - used for everything.
    No, there is no SQL injection tests because it is single user.
    """
    #lg(LOG_INFO, 'running SQL ' + sql)
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        if log_entry == 'Y':
            lg(conn, LOG_DATA, 'DDL - ' + sql)
    except Exception as e:
        lg(conn, LOG_ERROR, 'Error running DDL ' + str(e))    

def exec_sql(conn, sql, data):
    """
    runs SQL against a db - used for everything.
    No, there is no SQL injection tests because it is single user.
    """
    #lg(conn, LOG_INFO, 'running SQL ' + sql)
    try:
        c = conn.cursor()
        c.execute(sql, data)
        #print('sql = ' + sql)
        conn.commit()

    except Exception as e:
        lg(conn, LOG_ERROR, 'Error running SQL ' + str(e))    

def get_data(conn, sql, param):
    """
    runs SQL against a db - used for everything.
    No, there is no SQL injection tests because it is single user.
    """
    #lg(LOG_INFO, 'running SQL ' + sql)
    try:
        c = conn.cursor()
        #print('get_data - sql = ' + sql + ' , param = ' + str(param))
        c.execute(sql, param)
        rows = c.fetchall()
        return rows

    except Exception as e:
        lg(conn, LOG_ERROR, 'Error getting data ' + str(e))    





def create_table_from_sqllite(new_db, new_tbl_name, from_db, from_tbl):
    """
    Reads the metadata create script in FROM tbl and generates 
    a copy of it in the new_db as new_tbl_name.
    This is used to make copys of raw to staging tables
    """

    lg(conn, LOG_DATA, "Creating a new table " + new_tbl_name + " from " + from_tbl )

def create_table_from_csv(new_db, new_tbl_name, csv_file, header_rownum):
    """
    Reads CSV file and generates the SQL based on the header.
    It then loads the CSV data into the table
    This is used to make raw tables from CSV
    """

    lg(conn, LOG_DATA, "Creating a new table " + new_tbl_name + " from CSV File" + csv_file )



####################################################################
# Metadata Functions
#
# Everything is defined in the metadata tables in EACH sqllite
# database created - here you define tables, columns FIRST, and 
# then call the "create_table", "copy_data", etc functions.
# you can also batch them into TASK_LISTS and then call the ETL function
# RUN_JOB
#

def init_metadata_tables(conn):
    """
    resets, creates, truncates the sys metadata table and adds 
    standard table defs for each database

    """

    # first we need to manually create the core tables, so the auto create
    # can insert metadata of all table definitions, and log stuff.

    exec_ddl(conn, tbl_def.sql_create_sys_log, 'N')
    exec_ddl(conn, tbl_def.sql_create_sys_meta_tables, 'N')
    exec_ddl(conn, tbl_def.sql_create_sys_meta_table_columns), 'N'
    
    for tbl in tbl_def.def_tables:
        create_table_from_definition(conn, tbl)


def create_table_from_definition(conn, tbl):
    #if tbl[0][0:3] == 'sys_':
    #    return   # dont log sys
    #  6/8/2023
    # TODO - add FORIEGN KEY ... REFERENCE into tbl def for constraints - see https://www.sqlite.org/foreignkeys.html
    #
    sql = 'CREATE TABLE IF NOT EXISTS ' + tbl[0] + ' (\n'
    sql += '     id integer PRIMARY KEY,\n'
    col_tbl_rows = []
    for col in tbl[3].split(','):
        if col.strip(' ') in tbl[4]:  # if the column name is in the list defined as numbers
            sql += '    ' + col + ' INTEGER,\n'
            col_tbl_rows.append([tbl[0], col.strip(' '), 'INTEGER'])
        elif col.strip(' ') in tbl[5]:  # if the column name is in the list defined as numbers
            sql += '    ' + col + ' REAL,\n'
            col_tbl_rows.append([tbl[0], col.strip(' '), 'REAL'])
        elif col.strip(' ') in tbl[6]:  # if the column name is in the list defined as numbers
            sql += '    ' + col + ' BLOB,\n'
            col_tbl_rows.append([tbl[0], col.strip(' '), 'BLOB'])
        else:
            sql += '    ' + col + ' TEXT,\n'
            col_tbl_rows.append([tbl[0], col.strip(' '), 'TEXT'])
    sql += '    ' + 'REC_EXTRACT_DATE TEXT\n'
    sql += '    ' + ');\n'
    exec_ddl(conn, sql)



    # now insert metadata
    sql_tbl = '''INSERT INTO sys_meta_tables (table_name, description, grain_cols, col_list) VALUES (?, ?, ?, ?)'''
    data = (tbl[0], tbl[1], tbl[2], tbl[3] )
    exec_sql(conn, sql_tbl, data)




    for col_num, col_row in enumerate(col_tbl_rows):
        sql_col = '''INSERT INTO sys_meta_table_columns (table_name, col_num, col_name, col_type) VALUES (?, ?, ?, ?)'''
        data = (col_row[0], col_num+1, col_row[1], col_row[2] )
        exec_sql(conn, sql_col, data)        

def get_all_metadata(conn):
    res = []
    sql = '''SELECT name FROM sqlite_master'''
    table_list = get_data(conn, sql, [])
    for tbl in table_list:
        res.append([tbl[0], get_table_metadata(conn, tbl)])
    return res



def get_table_metadata(conn, tbl):
    sql = '''SELECT cid+1 as col_num, name as col_name, type as col_type FROM PRAGMA_TABLE_INFO(?)'''
    res = get_data(conn, sql, tbl)
    short_list = []
    for col_data in res:
        short_list.append(col_data[1])
    return short_list # res


####################################################################
# ETL Functions

def job_create(conn, proj_id, job_num, job_id, details):
    sql_tbl = '''INSERT INTO sys_jobs (proj_id, job_num, job_id, details) VALUES (?, ?, ?, ?)'''
    data = (proj_id, job_num, job_id, details )
    exec_sql(conn, sql_tbl, data)

    # now we need to remove all prev steps for this job from job_steps table
    #sql_del = '''DELETE FROM sys_job_steps WHERE job_id = ?'''
    #data = (job_id)
    #print('running ' + sql_del)  # WARNING - doesnt work check ? above
    #exec_sql(conn, sql_del, data)
    conn.commit()

def job_add_step(conn, job_id, job_num, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run, params):
    # job_id, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run
    sql_tbl = '''INSERT INTO sys_job_steps (job_id, job_num, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run, params) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    data = (job_id, job_num, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run, params)
    
    exec_sql(conn, sql_tbl, data)

    conn.commit()


def run_all_jobs(conn):
    sql = '''SELECT job_id, job_num, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run, params FROM sys_job_steps order by job_num, step_num'''
    res = get_data(conn, sql, [])    
    #print('running jobs - ' + str(res))
    for job_step in res:
        run_job_step(conn, job_step)


def run_job_step(conn, job_step):
    if job_step[3] == 'CSV':
        run_job_step_CSV(conn, job_step)
    elif job_step[3] == 'MANUAL':
        lg(conn, LOG_INFO, 'TODO - Manual step (should ETL pause here?)')

    elif job_step[3] == 'CREATE_FROM_MULT':
        run_job_step_Create_from_Multiple(conn, job_step)
    else:
        run_job_step_SQL(conn, job_step)
        


def run_job_step_CSV(conn, job_step):
    """
    This function needs to use import CSV and manually load all CSV
    files matching source spec to the SQLlite raw table specifed. 
    May also use pandas or BIG
    load by row by row if memory is an issue.

    this loads ALL CSV files into temp tables based on name
    Then creates the main S_RAW table and appends all those into it.
    It should probably also do some nice etl cleanup and remove temp tables
    """
    raw_tbls = []
    import glob
    fl = glob.glob(job_step[4])

    for csv_file in fl[0:DEBUG_NUM_FILELISTS_TO_LOAD]:
        tmp_tbl = get_short_table_name(csv_file)
        lg(conn, LOG_INFO, 'run_job_step_CSV : create table ' + tmp_tbl + ' from external CSV file ' + csv_file) 
        df = pd.read_csv(csv_file)
        df.columns = df.columns.str.strip() # strip whitespace from column headers
        df.to_sql(tmp_tbl, conn)  
        raw_tbls.append(tmp_tbl)  
        conn.commit()


def run_job_step_Create_from_Multiple(conn, job_step):

    # get a list of all tables matching the source (must have % instead of *)
    sql_tbls = 'SELECT name FROM sqlite_master WHERE name like ?'  # 
    raw_tbls = get_data(conn, sql_tbls, [job_step[4]])    
    
    # create the main destination table from FIRST in list
    sql_create = 'CREATE TABLE ' + job_step[5] + ' AS SELECT * FROM ' + raw_tbls[0][0]
    lg(conn, LOG_INFO, 'run_job_step_Create_from_Multiple : running ' + sql_create) 
    exec_ddl(conn, sql_create, log_entry='N')

    # now each of these need to be appended to master table get_short_table_name
    for raw_tbl in raw_tbls[1:]: # first one already loaded, so start at 1 not 0
            
        sql_append = 'INSERT INTO ' + job_step[5] + ' SELECT * FROM ' + raw_tbl[0]
        lg(conn, LOG_INFO, 'run_job_step_Create_from_Multiple : running ' + sql_append) 
        exec_sql(conn, sql_append, [])
        conn.commit()

        # now that table is appended - drop the raw table
        exec_sql(conn, 'DROP TABLE ' + raw_tbl[0], [])
        conn.commit()

    # also, drop the first table we created
    exec_sql(conn, 'DROP TABLE ' + raw_tbls[0][0], '')  # note this is the FULL array (1st element)
    conn.commit()


def run_job_step_SQL(conn, job_step):
    """
    This function runs the SQL in local database
    """
    sql_tbl = job_step[7]  # SQL - should have ? where needed
    data = job_step[8]  # params
        
    lg(conn, LOG_INFO, 'running ' + sql_tbl + ' with params = ' + str(data))        

    exec_sql(conn, sql_tbl, data)        


def get_short_table_name(txt):
    nme = txt.split(os.sep)
    #print('get_short_table_name' + str(nme))
    fname = ''.join(nme[len(nme) - 1:])[:-4]
    #print('fname' + str(fname))
    return fname

# ---- Database Functions
def get_table_summary(conn, db_file):
    """
    return a list of information on the database
    TODO - move this to ETL load so it gets calculated once on load
    """
    res = []
    res.append(['info', 'Database Filename', db_file])
    #res.append(['info', 'Database size (bytes)', 'todo'])

    #sql = '''SELECT cid+1 as col_num, name as col_name, type as col_type FROM PRAGMA_TABLE_INFO(?)'''

    short_list = []
    sql_tbl_list = "SELECT name FROM sqlite_master WHERE type in ('table') and name not like 'sys_%' and name not like 'App_%' order by 1";
    tbl_list =  get_data(conn, sql_tbl_list, [])
    for tbl in tbl_list:
        row_count = get_data(conn, "SELECT count(*) from " + tbl[0], [])
        #print(
        res.append(['tbl', tbl[0], row_count[0][0]])
        
    return res


if __name__ == '__main__':
    SELF_TEST()
