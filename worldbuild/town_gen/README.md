# Town Generator

prototype code to create random towns for games / worlds.

## Quick Start

1. Install worldbuild

```
pip install worldbuild
```

2. generate a random town 

```
import worldbuild.town_gen.town_gen as town_gen
res = town_gen.make_town('MyTown',town_y=5,town_x=20, 90)
```

3. print the town (or use in your code)

```
print(res)

Town "PrintableTown" located at  x=0/ y=0
SIZE:  x=12/ y=6
...SSP..hSPS
============
h....HS.TH.S
H.....H.h.Hh
.HH..H......
...........H
Shops    = 6 [0/3,0/4,0/9,0/11,2/6,2/11]
Pubs     = 2 [0/5,0/10]
TownHall = 1 [2/8]
Houses   = 13

```

![2D Rendered image of generated town](https://github.com/acutesoftware/worldbuild/blob/master/tests/town_gen_test_result.png)

See tests folder for more examples


## Standard buildings
Buildings are randomly placed and based on the following Building objects

```
road = Building(5,5,0,  building_type = '=')
pub = Building(7,8,2,  building_type = 'P')
shop = Building(4,6,1,  building_type = 'S')
town_hall = Building(9,9,1,  building_type = 'T')
house_small = Building(2,3,1,  building_type = 'h')
house_big = Building(4,5,2,  building_type = 'H')
empty_plot = Building(0,0,0,  building_type = '.')
```

