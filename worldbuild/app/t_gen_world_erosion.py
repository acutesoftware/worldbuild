import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

# Set the dimensions of the terrain
width = 256
height = 256

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

# Apply thermal erosion
def thermal_erosion(heightmap, iterations=100, talus_angle=0.01, erosion_factor=0.1):
    width, height = heightmap.shape

    for _ in range(iterations):
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                # Get the height of the current cell
                h = heightmap[j][i]
                
                # Check neighbors and calculate slope
                neighbors = [
                    (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
                ]
                for ni, nj in neighbors:
                    # If the slope is greater than the talus angle, apply erosion
                    h_neighbor = heightmap[nj][ni]
                    slope = h - h_neighbor

                    if slope > talus_angle:
                        erosion_amount = slope * erosion_factor
                        heightmap[j][i] -= erosion_amount
                        heightmap[nj][ni] += erosion_amount
                        
    return heightmap

# Generate and plot terrain with erosion
heightmap = generate_heightmap(width, height)
heightmap_normalized = normalize(heightmap)

# Apply thermal erosion
eroded_heightmap = thermal_erosion(heightmap_normalized, iterations=1000)

# Normalize and plot the eroded terrain
eroded_heightmap_normalized = normalize(eroded_heightmap)

plt.imshow(eroded_heightmap_normalized, cmap='terrain')
plt.colorbar()
plt.show()
