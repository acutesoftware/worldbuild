

###################### TEMPLATES #########################

def get_header(pge=''):
    txt = '<!DOCTYPE html><HTML><HEAD>\n'
    txt += '<title>worldbuild:' + pge + '</title>\n'
    txt += '<!-- Stylesheets for responsive design -->\n'
    txt += '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
    txt += '<link rel="stylesheet" type="text/css" href="worldbuild.css" media="screen" />\n'
    txt += '<link rel="stylesheet" href="worldbuild_mob.css"'
    txt += ' media="only screen and (min-device-width : 320px) and (max-device-width : 480px)">\n'
    txt += '</HEAD>\n'
    txt += '<body>\n'
    return txt
    
def get_footer(pge=''):
    txt = '\n\n<BR><BR><BR>\n<div id="footer">\n'
    txt += pge
    txt += '<HR>This page was generated from <a href="https://github.com/acutesoftware/worldbuild">worldbuild</a> - '
    txt += '</div></BODY></HTML>\n'
    return txt

def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res

def format_list_as_html_table_row(lst):
    txt = '<TR>'
    for i in lst:
        txt = txt + '<TD>' + i + '</TD>'
    txt = txt + '</TR>'	
    return txt
    
def format_csv_to_html(csvFile):
    txt += "<TABLE>"
    with open(csvFile) as csv_file:
        for row in csv_file:
            cols = row.split('","')
            txt += "<TR>"
            for col in cols:
                txt += "<TD>"
                txt += escape_html(col.strip('"'))
                txt += "</TD>"
            txt += "</TR>"
        txt += "</TABLE>"
    return txt

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
    return rows_to_load[1:]
