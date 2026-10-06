import pgzrun
import random
satellite=Actor("satellite")

def draw():
    screen.fill("purple")
    screen.blit("galaxy",(0,0))
    for i in range(25):
        satellite=Actor("satellite")
        satellite.x=random.randint(0,800)
        satellite.y=random.randint(0,800)
        satellite.draw()


pgzrun.go()