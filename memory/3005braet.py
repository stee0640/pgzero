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

print(billed_liste)