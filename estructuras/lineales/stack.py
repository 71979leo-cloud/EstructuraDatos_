
from estructuras.lineales.nodo import Node

class Stack(object):
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, dato):
        nuevo_nodo = Node(dato)
        if self.is_empty():
            self.top = nuevo_nodo
        else:
            nuevo_nodo.next = self.top 
            self.top = nuevo_nodo

    def pop(self):
        if self.is_empty():
            return None
        else:
            nodo_eliminado = self.top
            self.top = self.top.next 
            nodo_eliminado.next = None 
            return nodo_eliminado

    def top_of_stack(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            print(f"El tope de la pila es: {self.top.data}")