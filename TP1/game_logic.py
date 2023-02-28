#constantes
JUGADOR = "@"
JUGADOR_CON_OBJETIVO = "+"
PARED = "#"
OBJETIVO = "."
CAJA = "$"
CAJA_CON_OBJETIVO = "*"
ESPACIO = " "

#diccionarios que se utilizan en la funcion mover general
movimientos_simples = {ESPACIO: JUGADOR, OBJETIVO: JUGADOR_CON_OBJETIVO}
contenido1 = {CAJA: JUGADOR, CAJA_CON_OBJETIVO: JUGADOR_CON_OBJETIVO}#lo que puede haber en la casilla al lado del jugador
contenido2 = {OBJETIVO: CAJA_CON_OBJETIVO, ESPACIO: CAJA}#lo que puede haber al lado de contenido1

#funciones adicionales
def copiar_grilla(grilla):
    '''Copia una grilla y devuelve una nueva, igual a la recibida''' 
    return [list(fila) for fila in grilla]

def averiguar_coordenadas_jugador(grilla):
    '''Averigua las coordenas del jugador y las devuelve
       como una tupla'''
    for fila in grilla:
            for caracter in fila:
                if caracter == JUGADOR or caracter == JUGADOR_CON_OBJETIVO:
                    return grilla.index(fila), fila.index(caracter)

def mover_funcion_general(grilla, x, y, cord1, cord2):
    '''funcion que devuelve una grilla si el movimiento es valido,
       sino, devuelve la grilla original'''
    if grilla[cord1+y][cord2+x] in movimientos_simples: 
        grilla[cord1+y][cord2+x] = movimientos_simples[grilla[cord1+y][cord2+x]]
    elif grilla[cord1+y][cord2+x] == PARED:
        return grilla
    elif grilla[cord1+y][cord2+x] in contenido1 and grilla[cord1+y*2][cord2+x*2] in contenido2:
        grilla[cord1+y][cord2+x] = contenido1[grilla[cord1+y][cord2+x]]
        grilla[cord1+y*2][cord2+x*2] = contenido2[grilla[cord1+y*2][cord2+x*2]]
    return grilla

def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.
    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda.'''
    grilla = [list(fila) for fila in desc]
    m = max([len(fila) for fila in grilla])
    for fila in grilla:
        while len(fila) < m:
            fila.append(PARED)
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    return (len(grilla[0]), (len(grilla)))

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return (grilla[f][c]) == PARED

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == OBJETIVO or grilla[f][c] == CAJA_CON_OBJETIVO or grilla[f][c] == JUGADOR_CON_OBJETIVO

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return (grilla[f][c]) == CAJA or (grilla[f][c]) == CAJA_CON_OBJETIVO

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] == JUGADOR or grilla[f][c] == JUGADOR_CON_OBJETIVO

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for fila in grilla:
        for caracter in fila:
            if caracter == OBJETIVO or caracter == JUGADOR_CON_OBJETIVO:  #si es igual a un objetivo o un objetivo + jugador
                return False
            continue
    return True


def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.
    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:
    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur
    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    cord1 = averiguar_coordenadas_jugador(grilla)[0] #fila jugador
    cord2 = averiguar_coordenadas_jugador(grilla)[1] #columna jugador
    x = direccion[0]
    y = direccion[1]
    nueva_grilla = copiar_grilla(grilla)
    nueva_grilla = mover_funcion_general(nueva_grilla, x, y, cord1, cord2)

    if nueva_grilla == grilla:
        return nueva_grilla
    elif grilla[cord1][cord2] == JUGADOR:
        nueva_grilla[cord1][cord2] = ESPACIO
        return nueva_grilla
    elif grilla[cord1][cord2] == JUGADOR_CON_OBJETIVO:
        nueva_grilla[cord1][cord2] = OBJETIVO
        return nueva_grilla