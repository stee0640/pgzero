import random

WIDTH = 600
HEIGHT = 600
KSPEED = 10
KINTERVAL = 0.3
kugle_farver = ["red", "green", "blue"]
kugler = []

def ny_kugle():
    k = Actor(
        random.choice(kugle_farver), pos=(random.randint(0, WIDTH), -75), anchor=("middle", "middle"))
    kugler.append(k)

clock.schedule_interval(ny_kugle, KINTERVAL)

def draw():
    screen.clear()
    for kugle in kugler:
        kugle.draw()

def update():
    for kugle in kugler:
        kugle.y += KSPEED
        if kugle.y > HEIGHT + 75:
            kugler.remove(kugle)
