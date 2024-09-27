from flask import Flask, render_template, jsonify, request
from flask import send_file, url_for
from werkzeug.utils import safe_join
import sqlite3

import os
import sys
import importlib
from PIL import Image
import wb_app_utils as mod_wb
import if_sqllite as mod_sql
import config_app as mod_cfg

data_folder = mod_cfg.fldr_data # '/home/duncan/dev/src/python/worldbuild/worldbuild/data/wb_appdata'

db_file =  mod_cfg.db_file # os.path.join(data_folder, 'worldbuild.db')

IMAGE_FOLDER = mod_cfg.IMAGE_FOLDER
THUMBNAIL_FOLDER = mod_cfg.THUMBNAIL_FOLDER
THUMBNAIL_SIZE = mod_cfg.THUMBNAIL_SIZE


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    
    return render_template('index.html',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Home'),
                           current_menu='Home')

# ------------------------------ FILES ----------------------------

@app.route('/files')
def files():
    fl = get_list_thumbnails()
    print('fl - ' + str(fl))
    return render_template('files.html',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Files'),
                           current_menu='Files',
                           thumbnails=fl)

def get_list_thumbnails():
    # List all files in the external image directory
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    thumbnails = []
    
    # Generate thumbnails if they don't exist
    for image_file in image_files:
        name, ext = os.path.splitext(image_file)
        #print('name = ' +  name  )
        #print('ext = ' + ext )
        if ext in ['.jpg','.png']:
            thumbnail_path = os.path.join(THUMBNAIL_FOLDER, image_file)
            #print('thumbnail_path ' + thumbnail_path)
            if not os.path.exists(thumbnail_path):
                create_thumbnail(os.path.join(IMAGE_FOLDER, image_file), thumbnail_path)
            thumbnails.append(image_file)
    #print('thumbnails = ' + str(thumbnails))            
    return thumbnails
    #return render_template('files.html', thumbnails=thumbnails)

def create_thumbnail(image_path, thumbnail_path):
    img = Image.open(image_path)
    img.thumbnail(THUMBNAIL_SIZE)
    thumbnail_dir = os.path.dirname(thumbnail_path)
    if not os.path.exists(thumbnail_dir):
        os.makedirs(thumbnail_dir)
    img.save(thumbnail_path)

@app.route('/thumbnails/<filename>')
def serve_thumbnail(filename):
    mnu = mod_wb.get_top_menu(get_db_connection(), 'Home')
    
    return send_file(safe_join(THUMBNAIL_FOLDER, filename))

@app.route('/images/<filename>')
def serve_image(filename):
    mnu = mod_wb.get_top_menu(get_db_connection(), 'Home')
    return send_file(safe_join(IMAGE_FOLDER, filename))
    

# ---------------------------- DATA ---------------------------------


@app.route('/data')
def data():
    conn = get_db_connection()
    res = mod_sql.get_table_summary(conn, db_file)
    mnu = mod_wb.get_top_menu(get_db_connection(), 'Home')
    return render_template('data.html',
                           res = res,
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Data'),
                           current_menu='Data')


# ----- DATA TABLES -----------------------------


@app.route('/tables')
def tables():
    conn = get_db_connection()
    
    cursor = conn.execute("SELECT DISTINCT menu FROM App_menu;")
    menus = cursor.fetchall()
    
    menu_dict = {}
    for menu in menus:
        menu_name = menu['menu']
        cursor = conn.execute("SELECT submenu, table_name FROM App_menu WHERE menu = ?", (menu_name,))
        submenus = cursor.fetchall()
        menu_dict[menu_name] = submenus
    
    conn.close()
    return render_template('tables_list.html',
                           menus=menu_dict,
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Data'),
                           current_menu='Data')

@app.route('/table/<v_table_name>')
def show_table(v_table_name):
    submenu = request.args.get('submenu', '')
    conn = get_db_connection()
    # get the list of columns we want to show in table list mode
    #print('v_table_name = ' + v_table_name)
    sql_meta = "SELECT menu,submenu,table_name,col_list_view FROM App_menu WHERE table_name = '" + v_table_name + "'"
    res = mod_sql.get_data(conn, sql_meta, [])[0]   # only fetching 1 row

    #print('res=' + str(res) + ' res[0]=' + str(res[0]))
    row_view_cols = res[3]
    #print('row_view_cols = ' + str(row_view_cols)) 
    cols_to_show = row_view_cols.split(",")
    
    #print('cols_to_show = ' + str(cols_to_show))    
    # now get the contents of the table
    cursor = conn.execute(f"SELECT {row_view_cols} FROM {v_table_name};")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    #print('columns = ' + str(columns))

    if row_view_cols == '*':
        cols_to_render = columns
    else:
        cols_to_render = cols_to_show
    
    conn.close()
    return render_template('table_contents.html',
                           v_table_name=v_table_name,
                           v_menu=res[0],
                           v_submenu=res[1],
                           columns=cols_to_render,
                           current_menu='Data',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Data'),
                           rows=rows,
                           submenu=submenu)



# ----- TABLE CONTENTS -----------------------------

@app.route('/row/<table_name>/<row_id>')
def show_row_details(table_name, row_id):
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT * FROM {table_name} WHERE id = '{row_id}';")
    row = cursor.fetchone()
    columns = [description[0] for description in cursor.description]
    conn.close()
    return render_template('row_details.html',
                           table_name=table_name,
                           columns=columns,
                           row=row,
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Data'),
                           current_menu='Data')



# ---------------------------- TOOLS -----------------------------


@app.route('/tools')
def tools():
    mnu = mod_wb.get_top_menu(get_db_connection(), 'Tools')

    #mod_wb.save_list(mod_cfg.tool_list, 'tools.csv')
    
    return render_template('tools.html',
                           current_menu='Tools',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Tools'),
                           current_tool = '',
                           tool_list = mod_wb.get_tool_list(get_db_connection())
                           )


@app.route('/tool/<tool_id>', methods=['GET'])
def tool_current(tool_id):
    t = mod_wb.get_tool_details(get_db_connection(), tool_id)
    # tool_id,tool_name,py_import,desc,param_names,param_defaults
    print('t=' + str(t))
    tool_id = t[0]
    tool_name=t[1]
    py_import=t[2]
    desc = t[3]
    params_with_defaults=t[4]

    mod_tool = importlib.import_module(py_import)

    html_form, form_param_list, param_values = mod_wb.create_html_tool_form(params_with_defaults)

    print('TOOL REFRESH : form_param_list = ' + str(form_param_list))
    
    res = mod_tool.run_tool(param_values)
            
    return render_template('tool.html',
                           current_menu='Tools',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Tools'),
                           current_tool = tool_name,
                           tool_id=tool_id,
                           content_html = res,
                           form_param_list = form_param_list,
                           param_values = param_values,
                           tool_list = mod_wb.get_tool_list(get_db_connection())
                           )

@app.route('/tool/<tool_id>', methods=['POST'])
def tool_clicked(tool_id):
   new_form_param_list, new_param_values = mod_wb.get_tool_form_results(get_db_connection(), tool_id)
   t = mod_wb.get_tool_details(get_db_connection(), tool_id)
   mod_tool = importlib.import_module(t[2])
   res = mod_tool.run_tool(new_param_values)
            
   return render_template('tool.html',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Tools'),
                           current_menu = 'Tools',
                           current_tool = t[1],
                           tool_id=tool_id,
                           content_html = res,
                           form_param_list = new_form_param_list,
                           param_values = new_param_values,
                           tool_list = mod_wb.get_tool_list(get_db_connection())
                           )
    
    

@app.route('/option')
def page_options():
    print('options')
    return render_template('about.html',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Options'),
                           current_menu='Options')

@app.route('/publish')
def page_publish():
    return render_template('index.html',
                           top_menus = mod_wb.get_top_menu(get_db_connection(), 'Publish'),
                           current_menu='Publish')

#@app.route('/top_menu')
#def top_menu():
#    current_menu = request.args.get('current_menu', 'home')
#    return render_template('top_menu.html', current_menu=current_menu)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
