# table_definitions.py

sql_create_sys_log = """ CREATE TABLE IF NOT EXISTS sys_log (
                                        id integer PRIMARY KEY,
                                        log_date text,
                                        log_level integer,
                                        details text NOT NULL
                                        
                                    ); """

sql_create_sys_meta_tables = """ CREATE TABLE IF NOT EXISTS sys_meta_tables (
                                        id integer PRIMARY KEY,
                                        table_name text NOT NULL,
                                        description text,
                                        grain_cols text,
                                        col_list text,
                                        rec_extract_date text
                                        
                                    ); """

sql_create_sys_meta_table_columns = """ CREATE TABLE IF NOT EXISTS sys_meta_table_columns (
                                        id integer PRIMARY KEY,
                                        table_name text NOT NULL,
                                        col_num INTEGER,
                                        col_name text,
                                        col_type text,
                                        description text,
                                        rec_extract_date text
                                        
                                    ); """

# The above 3 core tables do not need to be added to the table list, and can be created
# from SQL above FIRST, so that in the init function, the metadata is inserted anyway.

def_tables = [ # [table_name, description, grain_cols, col_list, cols_INT, cols_REAL, cols_BLOB]
    ['sys_meta_tables', 'Table definitions for database', 'table_name', 'table_name, description, grain_cols, col_list', [], [], []],
    ['sys_meta_table_columns', 'Column definitions for database', 'table_name, col_num, col_name', 'table_name, col_name, col_type, description', ['col_num'], [], []],
    ['sys_log', 'Main logfile for database', 'log_date', 'log_date, log_level, details', ['log_level'], [], []],
    ['sys_usage', 'Usage log', 'log_date', 'log_date, details', [], [], []],
    ['sys_proj', 'Project Details', 'id', 'proj_id, details', [], [], []],
    ['sys_jobs', 'ETL Job to run', 'proj_id, job_id', 'proj_id, job_num, job_id, details', ['job_num'], [], []],
    ['sys_job_steps', 'SQL to run for step of a job', 'job_id, step_num', 'job_id, job_num, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run, params', ['step_num', 'job_num'], [], []],
    ['sys_todo', 'Dev notes on things to do, bugs to fix', 'todo_id', 'todo_id, date_added, date_done, tpe, details', [], [], []],

    
]


sql_view_file_xtn = """CREATE VIEW V_FILE_XTN AS 
    SELECT replace(name, rtrim(name, replace(name, '.', '')), '') as xtn, 
            sum(size) as tot_size, count(*) as num_files 
    FROM s_filelist_raw 
    group by replace(name, rtrim(name, replace(name, '.', '')), '');
"""