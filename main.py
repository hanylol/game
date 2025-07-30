from ursina import *
from player import Player
from weapon import Weapon
from enemy import Enemy
import score
from main_menu import MainMenu
from map import MirageMap

app = Ursina()
score.init_score()

def start_game():
    # Map
    mirage_map = MirageMap()

    # Player
    player = Player(position=(0, 1, 0))
    player.controller.cursor.visible = False

    # Weapon
    gun = Weapon()

    # Enemies
    enemy = Enemy(player=player, position=(10, 1, 10))

    # Crosshair
    crosshair = Entity(
        parent=camera.ui,
        model='quad',
        color=color.white,
        scale=0.008,
        rotation_z=45
    )

    # Lighting
    AmbientLight()
    DirectionalLight(direction=(1, -1, 1))

    # Sky
    Sky()


main_menu = MainMenu()
main_menu.start_button.on_click = lambda: {start_game(), main_menu.disable()}


app.run()
