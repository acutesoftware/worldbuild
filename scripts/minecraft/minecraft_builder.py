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
            time.sleep(1)     
            
        else:
            print('sending keys ' , line.strip('\n'))
            mod_tool.send_keys(line.strip('\n'))
            time.sleep(0.01) 
            mod_tool.send_keys("{ENTER}")
            time.sleep(0.1) 
    

                
if __name__ == '__main__':                
    main()            
