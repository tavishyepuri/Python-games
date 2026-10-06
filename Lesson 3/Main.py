import pgzrun
from random import randint

WIDTH=600
HEIGHT=480
TITLE="Catch the alien"
runner=Actor("alien")
runner.pos=(300,240)
score=0
def draw():
    screen.fill("white")
    runner.draw()
    screen.draw.text(str(score),topleft=(50,50),color="blue")

def on_mouse_down(pos):
    global score
    if runner.collidepoint(pos):
        x=randint(0,600)
        y=randint(0,480)
        score+=1
        runner.pos=(x,y)

def update():
    if keyboard.left:
        runner.x = runner.x - 5
    if keyboard.right:
        runner.x = runner.x + 5
    if keyboard.up:
        runner.y = runner.y - 5
    if keyboard.down:
        runner.y = runner.y + 5






pgzrun.go()