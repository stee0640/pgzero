import random
TING = ["sten", "saks", "papir"]

def sammenlign_valg(pc_valg, dit_valg):
    if pc_valg == dit_valg:
        return "uafgjort"
    if pc_valg == "sten":
        if dit_valg == "papir": bedst = "dig"
        else: bedst = "pc"
    if pc_valg == "saks":
        if dit_valg == "sten": bedst = "dig"
        else: bedst = "pc"
    if pc_valg == "papir":
        if dit_valg == "saks": bedst = "dig"
        else: bedst = "pc"
    return bedst

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
