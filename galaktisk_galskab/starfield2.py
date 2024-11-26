WIDTH=600
HEIGHT=600

y=-600

def draw():
    global y
    screen.blit("starfield2.png", (0,y))
    y = y + 2
    if y > 0:
        y=-1200

def update():
    pass
