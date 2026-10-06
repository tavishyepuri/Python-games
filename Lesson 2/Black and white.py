import pgzrun

WIDTH=400
HEIGHT=400
TITLE="Black and white circles"
colors=["black","white","black","white","black","white","black","white"]
def draw():
    screen.fill("white")
    for i in range(0,7,1):
        screen.draw.filled_circle((200,200),200-i*20,colors[i])


pgzrun.go()