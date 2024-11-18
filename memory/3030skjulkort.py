import random

BILLEDSTR = 100
GAB = 20
TOP = 50
SOEJLER = 7
RAEKKER = 4

BILLEDANTAL = SOEJLER * RAEKKER // 2
KORTANTAL = BILLEDANTAL * 2

WIDTH = SOEJLER * (BILLEDSTR + GAB) + GAB
HEIGHT = RAEKKER * (BILLEDSTR + GAB) + GAB + TOP

VENTETID = 1
vent_paa_ny_tur = False

billed_liste = [billed_nr for billed_nr in range(BILLEDANTAL)] * 2
random.shuffle(billed_liste)

def soejle_koordinat(kort_nr):
    soejle = kort_nr % SOEJLER
    return soejle * (BILLEDSTR + GAB) + GAB

def raekke_koordinat(kort_nr):
    raekke = kort_nr // SOEJLER
    return raekke * (BILLEDSTR + GAB) + GAB + TOP


kort_liste = []
for kort_nr in range(KORTANTAL):
    kort = Actor("bagside")
    kort.billede = str(billed_liste[kort_nr])
    kort.topleft = (soejle_koordinat(kort_nr), raekke_koordinat(kort_nr))
    kort_liste.append(kort)

viste_kort_liste = []

def skjul_viste_kort():
    global viste_kort_liste, vent_paa_ny_tur
    for kort_nr in viste_kort_liste:
        kort_liste[kort_nr].image = "bagside"
    viste_kort_liste = []
    vent_paa_ny_tur = False

def vis_kort(kort_nr):
    global viste_kort_liste, vent_paa_ny_tur
    kort_liste[kort_nr].image = kort_liste[kort_nr].billede
    viste_kort_liste.append(kort_nr)
    if len(viste_kort_liste) == 2:
        vent_paa_ny_tur = True
        clock.schedule_unique(skjul_viste_kort, VENTETID)

def vaelg_kort(kort_nr):
    if (
        len(viste_kort_liste) == 2
        or kort_nr in viste_kort_liste
    ):
        return False
    vis_kort(kort_nr)

def on_mouse_down(pos):
    if vent_paa_ny_tur:
        return
    for kort_nr in range(KORTANTAL):
        if kort_liste[kort_nr].collidepoint(pos):
            vaelg_kort(kort_nr)
            return

def draw():
    for kort_nr in range(0, KORTANTAL):
        kort_liste[kort_nr].draw()

def update():
    pass
