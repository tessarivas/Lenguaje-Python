import pgzrun

carro1 = Actor("carro1", (150, 300))
carro2 = Actor("carro2", (150, 400))

tecla_presionada_carro1 = None
tecla_presionada_carro2 = None

def draw():
    screen.clear()
    screen.fill("black")
    draw_linea_meta()
    draw_linea_texto()
    carro1.draw()
    carro2.draw()

def draw_linea_meta():
    screen.draw.filled_rect(Rect((700, 160), (50, 300)), (255, 243, 0))

def draw_linea_texto():
    screen.draw.text("- - - M E T A - - -", midleft=(725, 380), angle=90, color="black", fontsize=30)

def avanzar(carro):
    carro.x += 100
    if carro.x >= 700: 
        print(f"{carro.image.upper()} LLEGO A LA META!")
        quit()

def on_key_down(key):
    global tecla_presionada_carro1, tecla_presionada_carro2
    
    if key == keys.UP:
        tecla_presionada_carro1 = key.name
        print("CARRO 1 (Rojo) AVANZA")
        avanzar(carro1)
    
    if key == keys.W:
        tecla_presionada_carro2 = key.name
        print("CARRO 2 (Azul) AVANZA")
        avanzar(carro2)

pgzrun.go()
