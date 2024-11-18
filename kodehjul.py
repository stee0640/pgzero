import random
BOGSTAVER = "abcdefghijklmnopqrstuvwxy"
TAL = "0123456789_ /!?=+-"
TEGN = BOGSTAVER + BOGSTAVER.upper() + TAL

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

BRYD_DENNE_KODE_TEKST = "1FtuEjuIj-a-aacl"
kode_nr = 16

eksempel = "Kan I finde koden til pengeskabet? Den er ikke 01234"
kode = kodehjul(eksempel, kode_nr)
print("TEKST :", eksempel)
print("KRYPTO:", kode)
print("BRYD  :", BRYD_DENNE_KODE_TEKST)
