import random
TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', pos=(75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'), pos=(300, 350))
pipe_bottom = Actor('bottom', anchor=('left', 'top'), pos=(300, 350))

GAP = 130
SPEED = 3
def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

reset_pipes()

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        if not bird.dead:
            bird.score += 1

FLAP_STRENGTH = 4
GRAVITY = 0.3
def on_key_down():
    if not bird.dead:
        bird.vy = -FLAP_STRENGTH

def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += (uy + bird.vy) / 2

    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vy = 0
        reset_pipes()


def update():
    update_pipes()
    update_bird()

def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(f"Score: {bird.score}", color='white', midtop=(WIDTH//2, 10), fontsize=70, shadow=(1, 1))

