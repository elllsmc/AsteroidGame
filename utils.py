# as images will be loaded many times in game, seperate file created to extract 
# functionality to keep reusable methods and implement image loading

# image = sprite
# sound, font etc = asset

from pygame.image import load #load() method for reading images

def load_sprite(name, with_alpha=True):
    path = f"C:/Users/44746/OneDrive/Documents/Personal/Python/Asteroids/Assets/{name}.jpg" # creates a path to an image
    loaded_sprite = load(path) # method returns a 'surface', used to represent an image

    if with_alpha:
        return loaded_sprite.convert_alpha() #f ormat image size to screen
    else:
        return loaded_sprite.convert() # method differs based on transparency