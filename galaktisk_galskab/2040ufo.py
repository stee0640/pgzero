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

SKUD_HASTIGHED = 5
SKUD_VENTETID = 0.2
MAX_AKTIVE_SKUD = 5
rumskib.skudklar = True
skud_liste = []

def rumskib_kanon_klar():
    rumskib.skudklar = True

def rumskib_skyd():
    if rumskib.skudklar is False:
        return
    rumskib.skudklar = False
    clock.schedule_unique(rumskib_kanon_klar, SKUD_VENTETID)
    if len(skud_liste) < MAX_AKTIVE_SKUD:
        skud = Actor("skud1", pos=(rumskib.x, rumskib.top))
        skud_liste.append(skud)

def skud_opdater():
    if keyboard.space:
        rumskib_skyd()
    for skud in skud_liste:
        skud.y -= SKUD_HASTIGHED
        if skud.bottom < 0:
            skud_liste.remove(skud)

UFO_INTERVAL = 1
MIN_UFO_X_HASTIGHED = 2
MAX_UFO_X_HASTIGHED = 7
MIN_UFO_Y_HASTIGHED = 2
MAX_UFO_Y_HASTIGHED = 4
ufo_liste = []

def ufoer_skab_ufo():
    ny_ufo = Actor("ufo1")
    ny_ufo.x = random.randint(0, WIDTH)
    ny_ufo.vx = random.randint(MIN_UFO_X_HASTIGHED, MAX_UFO_X_HASTIGHED) * random.choice([-1, 1])
    ny_ufo.vy = random.randint(MIN_UFO_Y_HASTIGHED, MAX_UFO_Y_HASTIGHED)
    ufo_liste.append(ny_ufo)
clock.schedule_interval(ufoer_skab_ufo, UFO_INTERVAL)


def ufoer_opdater():
    for ufo in ufo_liste:
        ufo.angle += 1
        ufo.x += ufo.vx
        ufo.y += ufo.vy
        if ufo.x < 0 or ufo.x > WIDTH:
            ufo.vx = -ufo.vx
        if ufo.top > HEIGHT:
            ufo_liste.remove(ufo)
        if ufo.colliderect(rumskib):
            print("GAME OVER")
            exit()

def draw():
    screen.clear()
    stjerner_tegn_og_flyt()
    rumskib.draw()
    for ufo in ufo_liste: ufo.draw()
    for skud in skud_liste: skud.draw()

def update():
    rumskib_opdater()
    ufoer_opdater()
    skud_opdater()

