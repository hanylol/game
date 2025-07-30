from ursina import *
from props import Box

class MirageMap(Entity):
    def __init__(self):
        super().__init__()

        # A Site
        Entity(parent=self, model='cube', scale=(20, 1, 20), position=(0, 0, 20), color=color.orange, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(20, 5, 1), position=(0, 2.5, 30), color=color.gray, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(10, 2.5, 20), color=color.gray, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(-10, 2.5, 20), color=color.gray, collider='box') # Wall
        Box(position=(5, 1, 15))
        Box(position=(-5, 1, 15))

        # B Site
        Entity(parent=self, model='cube', scale=(20, 1, 20), position=(0, 0, -20), color=color.blue, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(20, 5, 1), position=(0, 2.5, -10), color=color.gray, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(10, 2.5, -20), color=color.gray, collider='box') # Wall
        Entity(parent=self, model='cube', scale=(1, 5, 20), position=(-10, 2.5, -20), color=color.gray, collider='box') # Wall

        # Mid
        Entity(parent=self, model='cube', scale=(10, 1, 40), position=(15, 0, 0), color=color.green, collider='box') # Floor
        Entity(parent=self, model='cube', scale=(10, 1, 40), position=(-15, 0, 0), color=color.green, collider='box') # Floor
