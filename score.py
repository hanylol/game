from ursina import *

score = 0
score_text = Text(
    text=f'Score: {score}',
    position=(-0.8, 0.45),
    scale=2,
    color=color.white
)

def add_score(amount):
    global score
    score += amount
    score_text.text = f'Score: {score}'
