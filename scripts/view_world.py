# view_world.py 
import os
import sys
import math

try:
	import Tkinter as Tkinter
except:
	import tkinter as Tkinter

from PIL import ImageTk, Image, ImageDraw
from tkinter import Tk, Canvas, PhotoImage, mainloop, Frame
        	
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  ) 

default_fname = os.path.join(root_folder, "worldbuild", "data", "sample_world.txt")
print(default_fname)

def main():
    display_map(default_fname)
    
def display_map(fname):
    """
    view a text file (map) in high resolution
    """
    print("viewing ", fname)
    
    app = view_tk(None)
    app.show_grid_from_file(fname)
    app.title('Map View')
    #app.after(2000,vais_main_loop(app))
    
        # bind mouse and keyboard for interactivity
  #  frame = Frame(app, width=100, height=100)
   # frame.bind("<Button-1>", callback)
    app.canvas.bind("<Button-1>", callback)
    app.bind("<Key>", key)

    
    app.mainloop()
    
def callback(event):
    mod_cmd.mouse_click(event.x, event.y)

def key(event):
    x = 60
    y = 22
    mod_cmd.key_pressed(event.char, x, y) 
    

class view_tk(Tkinter.Tk):
    """
    Class to manage the display of a saved text based 
    grid map in a GUI - useful for large grids
    Grid text sample is below:
        ..#......2#XXXXX.............X.X......X.
        ..#......A#XXXX.............XX.......X..
        ..#.A0000A#XXXX...X.XX......XXT......XXX
        ......111A#XXXX....X..X...XXXXX........X
        .....A1...#X..X..XXXXXXX...X.XX........X
    """
    def __init__(self,parent):
        """
        initialise tkinter with default parameters
        """
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.appWidth = 1600   # initial values
        self.appHeight = 900
        self.cell_width = 5
        self.cell_height = 4
        self.fname = ''
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.configure(bg='black')
        self.geometry('%dx%d+%d+%d' % (self.appWidth, self.appHeight, self.screenWidth - self.appWidth - 0, self.screenHeight - self.appHeight - 0))

        WIDTH = self.appWidth
        HEIGHT = self.appHeight
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT, bg="#000000")
        self.canvas.pack()
        self.img = PhotoImage(width=WIDTH, height=HEIGHT)
        self.canvas.create_image(( WIDTH/2,  HEIGHT/2), image=self.img, state="normal")
        #self.TEST_sin()   # testing - draws a sin wave
        self.appWidth = 1600   # canvas.width
        self.appHeight = 900
        
        """
        self.canvas_id = self.canvas.create_text(50, 50, anchor="nw")
        self.canvas.itemconfig(self.canvas_id, text="Welcome to Divitie")
        self.canvas.insert(self.canvas_id, 18, " ")
        """
        
        
        self.canvas.pack()
        
    def TEST_sin(self):    
        for x in range(4 * self.appWidth):
            y = int(self.appHeight/2 + self.appHeight/4 * math.sin(x/80.0))
            self.img.put("#ffffff", (x//4,y))
        self.canvas.pack()
    
    def add_file(self, fname):
        self.fname = fname
    
    def show_grid_from_file(self, fname):
        """
        reads a saved grid file and paints it on the canvas
        """
        with open(fname, "r") as f:
            for y, row in enumerate(f):
                for x, val in enumerate(row):
                    self.draw_cell(y, x, val)


    def draw_cell(self, row, col, val):
        """
        draw a cell as position row, col containing val
        """
        if val == 'T':
            self.paint_target(row,col)
        elif val == '#':
            self.paint_block(row,col)
        elif val == 'X':
            self.paint_hill(row,col)
        elif val == '.':
            self.paint_land(row,col)
        elif val in ['A']:
            self.paint_agent_location(row,col)
        elif val in ['1','2','3','4','5','6','7','8','9']:
            self.paint_agent_trail(row,col, val)
    
    def put_standard_block(self, y, x, val):
        """
        prints a block, packing out around the y/x location
        with pixels up to cell width and cell height
        """
        for j in range(0,self.cell_height):
            for i in range(0,self.cell_width):
                self.img.put(val, (x*self.cell_width+i, y*self.cell_height+j))
    
    def paint_land(self, y, x):
        #self.put_standard_block(y,x,'bisque')
        self.put_standard_block(y,x,'blue')
        
    def paint_block(self, y, x):
        self.put_standard_block(y,x,'gray9')

    def paint_hill(self, y, x):
        self.put_standard_block(y,x,'green4')

    def paint_target(self, y, x):
        self.put_standard_block(y,x,'yellow')
        self.img.put('black', (x*self.cell_width+1, y*self.cell_height+1))
        self.img.put('black', (x*self.cell_width+0, y*self.cell_height+1))
        self.img.put('black', (x*self.cell_width+1, y*self.cell_height+0))
        self.img.put('black', (x*self.cell_width+0, y*self.cell_height+0))

    def paint_agent_trail(self, y, x, val):
        """
        paint an agent trail as ONE pixel to allow for multiple agent
        trails to be seen in the same cell
        """
        for j in range(1,self.cell_height-1):
            for i in range(1,self.cell_width-1):
                self.img.put(self.agent_color(val), (x*self.cell_width+i, y*self.cell_height+j))

        #self.paint_agent_location(y,x,self.agent_color(val))
        # old version - try to paint a single pixel trail but it looks too small
        #self.paint_land(y,x)  # needed otherwise shows up black under dots - todo - fix this
        #self.img.put(self.agent_color(val), (x*self.cell_width, y*self.cell_height))  # +int(val)

    def paint_agent_location(self, y, x):
        self.put_standard_block(y,x,'red')

    def agent_color(self, val):
        """
        gets a colour for agent 0 - 9
        """
        if val == '0': 
            colour = 'blue'
        elif val == '1':
            colour = 'navy'
        elif val == '2':
            colour = 'firebrick'
        elif val == '3':
            colour = 'blue'
        elif val == '4':
            colour = 'blue2'
        elif val == '5':
            colour = 'blue4'
        elif val == '6':
            colour = 'gray22'
        elif val == '7':
            colour = 'gray57'
        elif val == '8':
            colour = 'red4'
        elif val == '9':
            colour = 'red3'

    
        
        return colour
                
if __name__ == "__main__":
    main()