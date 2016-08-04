=========================================
Worldbuild - Minecraft
=========================================
     
Builds structures in Minecraft local server using sendkeys to a local server



Basic Usage
----------------
Download this package using
git clone https://github.com/acutesoftware/worldbuild.git


Start a local minecraft server on the PC (Windows only at this stage), and select the text box in the servers GUI

Change directory to scripts/minecraft folder and run the code below
    
.. code:: python

    import castle_maker
    castle_maker.fill_area(70,62,-77,110,62,-34, 'minecraft:grass')
    castle_maker.make_castle_walls(70,63,-67,34,4,32, 2)  # outer wall
    castle_maker.gate(x=81, y=63, z=-68, width=3, height=6, length=4)
    castle_maker.tower_building(x=78, y=62, z=-55, width=11, height=5, length=10, butt_height=0)
    castle_maker.make_castle_walls(78,67,-55,10,1,9, 0)  # top parapet

This will create the following structure at location 70 62 -77 

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/tiny_castle.png


Structures 
-----------------------

Castle Wall - single castle wall

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/sample_castle_walls.png


Window - place a window

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/window.png


Main_door - fancy door

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/castle_door.png



gate - gate for outer castle wall

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/gate.png


build_tower - enclosed tower, with floors if very tall and stairs between them

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/castle_towers_inside.png


stairs - fancy stairs for main buildings (tower stairs are fixed at moment)

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/castle_inside_empty_ground_flr.png


Catapult - place a catapult (non working)

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/catapult.png


Plant - setout fenced grass area and plant veges (has torches and water holes)

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/garden.png



Complex Structures
----------------------------------------

Using the Make castle wall function (makes 4 walls joined) and wipe_area you can make complex walls as follows

    
.. code:: python

    castle_maker.make_castle_walls(30,63,30,120,4,90, 6)  # massive outer wall
    castle_maker.make_castle_walls(70,63,30,40,4,20, 6)  # gate inset wall
    castle_maker.make_castle_walls(30,63,74,20,4,46, 6)  # lower left inset wall
    castle_maker.make_castle_walls(130,63,74,20,4,46, 6)  # lower right inset wall
    clear_area.wipe_all(x=30,  y=63, z=81, w=10, h=7, d=49)  # clear bottom left corner
    clear_area.wipe_all(x=137, y=63, z=81, w=13, h=7, d=49) # clear bottom right corner
    clear_area.wipe_all(x=77,  y=63, z=30, w=26, h=7, d=8) # clear front gate inset

    
Will create a structure like 

.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/sample_castle_walls_complex.jpg


