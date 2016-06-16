# run_tests.py
import os
import time
import unittest as unittest

all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    

def wipe_file(fname):
    if os.path.exists(fname):
        try:
            os.remove(fname)
            print('deleted ' + fname)
        except:
            pass
        

print ('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(10)

wipe_file('test_world.txt')
wipe_file('world_traversed.txt')
wipe_file('agent.txt')