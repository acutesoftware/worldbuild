# minecraft_builder.py
import time

import aikif.toolbox.interface_windows_tools as mod_tool


def main():
    make_structure('build_box.bld')
    make_structure('build_house.bld')

def make_structure(fname):
    print('NOTE - you need to set focus to the command textbox in the Minecraft server')
    print('and do NOT lose focus to the server (dont touch or select anything while this runs)')
    res = []
    with open(fname, 'r') as f:
        for line in f:
            res.append(line)
    make_from_list(res)
 

def log_list(lst):
    with open('last_build.log', 'a') as f:
        for line in lst:
            f.write(line + '\n')
                
def make_from_list(lst):
    log_list(lst)
    for line in lst:
        if line.strip('\n') == '':
            pass
        elif line[0:1] == '#':
            pass
        elif line[0:1] == '@':
            mod_tool.app_activate(line.strip('\n')[1:])
            time.sleep(.1)     
            
        else:
            print('sending keys ' , str(line).strip('\n'))
            mod_tool.send_keys(str(line).strip('\n'))
            time.sleep(0.01) 
            mod_tool.send_keys("{ENTER}")
            time.sleep(0.01) 


def make_from_list_rcon(lst, rcon_connection):
    log_list(lst)
    for line in lst:
        if line.strip('\n') == '':
            pass
        elif line[0:1] == '#':
            pass
        elif line[0:1] == '@':
            pass
        else:
            print('rcon ' , str(line).strip('\n'))
            rcon_connection.command(line)




            
def mc_fill(x1, y1, z1, x2, y2, z2, item):
    """
    formats the fill params to a minecraft command
    /fill 1 79 1 9 88 9 minecraft:air 0
    /fill 1 80 1 4 84 4 minecraft:sandstone 0 hollow
    /fill 1 79 1 4 79 4 minecraft:stone 0
    /fill 1 85 1 4 85 4 minecraft:wool 3
    /fill 1 81 2 1 83 3 minecraft:air 0

    
    """
    r = '/fill ' 
    r += str(x1) + ' '
    r += str(y1) + ' ' 
    r += str(z1) + ' ' 
    r += str(x2) + ' ' 
    r += str(y2) + ' ' 
    r += str(z2) + ' ' 
    r += item
    return r 
                
if __name__ == '__main__':                
    main()            
