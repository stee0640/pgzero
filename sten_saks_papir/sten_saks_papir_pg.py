import random

WIDTH = 800
HEIGHT = 400

bedst = pc_valg = dit_valg = ""
pc = dig = 0

sten = Actor("sten", pos=(200, 200))
saks = Actor("saks", pos=(400, 200))
papir = Actor("papir", pos=(600, 200))


def sammenlign_valg(pc_valg, dit_valg):
    if pc_valg == dit_valg:
        return "uafgjort"
    if (
        (dit_valg == "sten" and pc_valg == "saks")
        or (dit_valg == "saks" and pc_valg == "papir")
        or (dit_valg == "papir" and pc_valg == "sten")
    ):
        return "dig"
    return "pc"


def on_mouse_down(pos):
    global pc, dig, bedst, pc_valg, dit_valg
    if sten.collidepoint(pos):
        dit_valg = "sten"
    elif saks.collidepoint(pos):
        dit_valg = "saks"
    elif papir.collidepoint(pos):
        dit_valg = "papir"
    else:
        return
    pc_valg = random.choice(["sten", "saks", "papir"])
    bedst = sammenlign_valg(pc_valg, dit_valg)
    if bedst == "pc":
        pc += 1
    elif bedst == "dig":
        dig += 1


def draw():
    screen.clear()
    sten.draw()
    saks.draw()
    papir.draw()
    screen.draw.text(
        "Sten, saks, papir", midtop=(WIDTH // 2, 25), fontsize=50, color="white"
    )
    if dit_valg != "":
        resultat = f"Du valgte: {dit_valg}  -  Pc valgte: {pc_valg}  -  Vinder: {bedst}"
    else:
        resultat = ""
    screen.draw.text(resultat, midtop=(WIDTH // 2, 80), fontsize=40, color="yellow")
    screen.draw.text(
        f"pc: {pc}  -  dig: {dig}",
        midtop=(WIDTH // 2, HEIGHT - 50),
        fontsize=40,
        color="yellow",
    )


def update():
    pass
