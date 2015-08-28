#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wiki.py
import os
import sys
import config



def main():
    """
    manages the wiki pages
    To generate new pages, use the command 
    > python wiki.py samples
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == 'samples':
            create_sample_wiki()
    else:
        print('To generate sample wiki pages using the command:\n > python wiki.py samples')
        

def create_sample_wiki():
    print("Generating sample wiki pages")
    for p in config.wiki_pages:
        print('generating ' + p)
        
    
    
    
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
        
class WikiList(Page):
    """
    manages a list of pages, like objects, vegetation
    that includes images etc
    """
    pass
    
    
class WikiInfo(Page):
    """
    base class to manage the content around the world
    """
    pass
    




if __name__ == '__main__':    
    main()    
    
 