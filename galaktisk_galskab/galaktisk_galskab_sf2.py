import random

TITLE = "Galaktisk Galskab"
WIDTH = 600
HEIGHT = 600

RUMSKIB_HASTIGHED = 5
RUMSKIB_LIV = 3
TYNGDEKRAFT = 2
SKUD_HASTIGHED = 5
SKUD_VENTETID = 0.2
MAX_AKTIVE_SKUD = 3
UFO_INTERVAL = 0.5
MIN_UFO_X_HASTIGHED = 3
MAX_UFO_X_HASTIGHED = 8
MIN_UFO_Y_HASTIGHED = 2
MAX_UFO_Y_HASTIGHED = 4
STJERNE_HASTIGHED = 3
ANTAL_STJERNER = 50

rumskib = Actor("rumskib1")
rumskib.bottom = HEIGHT - 20
rumskib.x = WIDTH // 2
rumskib.skudklar = True
rumskib.score = 0
rumskib.liv = RUMSKIB_LIV
rumskib.ramt = False

skud_liste = []
ufo_liste = []

music.play("battleship")

sfy=-600

def starfield_draw():
    global sfy
    screen.blit("starfield2.png", (0,sfy))
    sfy = sfy + 2
    if sfy > 0:
        sfy=-1200

def rumskib_boost():
    rumskib.y = rumskib.y - RUMSKIB_HASTIGHED


def rumskib_kanon_klar():
    rumskib.skudklar = True


def rumskib_skyd():
    if rumskib.skudklar is False or rumskib.liv <= 0:
        return
    rumskib.skudklar = False
    clock.schedule_unique(rumskib_kanon_klar, SKUD_VENTETID)
    if len(skud_liste) < MAX_AKTIVE_SKUD:
        skud = Actor("skud1", pos=(rumskib.x, rumskib.top))
        skud_liste.append(skud)
        sounds.laser.play()


def rumskib_bliv_paa_banen():
    if rumskib.top <= 0:
        rumskib.top = 0
    if rumskib.bottom >= HEIGHT:
        rumskib.bottom = HEIGHT
    if rumskib.left < 0:
        rumskib.left = 0
    if rumskib.right > WIDTH:
        rumskib.right = WIDTH


def rumskib_opdater():
    if keyboard.left:
        rumskib.x -= RUMSKIB_HASTIGHED
    if keyboard.right:
        rumskib.x += RUMSKIB_HASTIGHED
    if keyboard.down:
        rumskib.x += RUMSKIB_HASTIGHED
    if keyboard.up:
        rumskib_boost()
        rumskib.image = "rumskib2"
    else:
        rumskib.image = "rumskib1"
    rumskib.y += TYNGDEKRAFT
    rumskib_bliv_paa_banen()


def ufoer_skab_ufo():
    ny_ufo = Actor("ufo1")
    ny_ufo.x = random.randint(0, WIDTH)
    ny_ufo.vx = random.randint(
        MIN_UFO_X_HASTIGHED, MAX_UFO_X_HASTIGHED
    ) * random.choice([-1, 1])
    ny_ufo.vy = random.randint(MIN_UFO_Y_HASTIGHED, MAX_UFO_Y_HASTIGHED)
    ufo_liste.append(ny_ufo)


clock.schedule_interval(ufoer_skab_ufo, UFO_INTERVAL)


def normalt_rumskib():
    rumskib.ramt = False


def ufoer_opdater():
    for ufo in ufo_liste:
        ufo.angle += 1
        ufo.x += ufo.vx
        ufo.y += ufo.vy
        if ufo.x < 0 or ufo.x > WIDTH:
            ufo.vx = -ufo.vx
        if ufo.top > HEIGHT:
            ufo_liste.remove(ufo)
        for anden_ufo in ufo_liste:
            if ufo.colliderect(anden_ufo):
                ufo.vx, anden_ufo.vx = anden_ufo.vx, ufo.vx
        if rumskib.liv > 0 and ufo.colliderect(rumskib):
            ufo_liste.remove(ufo)
            rumskib.liv -= 1
            rumskib.ramt = True
            sounds.boom.play()
            clock.schedule(normalt_rumskib, 1)


def skud_opdater():
    if keyboard.space:
        rumskib_skyd()
    for skud in skud_liste:
        skud.y -= SKUD_HASTIGHED
        if skud.bottom < 0:
            skud_liste.remove(skud)
        else:
            for ufo in ufo_liste:
                if skud.colliderect(ufo):
                    rumskib.score += 1
                    sounds.boom.play()
                    ufo_liste.remove(ufo)
                    skud_liste.remove(skud)


def draw():
    starfield_draw()
    if rumskib.liv > 0:
        rumskib.draw()
        if rumskib.ramt:
            screen.draw.text(
                f"RAMT! {rumskib.liv} skjold tilbage",
                midtop=(WIDTH // 2, HEIGHT // 2),
                fontsize=70,
            )
    else:
        screen.draw.text(f"GAME OVER", midtop=(WIDTH // 2, HEIGHT // 2), fontsize=70)
    for ufo in ufo_liste:
        ufo.draw()
    for skud in skud_liste:
        skud.draw()
    screen.draw.text(
        str(rumskib.score),
        color="white",
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1),
    )


def update():
    if rumskib.liv > 0:
        rumskib_opdater()
    else:
        clock.unschedule(ufoer_skab_ufo)
    skud_opdater()
    ufoer_opdater()
