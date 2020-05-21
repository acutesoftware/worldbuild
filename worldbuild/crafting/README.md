# Crafting Simulator

prototype code to simulate crafting for games / worlds.

## Quick Start
run simulate_crafting.py to build objects from random inventory items

```
    -=< Recipe >=-
/=======================\
  1 - Torch
  2 - Wooden Plank
  3 - Charcoal
  4 - Butter
  5 - Bread
  6 - Biscuit
\=======================/

    -=< InventoryItem >=-
/=======================\
  1 - cheese (x1)
  2 - wood_stick (x2)
  3 - wood_twig (x2)
  4 - wood (x20)
  5 - string (x1)
  6 - shells (x5)
\=======================/
```

Press 2 and press Enter to craft a wooden plank (which uses 1x wood)

```
enter command: 2
crafting Wooden Plank
sorting bags...
    -=< InventoryItem >=-
/=======================\
  1 - cheese (x1)
  2 - shells (x5)
  3 - string (x1)
  4 - wood (x19)
  5 - wood_stick (x2)
  6 - wood_twig (x2)
  7 - wooden_plank (x1)
\=======================/

```

