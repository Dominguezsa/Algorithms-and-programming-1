from Library.gamelib import *
from SokobanGame.View.Constants import IMAGE_SIZE, diccionario_caracteres


def juego_mostrar(juego, indice, ancho, alto, pistas, mostrar_pistas):
    """Actualiza la ventana"""
    medio = ancho // 2  # medio de la ventana en el eje x
    columnas_grilla = len(juego[0])
    medio_vertical = alto // 2
    horizontal = (ancho - columnas_grilla * IMAGE_SIZE) // 2  # "horizontal" es el espacio en el eje x que hay entre
    # el borde de la ventana y la grilla
    max_horizontal = 0
    vertical = (alto - len(juego) * IMAGE_SIZE) // 2  # "vertical" es el espacio en el eje y que hay entre el borde
    # de la ventana y la grilla
    draw_text('SokoBan', 50, 20)
    draw_text(f'Nivel: {indice + 1}', ancho - 50, 20)
    if not pistas.esta_vacia():
        draw_text('HAY PISTA!', medio, vertical - 15)
    # mostar imagenes:
    for i in juego:
        for j in i:
            draw_image('img/empty.gif', horizontal, vertical)
            if j == "+":
                draw_image('img/goal.gif', horizontal, vertical)
                draw_image('img/player.gif', horizontal, vertical)
            else:
                draw_image(f'img/{diccionario_caracteres[j]}.gif', horizontal, vertical)
            horizontal += IMAGE_SIZE
            max_horizontal = max(horizontal, max_horizontal)
        horizontal = (ancho - columnas_grilla * IMAGE_SIZE) // 2  # vuelve al x inicial
        vertical += IMAGE_SIZE  # cambia de fila
    draw_text("See Keys ('H')", medio, (alto + vertical) // 2, fill="green")
    if mostrar_pistas:
        draw_rectangle((ancho - columnas_grilla * IMAGE_SIZE) // 2, (alto - len(juego) * IMAGE_SIZE) // 2,
                       max_horizontal, vertical)
        draw_text('P: pista', medio, medio_vertical - 50, fill="black")
        draw_text('R: reiniciar', medio, medio_vertical - 25, fill="black")
        draw_text('ESC: salir', medio, medio_vertical, fill="black")
        draw_text('T: rehacer', medio, medio_vertical + 25, fill="black")
        draw_text('B: deshacer', medio, medio_vertical + 50, fill="black")


def mostrar_eleccion(ancho, alto):
    draw_begin()
    draw_text('Siguiente', ancho * 0.25, alto * 0.5, size=18, fill='green')
    draw_text('Exit', ancho * 0.75, alto * 0.5, size=18, fill='red')
    draw_text('Clickea:', ancho * 0.5, 20, )
    draw_line(ancho // 2, 35, ancho // 2, alto, width=2, fill='white')
    draw_end()


def find_ancho_alto(juego):
    columnas_grilla = len(juego[0])
    ancho = columnas_grilla * IMAGE_SIZE + (columnas_grilla * IMAGE_SIZE) * 0.5
    alto = len(juego) * IMAGE_SIZE + len(juego) * IMAGE_SIZE * 0.4
    return ancho, alto
