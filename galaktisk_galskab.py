import random
TITLE = 'Galaktisk Galskab'
WIDTH = 600
HEIGHT = 600

RUMSKIB_HASTIGHED = 5
TYNGDEKRAFT = 2
SKUD_HASTIGHED = 5
SKUD_VENTETID = 0.2
MAX_AKTIVE_SKUD = 5
UFO_INTERVAL = 1
MIN_UFO_X_HASTIGHED = 2
MAX_UFO_X_HASTIGHED = 7
MIN_UFO_Y_HASTIGHED = 2
MAX_UFO_Y_HASTIGHED = 4
STJERNE_HASTIGHED = 3
ANTAL_STJERNER = 50

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT - 20
rumskib.x = WIDTH // 2
rumskib.skudklar = True
rumskib.score = 0

skud_liste = []
ufo_liste = []

stjerne_liste = [(random.randint(0,WIDTH), random.randint(0, HEIGHT)) for _ in range(ANTAL_STJERNER)]
def stjerner_tegn_og_flyt():
    for nr, (stjerne_x,stjerne_y) in enumerate(stjerne_liste):
        screen.draw.filled_circle((stjerne_x,stjerne_y), 2, "white")
        if stjerne_y > HEIGHT:
            stjerne_liste[nr] = (random.randint(0,WIDTH), 0)
        else:
            stjerne_liste[nr] = (stjerne_x, stjerne_y + STJERNE_HASTIGHED)

def rumskib_boost():
    rumskib.y = rumskib.y - RUMSKIB_HASTIGHED

def rumskib_kanon_klar():
    rumskib.skudklar = True

def rumskib_skyd():
    if rumskib.skudklar == False:
        return
    rumskib.skudklar = False
    clock.schedule_unique(rumskib_kanon_klar, SKUD_VENTETID)
    if len(skud_liste) < MAX_AKTIVE_SKUD:
        skud = Actor("skud1", pos=(rumskib.x, rumskib.top))
        skud_liste.append(skud)

def rumskib_bliv_paa_banen():
    if rumskib.top <= 0: rumskib.top = 0
    if rumskib.bottom >= HEIGHT: rumskib.bottom = HEIGHT
    if rumskib.left < 0: rumskib.left = 0
    if rumskib.right > WIDTH: rumskib.right = WIDTH

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
    if keyboard.space:
        rumskib_skyd()

def ufoer_skab_ufo():
    ny_ufo = Actor("ufo1")
    ny_ufo.nr = 1
    ny_ufo.x = random.randint(0, WIDTH)
    ny_ufo.vx = random.randint(MIN_UFO_X_HASTIGHED, MAX_UFO_X_HASTIGHED) * random.choice([-1,1])
    ny_ufo.vy = random.randint(MIN_UFO_Y_HASTIGHED, MAX_UFO_Y_HASTIGHED)
    ufo_liste.append(ny_ufo)
clock.schedule_interval(ufoer_skab_ufo, UFO_INTERVAL)

def ufoer_skift_billede():
    for ufo in ufo_liste:
        if ufo.nr == 1: ufo.nr = 2
        else: ufo.nr = 1
        ufo.image = "ufo" + str(ufo.nr)
clock.schedule_interval(ufoer_skift_billede, 0.1)

def ufoer_opdater():
    for ufo in ufo_liste:
        ufo.x += ufo.vx
        ufo.y += ufo.vy
        if ufo.x < 0 or ufo.x > WIDTH:
            ufo.vx = -ufo.vx
        if ufo.top > HEIGHT:
            ufo_liste.remove(ufo)
        for anden_ufo in ufo_liste:
            if ufo.colliderect(anden_ufo):
                ufo.vx, anden_ufo.vx = anden_ufo.vx, ufo.vx
        if ufo.colliderect(rumskib):
            print(f"GAME OVER")
            print(f"Score: {rumskib.score}")
            exit()

def skud_opdater():
    for skud in skud_liste:
        skud.y -= SKUD_HASTIGHED
        if skud.bottom < 0:
            skud_liste.remove(skud)
        for ufo in ufo_liste:
            if skud.colliderect(ufo):
                rumskib.score += 1
                ufo_liste.remove(ufo)
                skud_liste.remove(skud)

def draw():
    screen.clear()
    stjerner_tegn_og_flyt()
    rumskib.draw()
    for ufo in ufo_liste:
        ufo.draw()
    for skud in skud_liste:
        skud.draw()
    screen.draw.text(str(rumskib.score), color='white', midtop=(WIDTH//2, 10), fontsize=70, shadow=(1, 1))

def update():
    rumskib_opdater()
    skud_opdater()
    ufoer_opdater()
