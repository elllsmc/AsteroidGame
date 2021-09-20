from pygame.image import load
from pygame.math import Vector2
from utils import load_sprite

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
    def __init__(self, position):
        super().__init__(position, load_sprite("ship"), Vector2(0))