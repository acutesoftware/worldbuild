import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

# Set the dimensions of the terrain
width = 256
height = 256


def run_tool(params):
    width       =  params[0] # int(get_val('width', params))
    height      =  params[1] # int(get_val('height', params))
    scale       =  params[2] # int(get_val('num_seeds', params))
    octaves     =  params[3] # int(get_val('perc_land', params))
    persistence =  params[4] # int(get_val('perc_sea', params))
    lacunarity  =  params[5] # int(get_val('perc_blocked', params))

    # Generate and plot terrain
    #heightmap = generate_heightmap(width, height)
    heightmap = generate_heightmap(width, height, scale, octaves, persistence, lacunarity)    

    heightmap_normalized = normalize(heightmap)

    plt.imshow(heightmap_normalized, cmap='terrain')
    plt.colorbar()
    plt.show()

 

# Generate a heightmap using Perlin noise
def generate_heightmap(width, height, scale=100, octaves=6, persistence=0.5, lacunarity=2.0):
    heightmap = np.zeros((height, width))
    
    for i in range(width):
        for j in range(height):
            # Perlin noise value at this point
            heightmap[j][i] = pnoise2(i / scale, 
                                      j / scale, 
                                      octaves=octaves, 
                                      persistence=persistence, 
                                      lacunarity=lacunarity)
    return heightmap

# Scale and normalize heightmap values
def normalize(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))
 
