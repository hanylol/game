from ursina import *
from props import Box

class MirageMap(Entity):
    def __init__(self):
        super().__init__()

        # Textures
        sand_texture = 'assets/textures/sand.jpg'
        wall_texture = 'assets/textures/wall.jpg'

        # A Site
        Entity(parent=self, model='cube', scale=(20, 1, 20), position=(0, 0, 20), texture=sand_texture, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(20, 5, 1), position=(0, 2.5, 30), texture=wall_texture, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(10, 2.5, 20), texture=wall_texture, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(-10, 2.5, 20), texture=wall_texture, collider='box') # Wall
        Box(position=(5, 1, 15))
        Box(position=(-5, 1, 15))

        # B Site
        Entity(parent=self, model='cube', scale=(20, 1, 20), position=(0, 0, -20), texture=sand_texture, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(20, 5, 1), position=(0, 2.5, -10), texture=wall_texture, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(10, 2.5, -20), texture=wall_texture, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(-10, 2.5, -20), texture=wall_texture, collider='box') # Wall

        # Mid
        Entity(parent=self, model='cube', scale=(10, 1, 40), position=(15, 0, 0), texture=sand_texture, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(10, 1, 40), position=(-15, 0, 0), texture=sand_texture, collider='box') # Floor
