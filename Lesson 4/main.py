import pgzrun
import random
bee=Actor("bee")
flower=Actor("flower 1")
nectar = 0
def draw():
    screen.fill("turquoise")
    bee.draw()
    flower.draw()
    screen.draw.text("Nectar : "+str(nectar),(100,100),fontsize=30,color="red")


def update():
    global nectar
    if keyboard.left:
        bee.x = bee.x - 5
    if keyboard.right:
        bee.x = bee.x + 5
    if keyboard.up:
        bee.y = bee.y - 5
    if keyboard.down:
        bee.y = bee.y + 5

    if bee.colliderect(flower):
        flower.x = random.randint(0,500)
        flower.y = random.randint(0,500)
        nectar = nectar + 1

pgzrun.go()