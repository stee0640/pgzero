BOGSTAVER = "abcdefghijklmnopqrstuvwxyz"
TEGN = BOGSTAVER + BOGSTAVER.upper() + "0123456789_ /!?=+-"

def kodehjul(tekst, kode_nr):
    resultat = ""
    for bogstav in tekst:
        nr = TEGN.find(bogstav)
        if nr == -1:
            nyt_bogstav = bogstav
        else:
            nyt_nr = (nr + kode_nr) % len(TEGN)
            nyt_bogstav = TEGN[nyt_nr]
        resultat += nyt_bogstav
    return resultat

kode = "vm3?j3?f3cjqhlg9e?kl?j5"

def draw():
    resultat = kodehjul(tekst=kode, kode_nr=0)
    screen.draw.text(resultat, (30, 30))

