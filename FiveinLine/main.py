from Library import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 350
LIM_IZQ = 25
LIM_DER = 275
LIM_ARRIBA = 30
LIM_ABAJO = 280
LADO = 25
PLAYER1 = "O"
PLAYER2 = "X"
EMPTY = " "


def create_game():
    """Inicializar el estado del juego
       Devuelve una lista de listas con 10 filas y 10 columnas
       con elemntos vacíos (espacios en blanco)"""
    return [[" " for i in range(10)] for j in range(10)]


def update_game(juego, x, y):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    # defino las coordenadas de las celdas a las que se NO puede hacer click
    if x < LIM_IZQ or x >= LIM_DER or y < LIM_ARRIBA or y >= LIM_ABAJO:
        return juego
    x = (x - 25) // LADO
    y = (y - 30) // LADO
    # cant es la cantidad de espacios en blanco
    cant = 0
    for i in juego:
        for j in i:
            if j == EMPTY:
                cant += 1
    if juego[y][x] == EMPTY and cant % 2 == 0:
        juego[y][x] = PLAYER1
        return juego
    elif juego[y][x] == EMPTY and cant % 2 != 0:
        juego[y][x] = PLAYER2
        return juego
    else:
        return juego


def there_is_a_winner(grilla):
    # Comprobación de filas y columnas
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if j + 4 < len(grilla[i]) and same_player(i, j, 0, 1, grilla):
                return grilla[i][j], True
            elif i + 4 < len(grilla) and same_player(i, j, 1, 0, grilla):
                return grilla[i][j], True
            # Comprobación de diagonales
            if i + 4 < len(grilla) and j + 4 < len(grilla[i]) and same_player(i, j, 1, 1, grilla):
                return grilla[i][j], True
            elif i + 4 < len(grilla) and j >= 4 and same_player(i, j, 1, -1, grilla):
                return grilla[i][j], True
    # Si no hay ganador
    return None, False


def same_player(i, j, di, dj, grilla):
    return all(grilla[i][j] == grilla[i + k * di][j + k * dj] != EMPTY for k in range(5))


def display_game(juego, ganado):
    """Actualizar la ventana"""
    # titulo
    gamelib.draw_text('Five In Line', 150, 15, size=14)
    # cant es la cantidad de espacios en blanco
    cant = 0
    for i in juego:
        for j in i:
            if j == " ":
                cant += 1
    if cant % 2 == 0:
        gamelib.draw_text(f'Turn: {PLAYER1}', 150, 300, size=12, italic=True)
    else:
        gamelib.draw_text(f'Turn: {PLAYER2}', 150, 300, size=12, italic=True)

    # cuadrado 250x250
    gamelib.draw_rectangle(LIM_IZQ, LIM_ABAJO, LIM_DER, LIM_ARRIBA, outline='white', fill='black')

    # lineas verticales
    for i in range(1, 10):
        gamelib.draw_line(LIM_IZQ + LADO * i, LIM_ABAJO, LIM_IZQ + LADO * i, LIM_ARRIBA, fill='blue', width=2)

    # lineas horizontales
    for i in range(1, 10):
        gamelib.draw_line(LIM_IZQ, LIM_ARRIBA + LADO * i, LIM_DER, LIM_ARRIBA + LADO * i, fill='blue', width=2)
    # celdas con contenido
    for i in range(10):
        for j in range(10):
            if juego[i][j] == PLAYER1:
                gamelib.draw_text(f'{PLAYER1}', 37.5 + (LADO * j), 42.5 + (LADO * i))
            elif juego[i][j] == PLAYER2:
                gamelib.draw_text(f'{PLAYER2}', 37.5 + (LADO * j), 42.5 + (LADO * i))
    if ganado[0]:
        gamelib.draw_text(f'Game over, "{ganado[1]}" wins', 150, 325)


def main():
    juego = create_game()
    game_won = False, None
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        display_game(juego, game_won)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            if game_won[0]:
                juego = create_game()
                game_won = False, None
                display_game(juego, game_won)
            else:
                x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click
                juego = update_game(juego, x, y)
                someone_won = there_is_a_winner(juego)
                if someone_won[1]:
                    game_won = True, someone_won[0]


gamelib.init(main)
