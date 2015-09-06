#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wiki.py
import os
import sys
import config
import sample
import pprint

def main():
    """
    manages the wiki pages
    To generate new pages, use the command 
    > python wiki.py samples
    """
    if len(sys.argv) > 1:
        print('creating wiki from command line')
        create_sample_wiki(sys.argv[1])
    else:
        print('creating sample wiki from command line')
        create_wiki_from_yaml(os.path.join('samples','alrona.yaml'))
    print('remember, to run from cmd line = > python wiki.py samples/filename.yaml')    

def create_wiki_from_yaml(fname):
    dat = sample._read_yaml(fname)
    pprint.pprint(dat)
    if 'wiki' in dat:
        print('generating wiki for ' + fname)
    
def create_sample_wiki(fname=''):
    if fname == '':
        print("Generating sample wiki pages")
        for p in config.wiki_pages:
            print('generating ' + p)
    else:
        create_wiki_from_yaml(fname)
        
    print("Done")

class Page(object):
    """
    base class for the wiki pages that converts
    to various outputs
    """
    def __init__(self, nme, content):
        self.nme = nme
        self.content = content
        print('creating page ' + nme)
    
    def export(self):
        print('exporting..')
        



if __name__ == '__main__':    
    main()    
    
 