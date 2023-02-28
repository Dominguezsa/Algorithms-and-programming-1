import gamelib
from game_logic import mover, juego_ganado
from clases import Pila
CUADRADO = 32 #tamaño de un lado de un cuadrado dentro de la grilla
coords = {"NORTE": (0, -1), "ESTE": (1, 0), "SUR": (0, 1), "OESTE": (-1, 0)}
anticoords = {(0, -1): "NORTE", (0, 1): "SUR", (1, 0): "ESTE", (-1, 0): "OESTE"}

def teclas(archivo):
    """Crea un diccionario tecla = direccion a partir de un archivo"""
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
def juego_mostrar(juego, indice, ancho, alto, pistas):
    """Actualiza la ventana"""
    medio = ancho//2 #medio de la ventana en el eje x
    columnas_grilla = len(juego[0])
    horizontal = (ancho - columnas_grilla * CUADRADO) // 2 # "horizontal" es el espacio en el eje x que hay entre el borde de la ventana y la grilla
    vertical = (alto - len(juego) * CUADRADO) // 2 # "vertical" es el espacio en el eje y que hay entre el borde de la ventana y la grilla
    gamelib.draw_text('SokoBan', 50, 20)
    gamelib.draw_text('P: pista', 50, 40)
    gamelib.draw_text(f'Nivel: {indice+1}', ancho-50, 20)
    gamelib.draw_text('R: reiniciar       T: rehacer', medio, alto-vertical//2)
    gamelib.draw_text('ESC: salir     B: deshacer', medio, alto-vertical+20)
    if not pistas.esta_vacia():
        gamelib.draw_text('HAY PISTA!', medio, vertical-15)
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
diccionario_teclas = teclas("movement_keys.txt")
niveles = niveles_en_lista('levels.txt')
diccionario_caracteres = {"@": "jugador", "#": "pared", ".": "goal", "$": "caja", "*": "cajaobjetivo", " ": "espacio"} 
# "jugador + objetivo" no aparece porque la imagen es una combinacion de jugador y goal

#backtracking:
def buscar_solucion(estado_inicial):
    '''Trata de encontrar una posible solucion al juego,
    devolviendo las coordenadas de los movimientos a realizar,
    o una pila vacia si no hay solucion'''
    visitados = {}
    posible_solucion = backtracking(estado_inicial, visitados)
    try:
        if posible_solucion[0]:
            pila = Pila()
            for direc in posible_solucion[1]:
                pila.apilar(coords[direc])
            return pila
    except TypeError:
        return Pila()

def backtracking(estado, visitados):
    '''funcion auxiliar de buscar_solucion'''
    visitados[hacer_tupla(estado)] = True
    if juego_ganado(estado):
        return True
    for direccion in coords.values():
        nuevo_estado = hacer_tupla(mover(estado, direccion))
        if nuevo_estado in visitados:
            continue
        nivel_nuevo = hacer_lista(nuevo_estado)
        if backtracking(nivel_nuevo, visitados):
            return True, hacer_coordenadas(anticoords[direccion])
    return False

def hacer_tupla(estado):
    '''funcion auxiliar de backtracking, convierte una grilaa (lista de listas) en una tupla de tuplas'''
    tupla = []
    for i in estado:
        l = []
        for j in i:
            l.append(j)
        tupla.append(tuple(l))
    return tuple(tupla)

def hacer_lista(estado):
    '''funcion auxiliar de backtracking, convierte una grilla (tupla de tuplas) en una grilla lista de listas'''
    lista = []
    for i in estado:
        c = []
        for j in i:
            c.append(j)
        lista.append(c)
    return lista

def hacer_coordenadas(coord, lista=[]):
    '''funcion auxiliar de backtracking, va recibiendo coordenadas y las devuelve en forma de lista'''
    lista += [coord]
    return lista