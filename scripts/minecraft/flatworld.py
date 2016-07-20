# flatworld.py
import time

import aikif.toolbox.interface_windows_tools as mod_tool


fname = 'build_flatworld.bld'

def main():
    with open(fname, 'r') as f:
        for line in f:
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
                time.sleep(0.2) 
                mod_tool.send_keys("{ENTER}")
                time.sleep(1) 
main()            