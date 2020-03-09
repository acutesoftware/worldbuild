#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen.py

import os 
import sys
import random 

#import aikif.agents.explore.agent_explore_grid as mod_agt

import aikif.toolbox.cls_grid as mod_grid
from . import town_gen_config as cfg

def TEST():
    print('generating town...')
    dat_town = make_town(3, 5, 50)
    print(dat_town)


def make_town(town_name, sze_y, sze_x, sparseness):
    """
    generates the town
    """
    #agt = mod_agt.ExploreAgent('TEST - exploring_agent',  os.getcwd(), 4, True)
    #grd = mod_grid.Grid(grid_height=3, grid_width=sze, pieces=buildings, spacing=2)   

    t = Town(town_name, 0,0,sze_y,sze_x, sparseness)

    return t
    


class Building(object):
    def __init__(self, max_x, max_y, max_z, building_type):
        if max_x == 0:
            self.x = 0        
            self.y = 0        
            self.z = 0      
        else:
            # for random size buildings (maybe houses - DO LATER)

            if building_type in ['s', 'S']:
                self.x = random.randint(1, max_x)  + 4      
                self.y = random.randint(1, max_y)  + 4   
                self.z = random.randint(0, max_z)      
            else:
                self.x = max_x       
                self.y = max_y       
                self.z = max_z

        self.building_type = building_type 


    def __str__(self):
        res = self.building_type + ' at w=' + str(self.x) + ', l=' + str(self.y) + '\n'    
        return res

class Town(object):
    """
    A town has a grid of size_y / size_x and each cell contains a plot.
    The plot is arbitralily 8x8 so a building can be up to 8x8. 
    This allows for random size buildings (most will be 3x3) to be 
    fitted onto a plot without worrying about space fitting algorithms.
    """
    def __init__(self, town_name, pos_y, pos_x, size_y, size_x, sparseness):
        self.pos_x = pos_x
        self.pos_y =pos_y
        #self.size_x = random.randint(2, max_x)        
        #self.size_y = random.randint(2, max_y)     

        self.town_name = town_name   
        self.size_x = size_x  
        self.size_y =size_y

        self.road = Building(*cfg.road_size,  cfg.road_building_type)
        self.pub = Building(*cfg.pub_size,  cfg.pub_building_type)
        self.shop = Building(*cfg.shop_size,  cfg.shop_building_type)
        self.town_hall = Building(*cfg.town_hall_size,  cfg.town_hall_building_type)
        self.house_small = Building(*cfg.house_small_size,  cfg.house_small_building_type)
        self.house_big = Building(*cfg.house_big_size,  cfg.house_big_building_type)
        self.empty_plot = Building(*cfg.empty_plot_size,  cfg.empty_plot_building_type)

        self.sparse_percent = sparseness # 50
        self.town_grid = [ [ self.empty_plot for dummy_x in range( size_x ) ] for dummy_y in range( size_y ) ]
        self.road_y = 1

        self.add_roads()
        self.add_random_houses()
        self.add_random_shops()
        self.add_random_pubs()
        self.add_random_townhall()

        self.shop_list = []
        self.pub_list = []
        self.house_list = []
        self.townhall_list = []
        self.update_building_lists()

        # 2D image variables
        self.y_space_building = cfg.y_space_building
        self.x_space_building = cfg.x_space_building



        #print('town_grid = ', self.town_grid)
        #print(self)


    def __str__(self):
        res = '\nTown "' + self.town_name + '" located at  x=' + str(self.pos_x) + '/ y=' + str(self.pos_y) +  '\n' 
        res += 'SIZE:  x=' + str(self.size_x) + '/ y=' + str(self.size_y) +  '\n' 
        #res += str(self.grid)  
        building_list = ''
        for y in range(self.size_y ):
            for x in range(self.size_x):
                #print('town: y=', y, ', x=', x)
                if self.town_grid[y][x]:
                    res += self.town_grid[y][x].building_type
                    if not self.town_grid[y][x].building_type in ['.', '=']:  # self.empty_plot.building_type:
                        building_list += 'y=' + str(y) + ',x=' + str(x) + ' : ' + str(self.town_grid[y][x])
                else:
                    res += '.'                   
            res += '\n'

        # now list all buildings in town
        #res += building_list + '\n'
        res += 'Shops    = ' + str(len(self.shop_list)) + ' ['
        res += ','.join(str(p[0]) + '/' + str(p[1]) for p in self.shop_list) + ']\n'
        
        res += 'Pubs     = ' + str(len(self.pub_list)) + ' ['
        res += ','.join(str(p[0]) + '/' + str(p[1]) for p in self.pub_list) + ']\n'
        #print('pub_list = ',self.pub_list )

        res += 'TownHall = ' + str(len(self.townhall_list)) + ' ['
        res += ','.join(str(p[0]) + '/' + str(p[1]) for p in self.townhall_list) + ']\n'


        res += 'Houses   = ' + str(len(self.house_list)) + '\n'


        return res

    def add_building(self, y,x, building):
        """
        adds type Building to the town at pos x,y
        """
        #print('adding building "' + building.building_type +  '" to town x,y at ', x,y)
        #self.grid.set_tile(y, x, building_type)
        self.town_grid[y][x] = building

    def add_roads(self):
        # put a road down the middle
        self.road_y = int(self.size_y/2) - random.randint(0,3)  # horizontal road Y position through town
        if self.road_y < 1:
            self.road_y = 1
        for x in range(self.size_x):
            self.add_building(self.road_y,x,self.road)    
        

    def get_random_road_y_pos(self):
        if random.randint(1,100) > 50:
            y_pos = self.road_y + 1
        else:
            y_pos = self.road_y - 1
        return y_pos


    def add_random_houses(self):
        """
        add a random number of houses to the map based on sparsity
        and size of map
        """
        # add random houses on the map
        for x_pos in range(self.size_x):
            for y_pos in range(self.size_y):
                if random.randint(1,100) > self.sparse_percent:
                    if y_pos != self.road_y:  # cant build house on road
                    #y_pos = self.get_random_road_y_pos()
                        house_type = random.choice([self.house_small, self.house_big])
                        self.add_building(y_pos,x_pos,house_type)   


    def add_random_shops(self):
        """
        add a random number of shops to the map based on sparsity
        and size of map
        """
        # Add shops    
        shop_cluster_x = random.randint(int(self.size_x/4),int(self.size_x/2)) - int(self.size_x/4)
        if self.sparse_percent > 50:
            if self.size_x < 10:
                num_shops = 1  + random.randint(1, 2)
            else:
                num_shops = 2 + random.randint(2, 4)
        else:
            if self.size_x < 10:
                num_shops = 1 + random.randint(2, 3)
            else:
                num_shops = 2 + random.randint(1, int(self.size_x/10)  - int(self.sparse_percent/30))

        if num_shops < cfg.num_shops_min:
            num_shops = cfg.num_shops_min
        if num_shops > cfg.num_shops_max:
            num_shops = cfg.num_shops_max
        #print('num_shops = ', num_shops, ' starting at shop_cluster_x=' , shop_cluster_x)
        cur_shop_x = shop_cluster_x + random.randint(0,1)
        for shop_x in range(0, num_shops):
            cur_shop_x +=  shop_x
            if cur_shop_x > self.size_x-1:
                cur_shop_x = self.size_x-1
            y_pos = self.get_random_road_y_pos()
            #print('adding shop to ', y_pos, cur_shop_x)
            self.add_building(y_pos,cur_shop_x,self.shop)   
            

    def add_random_pubs(self):
        """
        add a random number of pubs to the map based on sparsity
        and size of map
        """
        # add 1 pub near outskirts (even if one exists)
        tx = random.randint(1, self.size_x-1)
        self.add_building(self.road_y-1,tx,self.pub)

        if self.size_x > cfg.pub_add_if_size_x_greater:   # add another pub if large width
            tx = random.randint(5, 8)
            self.add_building(self.road_y-1,tx,self.pub)

        if self.sparse_percent < cfg.pub_add_if_sparse_perc_less:   # add another pub if med population
            tx = random.randint(self.size_x-4, self.size_x-1)
            self.add_building(self.road_y-1,tx,self.pub)



    def add_random_townhall(self):
        """
        add a town hall to the map. Should be only 1
        """
        # add one and only one town hall near the centre
        tx = random.randint(int(self.size_x/2) - 2, int(self.size_x/2) + 2)
        if tx < 2:
            tx = 2
        if tx > self.size_x - 2: 
            tx = self.size_x - 2

        self.add_building(self.road_y+1,tx,self.town_hall)

    def update_building_lists(self):
        """
        generate lists of building objects with town x/y coords
        self.shop_list = []
        self.pub_list = []
        self.house_list = []
        self.update_building_lists        
        """
        for y in range(self.size_y ):
            for x in range(self.size_x):
                if self.town_grid[y][x].building_type in ['h', 'H']: 
                    self.house_list.append([y,x,self.town_grid[y][x]])
                if self.town_grid[y][x].building_type in ['s', 'S']: 
                    self.shop_list.append([y,x,self.town_grid[y][x]])
                if self.town_grid[y][x].building_type in ['p', 'P']:  # self.empty_plot.building_type:
                    self.pub_list.append([y,x,self.town_grid[y][x]])
                if self.town_grid[y][x].building_type in ['t', 'T']:  # self.empty_plot.building_type:
                    self.townhall_list.append([y,x,self.town_grid[y][x]])

        #print('house list = ', self.house_list)


    def output_detail(self, op_file_name, show_grid='N'):
        """
        outputs detailled view of town using grid as well as 
        the building sizes
        """
        from PIL import Image, ImageDraw

        col_blue = (0,0, 255)
        col_green = (0,255,0)
        col_red = (255,0, 0)

        res = []

        pic_x = self.size_x * self.x_space_building + self.x_space_building
        pic_y = self.size_y * self.y_space_building + self.y_space_building


        print('Generating town image...')


        im= Image.new('RGB', (pic_x, pic_y))
        # im.putdata([(255,0,0), (0,255,0), (0,0,255)]) -- puts 3 pixels on screen
        draw = ImageDraw.Draw(im) 
        base_x = int( self.x_space_building / 2 )
        base_y = int( self.y_space_building / 2 )
        
        if show_grid !='N':
            # draw a debug grid
            for y in range(self.size_y):
                draw.line((base_x,y * self.y_space_building, pic_x - base_x, y * self.y_space_building), fill=col_red)

            for x in range(self.size_x):
                draw.line((x * self.x_space_building, base_y, x * self.x_space_building, pic_y - base_y), fill=col_blue)


        # Now draw the buildings
        for y in range(self.size_y):

            for x in range(self.size_x):
                building = self.town_grid[y][x]
                #im.putdata([(255,0,0), (0,255,0), (0,0,255)])
                #print(' drawing building', str(building))
                start_y =  base_y + y * self.y_space_building
                start_x =  base_x + x * self.x_space_building
                width = building.x * self.x_space_building/10 #+  x_space_building/10
                length = building.y * self.y_space_building/10 #+  y_space_building/10
                self._draw_building_2d( draw, start_y, start_x, length, width, building)
        
        im.show()




        im.save(op_file_name)


        return res


    def _draw_building_2d(self, draw, y, x, width, length, building):
        """
        draw a 2D building on the image 
        """

        if y > self.road_y: # make shops and pub hard against road
            y += int(self.y_space_building/2) #+ 50
        else:
            y -=  int(self.y_space_building/2)# - 50
           
        if building.building_type == '=':
            draw.rectangle(((x, y-cfg.road_edge_y), (x+width, y+length+cfg.road_edge_y)), fill=cfg.road_edge_colour)
            draw.rectangle(((x, y), (x+width, y+length)), fill=cfg.road_colour)
            line_y = int(y+length/2)
            space_x = int(x + width/4)
            for line_x in range(x, int(x + width) - int(width/10), 25):
                draw.rectangle(((line_x  , line_y-2), (line_x + 14, line_y+2)), fill=cfg.road_white_line_colour)

        if building.building_type in ['h', 'H']:
            draw.rectangle(((x-1, y-1), (x+width+1, y+length+1)), fill=cfg.house_border_colour)
            draw.rectangle(((x, y), (x+width, y+length)), fill=cfg.house_body_colour)
            # now draw a little roof
            roof_left = (x-2, y-1)
            roof_top = (x+width/2, y-25)
            roof_right = (x+width+2,y-1)

            draw.polygon([roof_top, roof_left, roof_right], fill = cfg.house_roof_colour)



        if building.building_type in ['p', 'P']:
            draw.rectangle(((x-1, y-1), (x+width+1, y+length+1)), fill=cfg.pub_border_colour)
            draw.rectangle(((x, y), (x+width, y+length)), fill=cfg.pub_colour)

        if building.building_type in ['s', 'S']:
            draw.rectangle(((x-1, y-1), (x+width+1, y+length+1)), fill=cfg.shop_border_colour)
            draw.rectangle(((x, y), (x+width, y+length)), fill=cfg.shop_colour)

        if building.building_type in ['t', 'T']:
            draw.rectangle(((x-1, y-1), (x+width+1, y+length+1)), fill=cfg.town_hall_border_colour)
            draw.rectangle(((x, y), (x+width, y+length)), fill=cfg.town_hall_colour)


        if building.building_type ==  '.':   # empty plot
            if random.randint(1,100) < cfg.empty_plot_chance_tree:   # draw trees sometimes
                x += random.randint(8,29) - 15
                y += random.randint(8,29) - 15
                #print('drawing tree')
                r = 12 + random.randint(1,20)
                leftUpPoint = (x-r/2, y-r)
                rightDownPoint = (x+r, y+r)
                twoPointList = [leftUpPoint, rightDownPoint]
                draw.ellipse(twoPointList, fill=cfg.tree_leaf_colour)
                draw.rectangle(((x+2, y+r), (x+9, y+r+30)), fill=cfg.tree_trunk_colour)
                # add random fruit
                if random.randint(1,100) < cfg.tree_chance_fruit:
                    fruit = random.choice(cfg.tree_fruit_colours)
                    draw.rectangle(((x, y-r+3), (x+4, y-r+6)), fill=fruit)
                    draw.rectangle(((x+12, y), (x+16, y+4)), fill=fruit)
                    draw.rectangle(((x-2, y-4), (x+2, y)), fill=fruit)
                    draw.rectangle(((x-3, y+r-3), (x+1, y+r+1)), fill=fruit)


if __name__ == '__main__':
    TEST()

