from pygame import mouse
WIDTH = 400
HEIGHT = 400
GROUND = HEIGHT - 100

alien = Actor("alien")
splat = Actor("splat", pos = (300, GROUND))
alien.pos = (WIDTH // 2, GROUND)

def draw():
    screen.clear()
    screen.fill((128, 40, 40))
    screen.draw.line((10,10), (180,180), color="yellow")
    screen.draw.filled_rect(Rect((20, 20), (100, 100)), color="blue")
    screen.draw.text("Hello World", (40,40), angle=-45)
    screen.draw.textbox("Hello World", Rect((100, 200), (200,100)), angle=45)
    alien.draw()
    splat.draw()

def jump_up():
    animate(alien, y=GROUND - 200, tween="linear", duration=0.2, on_finished=fall_down)

def fall_down():
    animate(alien, y=GROUND, tween="bounce_end", duration=0.5)

#def on_mouse_move(pos):
#    print(mouse.get_pos())
#    alien.angle = alien.angle_to(pos)

def update():
    if keyboard.space:
        jump_up()
    if keyboard.left:
        alien.x -= 5
    elif keyboard.right:
        alien.x += 5
