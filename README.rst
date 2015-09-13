=========================================
World Build
=========================================

    
(Planning) Tools for computational world building

Overview
--------------------------------
Worldbuild contains tools to build worlds and store the metadata around that, including objects, history, animals, vegetation.

You provide a map of your world and annotate it via a YAML file to define towns with locations - the wiki tool extracts subset of the image to for each town.

You can add additional information to build a rich history around your world.


Quick Start
=========================================

Copy your map file (JPG) or scan a hand drawn map.

.. image:: ./doc/map_sample.jpg


Create a YAML file with the following sections

.. code:: python

    wiki: Yes
    world_name: Alrona
    contents:
        - races
        - settlements
    maps: [alrona-pen-coloured.jpg]


You need to have a root section for each element in contents, and there needs to be a name and desc element at the minimum. 

.. code:: python
    
    settlements:
      - name: Draeton 
        continent: Sharnia
        coords_x_y: [66,58]
        desc: >
            This is the largest city on the East side of Sharnia. 3,000 men live in this strongly 
            defended city
      - name: Ambyle
        continent: Sharnia
        coords_x_y: [64,58]
        desc: >
            Farming town East of Draeton, known for their famous weekend markets selling exotic produce grown in the warm regions north of the Eastern Desert

Then modify the params and run the wiki.py program to generate the HTML version of your world.

The main page looks like 

.. image:: ./doc/web_index.jpg

The settlements page shows the description from the yaml file, and also a section of the map based on the coords_x_y parameter

.. image:: ./doc/web_settlements.jpg


You can extend the wiki with as many sections as you like and each entry can include a file section to import a text (or html) file to be included in that page.
    


Future Functionality
============================
This isn't, and will never be a true rendered 3d representation of a world, rather a macro level world builder for hobbyists and gamers.

Future version will include ability to scan and convert images of world maps, and manage of the narrative of the world. 

Terrain Generation [Random Generation] (in progress)
Use planet.py to create a random planet
Should also allow modifying and saving to proper data format with layers for plants, etc

Scan from picture
Takes an image of a scanned map and extracts the content into multiple layers based on image clustering like hills and trees.  Users can tweak how it converts.

Object builder
- start simple with a name and some stats and can them flesh out details with images icons for map right up to 3d blender models or sgi cad models.

Creature Builder
specify creatures 
simple = rogue specs + icon for moving on 2d map
complex = armour and weapon tables like wow - basic image
path finding - send AI’s around your world to map paths

