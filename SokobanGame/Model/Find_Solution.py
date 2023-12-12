import time
from SokobanGame.Model.game_logic import mover, juego_ganado
from SokobanGame.Model.Constantes import BOX, WALL, GOAL, coords_int_str, COORDS_STR, BOX_WITH_GOAL, PLAYER_IN_GOAL
from SokobanGame.ADTs.Stack import Stack


def buscar_solucion(estado_inicial):
    """Trata de encontrar una posible solucion al juego,
    devolviendo las coordenadas de los movimientos a realizar,
    o una pila vacia si no hay solucion"""
    visitados = set()
    pila = Stack()
    ti = time.time()
    ete = hacer_tupla(estado_inicial)
    backtracking(ete, visitados, pila)
    print(time.time() - ti, pila.cantidad)
    return pila


def backtracking(estado, visitados: set, pila) -> bool:
    """funcion auxiliar de buscar_solucion"""
    visitados.add(estado)
    if juego_ganado(estado):
        return True
    for direccion in COORDS_STR:
        nuevo_estado = hacer_tupla(mover(estado, direccion))
        if (nuevo_estado in visitados
                or box_in_corner(nuevo_estado)
                or box_impossible(nuevo_estado)
                or two_boxes_together(nuevo_estado)):

            continue
        if backtracking(nuevo_estado, visitados, pila):
            pila.apilar(direccion)
            return True
    return False


def two_boxes_together(grilla):
    for i in range(1, len(grilla) - 1):
        for j in range(1, len(grilla[0]) - 1):
            if grilla[i][j] == BOX and hay_box_alrededor(grilla, i, j):
                return True
    return False


def hay_box_alrededor(grilla, i, j):
    for dx, dy in coords_int_str.keys():
        nx = i + dy
        ny = j + dx
        if grilla[nx][ny] == BOX:
            if dx == 0:
                if (grilla[i][j - 1] == WALL and grilla[i + dy][j - 1] == WALL) or (
                        grilla[i][j + 1] == WALL and grilla[i + dy][j + 1] == WALL):
                    return True
            else:
                if (grilla[i - 1][j] == WALL and grilla[i - 1][j + dx] == WALL) or (
                        grilla[i + 1][j] == WALL and grilla[i + 1][j + dx] == WALL):
                    return True
    return False


FICHAS = [GOAL, BOX_WITH_GOAL, PLAYER_IN_GOAL]


def box_impossible(matriz):
    l1 = set()
    l2 = set()
    for i in range(1, len(matriz) - 1):
        l1.add(matriz[i][1])
        l2.add(matriz[i][len(matriz[0]) - 2])
    if BOX in l1 and not hay_algo(l1):
        return True
    if BOX in l2 and not hay_algo(l2):
        return True
    l3 = set()
    l4 = set()
    for j in range(1, len(matriz[0]) - 1):
        l3.add(matriz[1][j])
        l4.add(matriz[len(matriz) - 2][j])
    if BOX in l3 and not hay_algo(l3):
        return True
    if BOX in l4 and not hay_algo(l4):
        return True
    return False


def hay_algo(fila):
    for elem in FICHAS:
        if elem in fila:
            return True
    return False


def box_in_corner(matriz):
    for i in range(1, len(matriz) - 1):
        for j in range(1, len(matriz[0]) - 1):
            if matriz[i][j] == BOX:
                if matriz[i - 1][j] == WALL and (matriz[i][j - 1] == WALL or matriz[i][j + 1] == WALL):
                    return True
                if matriz[i + 1][j] == WALL and (matriz[i][j - 1] == WALL or matriz[i][j + 1] == WALL):
                    return True
    return False


def hacer_tupla(estado):
    """funcion auxiliar de backtracking, convierte una grilaa (lista de listas) en una tupla de tupla"""
    return tuple(tuple(i) for i in estado)


def hacer_lista(grilla):
    return list(list(i) for i in grilla)
