import game_logic as soko
import gamelib
from general import diccionario_teclas, juego_mostrar, niveles, CUADRADO, buscar_solucion
from clases import Pila

def main():
    indice=0
    juego = soko.crear_grilla(niveles[indice])
    pila1 = Pila() #pila de cada movimiento que almacena grillas
    pila2 = Pila() #pila de cada deshacer que almacena grillas
    pistas = Pila() #pila de cada pista que almacena cooredenas de movimientos
    columnas_grilla = len(juego[0])
    ancho = columnas_grilla*CUADRADO + (columnas_grilla*CUADRADO)*0.5
    alto = len(juego)*CUADRADO + len(juego)*CUADRADO*0.75
    gamelib.resize(ancho, alto)
    

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibuja la grilla
        juego_mostrar(juego,indice, ancho, alto, pistas)
        gamelib.draw_end()
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        try:
            if not ev:
                break
            if ev.type == gamelib.EventType.KeyPress and diccionario_teclas[ev.key.lower()] == "SALIR":
                break
            if ev.type == gamelib.EventType.KeyPress and diccionario_teclas[ev.key.lower()] == "REINICIAR":
                #reinicia el nivel
                juego = soko.crear_grilla(niveles[indice])
                pila1 = Pila()
                pistas = Pila()
                continue
            if ev.type == gamelib.EventType.KeyPress and diccionario_teclas[ev.key.lower()] == "PISTA":
                #muestra una pista
                if pistas.esta_vacia():
                    pistas = buscar_solucion(juego)
                    continue
                if not pistas.esta_vacia():
                    juego = soko.mover(juego, pistas.desapilar())
            if ev.type == gamelib.EventType.KeyPress and diccionario_teclas[ev.key.lower()] == "DESHACER":
                #deshace el movimiento
                if pila2.esta_vacia() or juego != pila2.ver_tope():
                    pila2.apilar(juego)
                juego = pila1.desapilar()
                if pila1.esta_vacia():
                    pila1.apilar(juego)
                pistas = Pila()      
                continue
            if ev.type == gamelib.EventType.KeyPress and diccionario_teclas[ev.key.lower()] == "REHACER":
                #rehace el movimiento
                if pila1.esta_vacia() or juego != pila1.ver_tope():
                    pila1.apilar(juego)
                juego = pila2.desapilar()
                continue

            if pila1.esta_vacia() or juego != pila1.ver_tope():
                pila1.apilar(juego)
            if diccionario_teclas[ev.key.lower()] != "DESHACER" or diccionario_teclas[ev.key.lower()] == "REHACER":
                pila2 = Pila()
            if diccionario_teclas[ev.key.lower()] != "PISTA":
                pistas = Pila()
                juego = soko.mover(juego, diccionario_teclas[ev.key.lower()])
        except KeyError:
            continue
        except ValueError:
            continue


        if soko.juego_ganado(juego):
                gamelib.draw_begin()
                gamelib.draw_text('Siguiente', ancho*0.25, alto*0.5, size=18, fill = 'green')
                gamelib.draw_text('Exit', ancho*0.75, alto*0.5, size=18, fill = 'red')
                gamelib.draw_text('Clickea:', ancho*0.5, 20,)
                gamelib.draw_line(ancho//2, 35, ancho//2, alto, width=2, fill='white')
                gamelib.draw_end()
                
                ev = gamelib.wait(gamelib.EventType.ButtonPress)
                if not ev:
                    break
                if ev.x<ancho//2:
                    indice += 1
                    try:
                        juego = soko.crear_grilla(niveles[indice])
                        pila1 = Pila()
                        pila1.apilar(juego)
                        pila2 = Pila()
                        pistas = Pila()
                        columnas_grilla = len(juego[0])
                        ancho = columnas_grilla*CUADRADO + (columnas_grilla*CUADRADO)*0.5
                        alto = len(juego)*CUADRADO + len(juego)*CUADRADO*0.75
                        gamelib.resize(ancho, alto)
                        continue
                    except IndexError:
                        print("No hay mas niveles")
                        break
                else:
                    break
gamelib.init(main)