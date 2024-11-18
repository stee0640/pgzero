WIDTH = 600
HEIGHT = 600

RUMSKIB_HASTIGHED = 5
TYNGDEKRAFT = 2

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT - 20
rumskib.x = WIDTH // 2

def rumskib_bliv_paa_banen():
    if rumskib.top <= 0: rumskib.top = 0
    if rumskib.bottom >= HEIGHT: rumskib.bottom = HEIGHT
    if rumskib.left < 0: rumskib.left = 0
    if rumskib.right > WIDTH: rumskib.right = WIDTH

def rumskib_boost():
    rumskib.y = rumskib.y - RUMSKIB_HASTIGHED

def rumskib_opdater():
    if keyboard.left: rumskib.x -= RUMSKIB_HASTIGHED
    if keyboard.right: rumskib.x += RUMSKIB_HASTIGHED
    if keyboard.down: rumskib.y += RUMSKIB_HASTIGHED
    if keyboard.up:
        rumskib_boost()
        rumskib.image = "rumskib2"
    else:
        rumskib.image = "rumskib1"
    rumskib.y += TYNGDEKRAFT
    rumskib_bliv_paa_banen()

def draw():
    screen.clear()
    rumskib.draw()

def update():
    rumskib_opdater()
