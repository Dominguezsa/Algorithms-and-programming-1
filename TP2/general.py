import gamelib
CUADRADO = 32 #tamaño de un lado de un cuadrado dentro de la grilla
coords = {"NORTE": (0, -1), "SUR": (0, 1), "ESTE": (1, 0), "OESTE": (-1, 0)}

def teclas(archivo):
    """Crea un diccionario <tecla> = <direccion> o <accion>"""
    diccionario = {}
    with open(archivo, 'r') as f:
        for linea in f:
            if linea == "\n":
                continue
            tecla, clave = linea.rstrip("\n").replace(" ", "").split("=")
            clave = coords.get(clave, clave)
            diccionario[tecla.lower()] = clave
    return diccionario

def niveles_en_lista(archivo):
    """Crea una lista con los niveles del archivo dado"""
    lista_definitiva = []
    listas = []
    with open (archivo, "r") as f:
        for linea in f:
            if linea == "\n":
                lista_definitiva.append(listas)
                listas = []
            if linea[0] != "#" and linea[0] != " ":
                continue
            else:
                listas.append(linea.rstrip("\n"))
    return lista_definitiva

def juego_mostrar(juego, indice, ancho, alto):
    """Actualiza la ventana"""
    medio = ancho//2 #medio de la ventana en el eje x
    columnas_grilla = len(juego[0])
    horizontal = (ancho - columnas_grilla * CUADRADO) // 2 # "horizontal" es el espacio en el eje x que hay entre el borde de la ventana y la grilla
    vertical = (alto - len(juego) * CUADRADO) // 2 # "vertical" es el espacio en el eje y que hay entre el borde de la ventana y la grilla
    gamelib.draw_text('SokoBan', 50, 20)
    gamelib.draw_text(f'Nivel: {indice+1}', ancho-50, 20)
    gamelib.draw_text('Presione (r) para reiniciar nivel', medio, alto-vertical//2-10)
    gamelib.draw_text('Presione (esc) para salir', medio, alto-vertical+10)

    #mostar imagenes:
    for i in juego:
        for j in i:
            gamelib.draw_image('img/espacio.gif', horizontal, vertical)
            if j == "+":
                gamelib.draw_image('img/goal.gif', horizontal, vertical)
                gamelib.draw_image('img/jugador.gif', horizontal, vertical)
            else:
                gamelib.draw_image(f'img/{diccionario_caracteres[j]}.gif', horizontal, vertical)
            horizontal += CUADRADO
        horizontal = (ancho - columnas_grilla * CUADRADO) // 2 #vuelve al x inicial
        vertical += CUADRADO #cambia de fila

diccionario_teclas = teclas('movement_keys.txt')
niveles = niveles_en_lista('levels.txt')
diccionario_caracteres = {"@": "jugador", "#": "pared", ".": "goal", "$": "caja", "*": "cajaobjetivo", " ": "espacio"} 
# "jugador + objetivo" no aparece porque la imagen es una combinacion de jugador y goal