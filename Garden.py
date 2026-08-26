import pgzrun
import random
WIDTH = 1500
HEIGHT = 900
TITLE = "Garden full of butterflies"
Garden = Actor ("garden")

butterflies = []
next_butterflies = 0
number_of_butterflies = 8
lines = []

for i in range(8):
    butterfly = Actor("butterfly")
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    butterfly.pos = (x,y)
    butterflies.append(butterfly)
    
def draw():
    Garden.draw()
    number = 0
    for butterfly in butterflies:
             butterfly.draw()
             print(butterfly.pos)
             screen.draw.text(str(number), (butterfly.pos[0], butterfly.pos[1]), color = 'black')
             number = number +1
    for line in  lines:      
        screen.draw.line(line[0], line [1], color = "white")


def on_mouse_down(pos):
      global next_butterflies, number_of_butterflies, lines
      if next_butterflies < number_of_butterflies:
         if butterflies[next_butterflies].collidepoint(pos):
            if next_butterflies:
                 lines.append((butterflies[next_butterflies -1].pos,butterflies[next_butterflies].pos))
            next_butterflies = next_butterflies +1
         else:
            lines = []
            next_butterflies = 0


pgzrun.go()