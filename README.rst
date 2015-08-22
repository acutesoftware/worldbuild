=========================================
World Build
=========================================

    
(Planning) Tools for computational world building

Proposal / Overview
--------------------------------
This package currently has the planet terrain code previously from VAIS.

It will contain tools to build worlds and store the metadata around that, including objects, history, animals, vegetation

This is NOT a true rendered 3d representation of a world, rather a macro level world builder for hobbyists and gamers.

Future version will include ability to scan and convert images of world maps, and manage of the narrative of the world. 



Tools
-------------------------------

World Overview
=========================================

Has tools and wizards to guide you to give as much or as little detail as you want - this is the meta data of the world and will be helpful for later auto implementation


Terrain Generation
=========================================
Free form
You can draw lines and place down land / vegetation etc in a gui (best if it is javascript rather than TKinter)

Random Generation (in progress)
Use planet.py to create a random planet
Should also allow modifying and saving to proper data format with layers for plants, etc

Scan from picture
Takes an image of a scanned map and extracts the content into multiple layers based on image clustering like hills and trees.  Users can tweak how it converts.


Object builder
=========================================
Remember you start simple with a name and some stats and can them flesh out details with images icons for map right up to 3d blender models or sgi cad models.

Creature Builder
=========================================
specify creatures 
simple = rogue specs + icon for moving on 2d map
complex = armour and weapon tables like wow - basic image
path finding - send AI’s around your world to map paths

