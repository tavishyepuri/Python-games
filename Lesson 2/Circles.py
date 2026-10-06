import pgzrun

WIDTH=400
HEIGHT=400
TITLE="Circles"

def draw():
    screen.fill("aqua")
    screen.draw.filled_circle((200,200),200,"black")
    screen.draw.filled_circle((200,200),190,"white")
    screen.draw.filled_circle((200,200),180,"brown")
    screen.draw.filled_circle((200,200),170,"yellow")
    screen.draw.filled_circle((200,200),160,"red")
    screen.draw.filled_circle((200,200),150,"blue")
    screen.draw.filled_circle((200,200),140,"green")
    screen.draw.filled_circle((200,200),130,"orange")
    screen.draw.filled_circle((200,200),115,"purple")
    screen.draw.filled_circle((200,200),98,"pink")


pgzrun.go()