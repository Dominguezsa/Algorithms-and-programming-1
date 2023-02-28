import game_logic as soko
import gamelib
from general import diccionario_teclas, juego_mostrar, niveles, CUADRADO

def main():
    indice=0
    juego = soko.crear_grilla(niveles[indice])
    columnas_grilla = len(juego[0])
    ancho = columnas_grilla*CUADRADO + (columnas_grilla*CUADRADO)*0.5
    alto = len(juego)*CUADRADO + len(juego)*CUADRADO*0.75
    gamelib.resize(ancho, alto)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibuja la grilla
        juego_mostrar(juego,indice, ancho, alto)
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
                continue
            tecla = ev.key.lower()
            juego = soko.mover(juego, diccionario_teclas[tecla])
        except KeyError:
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