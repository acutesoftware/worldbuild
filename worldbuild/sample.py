# sample.py
import os
import sys
import glob
import fnmatch

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'samples' ) 
print('data_fldr = ', data_fldr)
sample_xtn = '*.sample'


def main():
    print('Sample worlds')
    for root, _, files in os.walk(data_fldr):
        for f in files:
            fullname = os.path.join(root,f)
            print('reading ' + f)
            get_variables(fullname)
        
def get_variables(fname):
    """
    read all the parameters in the file world_name
    from the samples folder
    """
    print(fname + ' Variables')
    all_modules_vars = [item for item in dir(fname) if not item.startswith("__")]
    for variable_name in all_modules_vars:
        if len(variable_name) > 2:
            print('  ',  variable_name)
        #print(str(variable_name))

main()