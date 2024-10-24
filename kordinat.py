WIDTH = 400
HEIGHT = 400

def draw():
    screen.clear()
    screen.draw.text("X", (200,70))
    screen.draw.line((100,100), (300,100), "white")
    screen.draw.text("Y", (70, 200))
    screen.draw.line((100,100), (100,300), "white")
    for x in range(100,301, 100):
        for y in range(100, 301, 100):
            screen.draw.filled_circle((x,y), 10, "red")
            screen.draw.text(f"({x},{y})", (x,y), fontsize=20)
