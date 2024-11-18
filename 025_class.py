class Rumskib:
    def __init__(self, navn):
        self.navn = navn
        self.antal_skud = 5

    def skyd(self):
        if self.antal_skud > 0:
            print(f"ZAP! ({self.navn})")
            self.antal_skud -= 1
        else:
            print(f"KLIK! ({self.navn})")

nebula = Rumskib("Nebula Phantom")
vortex = Rumskib("Vortex Serpent")

nebula.antal_skud = 0
nebula.skyd()
vortex.skyd()
