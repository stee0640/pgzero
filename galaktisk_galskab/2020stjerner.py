import random
WIDTH = 600
HEIGHT = 600

RUMSKIB_HASTIGHED = 5
TYNGDEKRAFT = 2

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT - 20
rumskib.x = WIDTH // 2

STJERNE_HASTIGHED = 3
ANTAL_STJERNER = 50
stjerne_liste = [
    (random.randint(0, WIDTH),random.randint(0, HEIGHT))
    for _ in range(ANTAL_STJERNER)
]

def stjerner_tegn_og_flyt():
    for nr, (stjerne_x, stjerne_y) in enumerate(stjerne_liste):
        screen.draw.filled_circle((stjerne_x, stjerne_y), 2, "white")
        if stjerne_y > HEIGHT:
            stjerne_liste[nr] = (random.randint(0, WIDTH), 0)
        else:
            stjerne_liste[nr] = (stjerne_x, stjerne_y + STJERNE_HASTIGHED)

def draw():
    screen.clear()
    stjerner_tegn_og_flyt()
    rumskib.draw()

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

def update():
    rumskib_opdater()
