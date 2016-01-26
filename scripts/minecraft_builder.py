# minecraft_builder.py
import time

import aikif.toolbox.interface_windows_tools as mod_tool

fname = 'build_box.bld'

def main():
    print('NOTE - you need to set focus to the command textbox in the Minecraft server')
    print('and do NOT lose focus to the server (dont touch or select anything while this runs)')
    mod_tool.app_activate('Minecraft Server')
    time.sleep(0.2)     

    with open(fname, 'r') as f:
        for line in f:
            if line.strip('\n') == '':
                pass
            elif line[0:1] == '#':
                pass
            else:
                print('sending keys ' , line.strip('\n'))
                mod_tool.send_keys(line.strip('\n'))
                mod_tool.send_keys("{ENTER}")
                time.sleep(0.1) 
main()            