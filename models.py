from pygame.image import load
from pygame.math import Vector2
from utils import load_sprite
from pygame.transform import rotozoom # responsible for scaling/rotating

UP = Vector2(0, -1) # pygame Y axis  goes from top to bottom so -ve value points upwards

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position) # centre of obj
        self.sprite = sprite # image used to draw object
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity) # updates position each frame

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius) # calculate correct position for blitting
        surface.blit(self.sprite, blit_position) # positions object on surface

    def move(self):
        self.position = self.position + self.velocity # update position vector

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius # if distance between two objects is smaller than sum of radius', collision

class Spaceship(GameObject):
    MANEUVERABILITY = 3 # value determines how fast ship can rotate - higher = faster
    def __init__(self, position):
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("ship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP) # calculate angle to be rotated  by to match other vecton
        rotated_surface = rotozoom(self.sprite, angle, 1.0) # rotation
        rotated_surface_size = Vector2(rotated_surface.get_size()) # recalc blit pos
        blit_position = self.position - rotated_surface_size * 0.5 # to center the rotated image, move blit position by half the size of the image
        surface.blit(rotated_surface, blit_position) # put new image on screen
