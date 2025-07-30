from ursina import *

class Barrier(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model='cube',
            collider='box',
            color=color.gray,
            **kwargs
        )
