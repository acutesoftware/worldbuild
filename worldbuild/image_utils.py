# image_utils.py

import aikif.toolbox.image_tools as mod_img


def make_map_medium(fname, op_file):
    """
    takes the main map file and makes a copy resized for html summary
    """
    print(fname, op_file)
    mod_img.resize(fname, 500, op_file)

def extract_map_fragment(map_file, coords, op_file):
    """
    Takes the map and extracts a segment of the map at coords
    into a separate file, used for the settlement wiki so we 
    can see where each town and city lives.
    
    NOTE coords is (x,y) and is a PERCENTAGE of the image size
    
    """
    from PIL import Image

    # size is width/height
    img = Image.open(map_file)
    width, height = img.size
    centre_x_pixels = int(round(width * (coords[0]/100), 0))
    centre_y_pixels = int(round(height * (coords[1]/100), 0))
    offset_x = int(round(width * (22/100), 0))
    offset_y = int(round(height * (11/100), 0))
    print(centre_x_pixels, centre_y_pixels)
    left = centre_x_pixels - offset_x
    top = centre_y_pixels - offset_y
    right = left + offset_x
    bottom = top + offset_y
    
    if left < 1:
        left = 0
        right = offset_x * 2
        
    if top < 1:
        top = 0
        bottom = offset_y * 2
        
    if right > width:
        right = width
        left = offset_x * 2
        
    if bottom > height:
        bottom = height
        top = offset_y * 2
        
        
    # crop the image: im.crop((left, top, right, bottom))
    box = (left, top, right, bottom)
    area = img.crop(box)

    area.save(op_file, 'jpeg')
    #img.close()    
        