from ursina import *

class Box(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model='cube',
            scale=2,
            position=position,
            color=color.brown,
            collider='box'
        )
