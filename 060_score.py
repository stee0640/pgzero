WIDTH = 800
HEIGHT = 400

alien = Actor("alien")
alien.pos = (400,200)

def update():
    alien.x = alien.x + 3
    if alien.x > 800: alien.x = 0

def set_alien_normal():
    alien.image = "alien"

score = 0
game_over = False

def draw():
    if game_over == False:
        screen.blit("newyork", (0, -300))
        screen.draw.text(f"SCORE: {score}", (20, 20), fontsize=60)
        alien.draw()
    else:
        screen.fill("darkblue")
        screen.draw.text("Game Over", (20, 20), fontsize=60)

def set_alien_hurt():
    global score, game_over
    score += 1
    if score == 5: game_over = True
    alien.image = "alien_hurt"
    clock.schedule_unique(set_alien_normal, 1.0)

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

