WIDTH = 800
HEIGHT = 400

alien = Actor("alien")
alien.pos = (400,200)

def draw():
    screen.blit("newyork", (0, -300))
    alien.draw()

def update():
    alien.x = alien.x + 3
    if alien.x > 800: alien.x = 0
