import random

BILLEDSTR = 100
GAB = 20
TOP = 50
VENTETID = 1
SOEJLER = 7
RAEKKER = 4
BILLEDANTAL = SOEJLER * RAEKKER // 2
KORTANTAL = BILLEDANTAL * 2
HUSKEDE = 6
WIDTH = SOEJLER * (BILLEDSTR + GAB) + GAB
HEIGHT = RAEKKER * (BILLEDSTR + GAB) + GAB + TOP

score = 0
computer_score = 0
computers_tur = False
vent_paa_ny_tur = False
tur_tekst = ""
kort_liste = []
fundne_kort_liste = []
viste_kort_liste = []
husker = []

billed_liste = [billed_nr for billed_nr in range(BILLEDANTAL)] * 2
random.shuffle(billed_liste)

def soejle_koordinat(kort_nr):
    soejle = kort_nr % SOEJLER
    return soejle * (BILLEDSTR + GAB) + GAB

def raekke_koordinat(kort_nr):
    raekke = kort_nr // SOEJLER
    return raekke * (BILLEDSTR + GAB) + GAB + TOP


for kort_nr in range(KORTANTAL):
    kort = Actor("bagside")
    kort.billede = str(billed_liste[kort_nr])
    kort.topleft = (soejle_koordinat(kort_nr), raekke_koordinat(kort_nr))
    kort_liste.append(kort)


def skjul_viste_kort():
    global viste_kort_liste, vent_paa_ny_tur
    for kort_nr in viste_kort_liste:
        kort_liste[kort_nr].image = "bagside"
    viste_kort_liste = []
    vent_paa_ny_tur = False


def skift_tur():
    global computers_tur, vent_paa_ny_tur
    vent_paa_ny_tur = True
    if computers_tur:
        computers_tur = False
    else:
        computers_tur = True
    clock.schedule_unique(skjul_viste_kort, VENTETID)


def valgte_kort_matcher():
    kort_A = kort_liste[viste_kort_liste[0]]
    kort_B = kort_liste[viste_kort_liste[1]]
    return kort_A.billede == kort_B.billede


def tjek_to_kort():
    global fundne_kort_liste, viste_kort_liste, score, computer_score
    if valgte_kort_matcher():
        if computers_tur:
            computer_score += 1
        else:
            score += 1
        fundne_kort_liste += viste_kort_liste
        viste_kort_liste = []
    else:
        skift_tur()


def vis_kort(kort_nr):
    kort_liste[kort_nr].image = kort_liste[kort_nr].billede
    husker.append((kort_nr, kort_liste[kort_nr].billede))
    if len(husker) > HUSKEDE:
        husker.pop(0)
    viste_kort_liste.append(kort_nr)
    if len(viste_kort_liste) == 2:
        tjek_to_kort()


def vaelg_kort(kort_nr):
    if (
        len(viste_kort_liste) == 2
        or kort_nr in viste_kort_liste
        or kort_nr in fundne_kort_liste
    ):
        return False
    vis_kort(kort_nr)
    return True

def computer_find_et_match(kort_nr, billede):
    for andet_kort_nr, andet_billede in husker:
        if kort_nr == andet_kort_nr:
            continue
        if billede == andet_billede:
            if kort_nr in viste_kort_liste:
                return andet_kort_nr
            else:
                return kort_nr
    return None

def computer_vaelg_et_ukendt_kort():
    huskede_kort = [kort_nr for kort_nr, _ in husker]
    kendte_kort = huskede_kort + fundne_kort_liste
    resterende_kort = [k for k in range(KORTANTAL) if not k in kendte_kort]
    return random.choice(resterende_kort)

def computer_tjek_hukommelsen():
    matchende_kort_nr = None
    for kort_nr, billede in husker:
        if kort_nr in fundne_kort_liste:
            continue
        matchende_kort_nr = computer_find_et_match(kort_nr, billede)
        if matchende_kort_nr is not None:
            return matchende_kort_nr
    return computer_vaelg_et_ukendt_kort()

def computer_vaelg_kort():
    if vent_paa_ny_tur or not computers_tur:
        return
    kort_forslag = computer_tjek_hukommelsen()
    vaelg_kort(kort_forslag)


clock.schedule_interval(computer_vaelg_kort, 1)


def on_mouse_down(pos):
    if vent_paa_ny_tur or computers_tur:
        return
    for kort_nr in range(KORTANTAL):
        if kort_liste[kort_nr].collidepoint(pos):
            vaelg_kort(kort_nr)
            return


def draw():
    screen.clear()
    screen.draw.text(tur_tekst, midtop=(WIDTH // 2, GAB), fontsize=40, color="maroon")
    screen.draw.text(f"Spiller: {score:2}", topleft=(GAB, GAB), fontsize=40)
    screen.draw.text(
        f"Computer: {computer_score:2}", topright=(WIDTH - GAB, GAB), fontsize=40
    )
    for kort_nr in range(0, KORTANTAL):
        kort_liste[kort_nr].draw()


def update():
    global tur_tekst
    if len(fundne_kort_liste) == KORTANTAL:
        if computer_score > score:
            tur_tekst = "JEG VANDT"
        elif score > computer_score:
            tur_tekst = "DU VANDT"
        else:
            tur_tekst = "UAFGJORT"
        clock.unschedule(computer_vaelg_kort)
    elif vent_paa_ny_tur:
        tur_tekst = "Turen skifter"
    elif computers_tur:
        tur_tekst = "Min tur"
    else:
        tur_tekst = "Din tur"
