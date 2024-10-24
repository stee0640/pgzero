# Pygame Zero "update" funktionen

WIDTH = 800
HEIGHT = 400

alien = Actor('alien')
alien.pos = (400,200)

WIDTH = 800
HEIGHT = 400

alien = Actor("alien")
alien.pos = (400,200)

def draw():
    screen.clear()
    screen.blit('newyork', (0, -300))
    alien.draw()

def update():
    speed = 5
    if keyboard.left: alien.x = alien.x - speed
    if keyboard.right: alien.x = alien.x + speed
    if keyboard.up: alien.y = alien.y - speed
    if keyboard.down: alien.y = alien.y + speed

