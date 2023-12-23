import Model.game_logic as soko
from ADTs.stack import Stack
import Library.gamelib as gamelib
from Model.general import get_stacks, manage_stacks
from Model.find_solution import buscar_solucion
from Model.manage_files import teclas, niveles_en_lista, obtener_movimientos_validos
from Model.constants import INDICE_INICIAL, PATH_LEVELS, PATH_KEYS
from View.View import display_game, show_options, find_height_and_width


def main():
    indice = INDICE_INICIAL
    niveles = niveles_en_lista(PATH_LEVELS)
    diccionario_teclas = teclas(PATH_KEYS)
    movimientos_validos = obtener_movimientos_validos(diccionario_teclas)
    juego = soko.crear_grilla(niveles[indice])
    pila_deshacer, pila_rehacer, pistas = get_stacks(juego)
    ancho, alto = find_height_and_width(juego)
    gamelib.resize(ancho, alto)
    mostrar_letras = False

    while gamelib.is_alive():
        gamelib.draw_begin()
        display_game(juego, indice, ancho, alto, pistas, mostrar_letras)
        gamelib.draw_end()
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        try:
            if not ev:
                break
            if diccionario_teclas[ev.key.lower()] == "SALIR":
                break
            if diccionario_teclas[ev.key.lower()] == "REINICIAR" and not mostrar_letras:
                juego = soko.crear_grilla(niveles[indice])
                pila_deshacer = Stack()
                pistas = Stack()
                continue
            if diccionario_teclas[ev.key.lower()] == "PISTA" and not mostrar_letras:
                # muestra una pista
                if pistas.esta_vacia():
                    pistas = buscar_solucion(juego)
                    continue
                if not pistas.esta_vacia():
                    juego = soko.mover(juego, pistas.desapilar())
            if diccionario_teclas[ev.key.lower()] == "DESHACER" and not mostrar_letras:
                juego = manage_stacks(pila_rehacer, pila_deshacer, juego)
                pistas = Stack()
                continue
            if diccionario_teclas[ev.key.lower()] == "REHACER" and not mostrar_letras:
                juego = manage_stacks(pila_deshacer, pila_rehacer, juego)
                continue
            if diccionario_teclas[ev.key.lower()] == "HELP":
                if mostrar_letras:
                    mostrar_letras = False
                else:
                    mostrar_letras = True
            if pila_deshacer.esta_vacia() or juego != pila_deshacer.ver_tope():
                pila_deshacer.apilar(juego)
            if diccionario_teclas[ev.key.lower()] != "DESHACER" or diccionario_teclas[ev.key.lower()] == "REHACER":
                pila_rehacer = Stack()
            if ev.key.lower() in movimientos_validos and not mostrar_letras:
                pistas = Stack()
                juego = soko.mover(juego, diccionario_teclas[ev.key.lower()])
                if juego == pila_deshacer.ver_tope():
                    pila_deshacer.desapilar()
        except KeyError:
            continue
        except ValueError:
            continue
        if soko.juego_ganado(juego):
            show_options(ancho, alto)
            ev = gamelib.wait(gamelib.EventType.ButtonPress)
            if not ev:
                break
            if ev.x < ancho // 2:
                indice += 1
                try:
                    juego = soko.crear_grilla(niveles[indice])
                    pila_deshacer, pila_rehacer, pistas = get_stacks(juego)
                    ancho, alto = find_height_and_width(juego)
                    gamelib.resize(ancho, alto)
                    continue
                except IndexError:
                    print("No hay mas niveles")
                    break
            else:
                break


gamelib.init(main)
