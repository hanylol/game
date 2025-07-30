from ursina import *
import score

class Enemy(Entity):
    def __init__(self, player, position=(0, 1, 0)):
        super().__init__(
            model='cube',
            scale=1,
            position=position,
            color=color.red,
            collider='box'
        )
        self.health = 100
        self.player = player

    def update(self):
        self.look_at(self.player)
        self.position += self.forward * time.dt * 1

        hit_info = self.intersects()
        if hit_info.hit:
            if 'bullet' in hit_info.entity.name:
                self.health -= 25
                if self.health <= 0:
                    destroy(self)
                    score.add_score(10)
                destroy(hit_info.entity)
            if hit_info.entity == self.player.controller:
                self.player.health -= 10
