from ursina import *

player_skins = [
    color.cyan,
    color.red,
    color.green,
    color.blue
]

weapon_skins = [
    color.dark_gray,
    color.gold,
    color.brown
]

current_player_skin = 0
current_weapon_skin = 0

def next_player_skin():
    global current_player_skin
    current_player_skin = (current_player_skin + 1) % len(player_skins)

def next_weapon_skin():
    global current_weapon_skin
    current_weapon_skin = (current_weapon_skin + 1) % len(weapon_skins)
