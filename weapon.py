from ursina import *
import skins

class Weapon(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.1, 0.2, 0.5),
            position=(0.3, -0.25, 0.25),
            rotation=(-10, 20, -10),
            color=skins.weapon_skins[skins.current_weapon_skin]
        )

    def input(self, key):
        if key == 'left mouse down':
            # Add shoot sound
            # Audio('assets/sounds/shoot.wav')
            Bullet(
                model='sphere',
                color=color.black,
                scale=0.1,
                position=self.world_position,
                rotation=camera.world_rotation
            )
        if key == 'o':
            skins.next_weapon_skin()
            self.color = skins.weapon_skins[skins.current_weapon_skin]


class Bullet(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.world_parent = scene
        self.collider = 'box'
        self.name = 'bullet'

    def update(self):
        self.position += self.forward * time.dt * 100
        dist = distance_2d(self.position, self.start_position)
        if dist > 50:
            destroy(self)
