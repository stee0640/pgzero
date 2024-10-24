TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

bird = Actor('bird1', pos=(75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'), pos=(300, 350))
pipe_bottom = Actor('bottom', anchor=('left', 'top'), pos=(300, 350))

def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(f"Score: {bird.score}", color='white', midtop=(WIDTH//2, 10), fontsize=70, shadow=(1, 1))

def update():
    pass
