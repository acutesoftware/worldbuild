# minecraft_notes.py
# to make a little house 100 ft above spawn point

# you may need admin on server, so from server console type
/op [your_username]

# now, teleport to where it will be built - a bit off from it
/tp -3 103 -3

# first, we clear the air above the ground (not needed now, but use this command to clean up if you stuff up)
/fill 1 95 1 30 135 30 minecraft:air 0


# sandstone base 1 block high, so base is at 100
# /fill 1 100 1 25 100 25 minecraft:sandstone 0  # one block high
/fill 1 95 1 25 100 25 minecraft:sandstone 0  # 5 blocks high


# to make a hollow stone box on it
/fill 5 100 5 20 106 20 minecraft:stone 0 hollow


# make a door border
/fill 12 101 5 14 103 5 minecraft:sandstone 0

# place the door (need to do it in 2 parts)
/setblock 13 101 5 wooden_door
/setblock 13 102 5 wooden_door 8

# make some windows
/fill 8 103 5 9 104 5 minecraft:glass 0 
/fill 17 103 5 18 104 5 minecraft:glass 0 

