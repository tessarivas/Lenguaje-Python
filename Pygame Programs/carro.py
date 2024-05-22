import pgzrun

carro1 = Actor("carro", (150, 350))

def draw():
    screen.clear()
    screen.fill(color="black")
    draw_linea_meta()
    draw_linea_texto()
    carro1.draw()

def draw_linea_meta():
    linea_meta = screen.draw.filled_rect(Rect(700, 160, 50, 300), (255, 243, 0))
    return linea_meta

def draw_linea_texto():
    linea_texto = screen.draw.text("- - - M E T A - - -", midleft=(725, 380), angle=90, color="black", fontsize=30)
    return linea_texto

def avanzar():
    carro1.x += 100
    if carro1.x >= 600: 
        print("LLEGO A LA META")
        quit()

def on_mouse_down(pos):
    if carro1.collidepoint(pos):
        print("CLICK")
        avanzar()
    else:
        print("CLICK AFUERA")
        quit()

pgzrun.go()

## FUNCIONES
# screen.fill(color) 
# screen.draw.line(x, y, color)
# screen.draw.text(string, (x, y), fontsize, color)
# objetoCarro.collidepoint(x, y)
# objetoCarro.x
# objetoCarro.y
# quit()

### LOGICA
# avanzar con los clicks 100 hacia la derecha hasta alcanzar 
# la meta, ya alcanzada se cierra el programa