import random
TING = ["sten", "saks", "papir"]

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

pc = dig = 0
while True:
    dit_valg = ""
    while dit_valg not in TING:
        dit_valg = input("sten, saks eller papir: ")
    pc_valg = random.choice(TING)
    print("Jeg valgte:", pc_valg)
    bedst = sammenlign_valg(pc_valg, dit_valg)
    print("Bedst:", bedst)
    if bedst == "pc": pc += 1
    if bedst == "dig": dig += 1
    print(f"Points PC: {pc} Dig: {dig}")
