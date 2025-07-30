from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import skins

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = FirstPersonController(parent=self,
            model='cube',
            scale=(1, 1, 0.5),
            position=(0, 0.5, 0),
            color=skins.player_skins[skins.current_player_skin],
            origin_y=-.5
            )
        self.head = Entity(
            parent=self.controller,
            model='sphere',
            scale=(0.5, 0.5, 0.5),
            position=(0, 1.5, 0),
            color=color.white
        )
        self.controller.camera_pivot.z = -1
        self.controller.camera_pivot.y = 2
        self.health = 100
        self.health_bar = Entity(
            parent=camera.ui,
            model='quad',
            scale=(self.health/100 * 0.5, 0.02),
            position=(-0.7, -0.4),
            color=color.red
        )


    def update(self):
        self.controller.camera_pivot.y = 2 - held_keys['left control']
        if self.controller.velocity.length() > 0:
            self.head.position = (0, 1.5 + sin(time.time() * 10) * 0.1, 0)
        else:
            self.head.position = (0, 1.5, 0)
        if self.health <= 0:
            destroy(self.controller)
            destroy(self)
            Text(text='Game Over', origin=(0, 0), scale=5, color=color.red)
        self.health_bar.scale_x = self.health/100 * 0.5


    def input(self, key):
        if key == 'p':
            skins.next_player_skin()
            self.controller.color = skins.player_skins[skins.current_player_skin]
