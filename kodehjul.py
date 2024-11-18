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

BRYD_DENNE_KODE_TEKST = "s?34!T4-TJKJKKMV"

kode_nr = 52
eksempel = "Kan I finde koden til pengeskabet? Den er ikke 01234"
kode = kodehjul(eksempel, kode_nr)
print("TEKST :", eksempel)
print("KRYPTO:", kode)
print("BRYD  :", BRYD_DENNE_KODE_TEKST)
