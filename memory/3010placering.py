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
    #kort.image = kort.billede
    kort.topleft = (soejle_koordinat(kort_nr), raekke_koordinat(kort_nr))
    kort_liste.append(kort)

def draw():
    for kort_nr in range(0, KORTANTAL):
        kort_liste[kort_nr].draw()

def update():
    pass
