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

def set_alien_normal():
    alien.image = "alien"

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.image = "alien_hurt"
        clock.schedule_unique(set_alien_normal, 1.0)
        sounds.eep.play()
