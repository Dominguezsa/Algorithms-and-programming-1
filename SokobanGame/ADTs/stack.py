from SokobanGame.ADTs.node import Node


class Stack:
    def __str__(self):
        return str(self.ver_tope())

    def __init__(self):
        """
        Inicializa una nueva pila, vacía
        """
        self.tope = None
        self.cantidad = 0

    def apilar(self, dato):
        """
        Agrega un nuevo elemento a la pila
        """
        nodo = Node(dato, self.tope)
        self.tope = nodo
        self.cantidad += 1

    def desapilar(self):
        """
        Desapila el elemento que está en el tope de la pila
        y lo devuelve.
        Pre: la pila NO está vacía.
        Pos: el nuevo tope es el que estaba abajo del tope anterior
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        self.cantidad -= 1
        return dato

    def ver_tope(self):
        """
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        """
        Devuelve True o False según si la pila está vacía o no
        """
        return self.tope is None

    def cantidad(self):
        return self.cantidad
