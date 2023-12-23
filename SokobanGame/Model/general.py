
from SokobanGame.ADTs.stack import Stack


def get_stacks(juego):  # return ancho, alto, pila2, pistas
    pila1 = Stack()  # pila de cada movimiento que almacena grillas
    pila1.apilar(juego)
    pila2 = Stack()
    pistas = Stack()
    return pila1, pila2, pistas


def manage_stacks(pila1, pila2, juego):
    if pila1.esta_vacia() or juego != pila1.ver_tope():
        pila1.apilar(juego)
    juego = pila2.desapilar()
    if pila2.esta_vacia():
        pila2.apilar(juego)
    if juego == pila1.ver_tope():
        pila1.desapilar()
    return juego
