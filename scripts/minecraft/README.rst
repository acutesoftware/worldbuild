=========================================
Worldbuild - Minecraft
=========================================
     
Builds structures in Minecraft local server (currently using sendkeys)



Basic Usage
----------------

.. code:: python

    import castle_maker
    castle_maker.fill_area(70,62,-77,110,62,-34, 'minecraft:grass')
    castle_maker.make_castle_walls(70,63,-67,34,4,32, 2)  # outer wall
    castle_maker.gate(x=81, y=63, z=-68, width=3, height=6, length=4)
    castle_maker.tower_building(x=78, y=62, z=-55, width=11, height=5, length=10, butt_height=0)
    castle_maker.make_castle_walls(78,67,-55,10,1,9, 0)  # top parapet


.. image:: https://github.com/acutesoftware/worldbuild/blob/master/scripts/minecraft/screenshots/tiny_castle.png

