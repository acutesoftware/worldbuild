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
  sap (x1)
  wood (x2)
  stick (x1)
  milk (x2)
\=======================/

```

Press 'b' and Enter to craft craft all items

```
enter command: b
crafting Torch
crafting Wooden Plank
crafting Charcoal
crafting Butter
crafting Biscuit
Finished Build all - you made  5 items
    -=< InventoryItem >=-
/=======================\
  biscuit (x1)
  butter (x1)
  charcoal (x1)
  torch (x1)
  wooden_plank (x1)
\=======================/

```

You can add random inventory items to check crafting lots of recipes

```

enter command: a
Adding glue (x3)
Adding pick (x31)

```

or you can just edit inventory.csv in the worldbuild\data folder


## Data Structures

Shows how crafting is managed


### Recipes

The recipe.csv file has one line per recipe and shows the display name and cost to build

```

recipe_id,recipe_name,base_time_to_build,base_cost_to_build
torch,Torch,1,0
wooden_plank,Wooden Plank,3,1
charcoal,Charcoal,3,0

```

### Items

Items are all the 'stuff' in the world - this includes raw materials and crafted items.

```

category,name,type,buy_price,sell_price,description
forage,wood_stick,Wooden stick,2,0,
forage,wood_twig,Wooden Twig,2,0,
forage,wood,Wood,2,0,
material,string, Used for fishing rods and bows,2,1,

```


### IngredientRecipes

For each recipe, there can be 1 or more items needed to make it.
There are multiple records per recipe to allow for complex recipes to be made

```

recipe_id,item_id,quantity,crafting_method_id
torch,stick,1,attach_misc
torch,sap,1,attach_misc
wooden_plank,wood,1,cut_saw
charcoal,wood,1,burn_flame
butter,milk,1,mix
bread,yeast,1,mix
bread,water,3,mix
bread,flour,5,mix

```


