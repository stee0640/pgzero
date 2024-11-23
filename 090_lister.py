import random

WIDTH = 600
HEIGHT = 600
SPEED = 10
INTERVAL = 0.4
planeter = []

def ny_planet():
    k = Actor("planet")
    k.anchor = ("middle", "middle")
    k.pos = (random.randint(0, WIDTH), -100)
    planeter.append(k)

def draw():
    screen.clear()
    for planet in planeter:
        planet.draw()
    screen.draw.text(str(len(planeter)), (20,20))

def update():
    for planet in planeter:
        planet.y += SPEED
        if planet.y > HEIGHT + 100:
            planeter.remove(planet)


clock.schedule_interval(ny_planet, INTERVAL)
