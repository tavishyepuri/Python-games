import pgzrun

WIDTH=400
HEIGHT=400
TITLE="Squares"

def draw():
    screen.fill("aqua")
    r=Rect(20,20,360,360)
    screen.draw.filled_rect(r,"black")
    r=Rect(40,40,320,320)
    screen.draw.filled_rect(r,"white")
    r=Rect(60,60,300,300)
    screen.draw.filled_rect(r,"brown")
    r=Rect(80,80,280,280)
    screen.draw.filled_rect(r,"yellow")
    r=Rect(100,100,260,260)
    screen.draw.filled_rect(r,"red")
    r=Rect(120,120,240,240)
    screen.draw.filled_rect(r,"blue")
    r=Rect(140,140,220,220)
    screen.draw.filled_rect(r,"green")
    r=Rect(160,160,200,200)
    screen.draw.filled_rect(r,"orange")
    r=Rect(180,180,180,180)
    screen.draw.filled_rect(r,"purple")
    r=Rect(200,200,160,160)
    screen.draw.filled_rect(r,"pink")
    r=Rect(220,220,140,140)


pgzrun.go()