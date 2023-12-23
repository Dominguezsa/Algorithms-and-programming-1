
# CONSTANTS
PLAYER = "@"
PLAYER_IN_GOAL = "+"
WALL = "#"
GOAL = "."
BOX = "$"
BOX_WITH_GOAL = "*"
EMPTY = " "


PATH_KEYS = "LevelsAndKeys/movement_keys.txt"
PATH_LEVELS = "LevelsAndKeys/levels.txt"
coords_str_int = {"NORTE": (0, -1), "ESTE": (1, 0), "SUR": (0, 1), "OESTE": (-1, 0)}
COORDS_STR = ((0, -1), (1, 0), (0, 1), (-1, 0))
coords_int_str = {(0, -1): "NORTE", (0, 1): "SUR", (1, 0): "ESTE", (-1, 0): "OESTE"}
CUADRADO = 32
# diccionarios que se utilizan en la funcion mover general
movimientos_simples = {EMPTY: PLAYER, GOAL: PLAYER_IN_GOAL}
contenido1 = {BOX: PLAYER,
              BOX_WITH_GOAL: PLAYER_IN_GOAL}  # lo que puede haber en la casilla al lado del jugador
contenido2 = {GOAL: BOX_WITH_GOAL, EMPTY: BOX}  # lo que puede haber al lado de contenido1

INDICE_INICIAL = 0

