import pgzrun
from random import randint

manzana = Actor("manzana")

def draw():
    screen.clear()
    manzana.draw()

def place_manzana():
    manzana.x = randint(10, 800)
    manzana.y = randint(10, 600)

def on_mouse_down(pos):
    if manzana.collidepoint(pos):
        print("Buen disparo")
        place_manzana()
    else:
        print("Perdiste")
        quit()

place_manzana()
pgzrun.go()