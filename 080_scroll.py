import random
WIDTH = 800
HEIGHT = 400

alien = Actor("alien")
alien.pos = (200,200)

def set_normal():
    alien.image = "alien"
    alien.angle = 0

def update_rumskib():
    rumskib.x -= 8
    if rumskib.right < 0:
        rumskib.center = (WIDTH+200, random.randint(60, HEIGHT-60))
    if rumskib.colliderect(alien):
        alien.image = "alien_hurt"
        animate(alien, angle=360, on_finished=set_normal)

rumskib = Actor("rumskib", center=(WIDTH+200, random.randint(60, HEIGHT-60)))
space_x = 0

def draw():
    screen.blit("space2", (space_x, 0))
    rumskib.draw()
    alien.draw()

def update():
    global space_x
    space_x -= 2
    if space_x <= -WIDTH * 2: space_x = 0
    update_rumskib()
    if keyboard.up: alien.y -= 5
    if keyboard.down: alien.y += 5
