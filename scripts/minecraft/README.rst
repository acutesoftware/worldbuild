=========================================
Worldbuild - Minecraft
=========================================
     
Builds structures in Minecraft local server using sendkeys to a local server



Basic Usage
----------------
Download this package using
git clone https://github.com/acutesoftware/worldbuild.git


Start a local minecraft server on the PC (Windows only at this stage), and select the text box in the servers GUI

Run the code below (location can be anywhere, but teleport to 70 65 -80 to see castle below) 
    
.. code:: python

    import castle_maker
    castle_maker.fill_area(70,62,-77,110,62,-34, 'minecraft:grass')
    castle_maker.make_castle_walls(70,63,-67,34,4,32, 2)  # outer wall
    castle_maker.gate(x=81, y=63, z=-68, width=3, height=6, length=4)
    castle_maker.tower_building(x=78, y=62, z=-55, width=11, height=5, length=10, butt_height=0)
    castle_maker.make_castle_walls(78,67,-55,10,1,9, 0)  # top parapet

This will create the following structure

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/tiny_castle.png


Structures 
-----------------------

Castle Wall - single castle wall

Window - place a window

Main_door - fancy door

Make castle wall - makes 4 walls joined

gate - gate for outer castle wall

build_tower - enclosed tower, with floors if very tall and stairs between them

stairs - fancy stairs for main buildings (tower stairs are fixed at moment)

Catapult - place a catapult (non working)


Plant - setout fenced grass area and plant veges (has torches and water holes)

