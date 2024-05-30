# sample.py
import os
import sys
import glob
import fnmatch
import json
import yaml

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'samples' ) 

#print('data_fldr = ', data_fldr)
sample_xtn = '*.sample'


def main():
    print('Sample worlds')
    for root, _, files in os.walk(data_fldr):
        for f in files:
            fullname = os.path.join(root,f)
            print('reading ' + f)
            if f[-5:].lower() == '.yaml':
                _print_yaml(fullname)
            #get_variables(fullname)
        
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

##################################################
# misc utils to be put somewhere better later on
##################################################

def read_yaml(fname):
    """
    reads a yaml file
    """
    import yaml

    with open(fname, 'r') as stream:
        print(yaml.load(stream, Loader=yaml.SafeLoader))
 
    
def convert_json_to_yaml(fname):    
    import json
    import yaml
    
    if os.path.exists(fname):    
        jstr = open(fname, 'r').read()
    else:
        jstr = '{ "NO_DATA": "bar" }'
    print(' ----------- JSON to YAML ---------------')
    jdata = json.loads(jstr)
    yml = yaml.safe_dump(jdata)
    return jdata    
 
def convert_yaml_to_json(fname):    
    if os.path.exists(fname):    
        ystr = open(fname, 'r').read()
    else:
        ystr = '--- NO_DATA:bar'
    print(' ----------- YAML to JSON ----------- ')
    ydata = yaml.load(ystr, Loader=yaml.SafeLoader)
    jstr = json.dumps(ydata)
    return jstr
 
def _print_yaml(fname):
    print('\n' + fname)
    with open(fname, 'r') as stream:
        print(yaml.load(stream, Loader=yaml.SafeLoader))
     
def _read_yaml(fname):
    with open(fname, 'r') as stream:
        return yaml.load(stream, Loader=yaml.SafeLoader)


if __name__ == '__main__': 
    main()
