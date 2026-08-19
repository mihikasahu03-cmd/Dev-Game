import pgzrun
import random
WIDTH = 1500
HEIGHT = 900
TITLE = "Garden full of butterflies"
Garden = Actor("garden")

butterflies = []

for i in range(8):
    butterfly = Actor("butterfly")
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    butterfly.pos = (x,y)
    butterflies.append(butterfly)
    
def draw():
    Garden.draw()
    for butterfly in butterflies:
             butterfly.draw()    

pgzrun.go()