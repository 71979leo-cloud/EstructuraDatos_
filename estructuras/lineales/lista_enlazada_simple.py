from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Paso 1: Crear un nuevo nodo
        new_node = Node(data) 
        # Paso 2: Verificar si la lista esta vacia
        if self.head is None and self.tail is None:
            # Si la lista esta vacia, el nuevo nodo sera tanto la cabeza como la cola
            self.head = new_node
            self.tail = new_node
        else:
            # Si no esta vacia, el nuevo nodo apunta a la actual cabeza
            new_node.next = self.head   
            # Luego, la cabeza se actualiza para apuntar al nuevo nodo
            self.head = new_node

    def print_linked_list(self):
        # Paso 1: Iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        # Paso 2: Recorrer la lista mientras el nodo temporal no sea None
        print("Head -> ", end="")
        # Paso 3: Imprimir el valor del nodo temporal y avanzar al siguiente nodo
        while temp is not None:
            # Paso 4: comparar el valor del nodo temporal con el valor buscado
            print(temp.data, "->", end=" ")
            # Paso 5: imprimir el valor del nodo temporal y avanzar al siguiente nodo
            temp = temp.next
            # Paso 6: Al finalizar el recorrido, imprimir None para indicar el final de la lista
        print("None (Tail en:", self.tail.data if self.tail else "None", ")")
        # Paso 7: imprimir la 

    def insert_at_end(self, data):
        # Paso 1: Crear el nuevo nodo
        new_node = Node(data)
        # Paso 2: Verificar si está vacía
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # El nodo que actualmente es la cola apunta al nuevo nodo
            self.tail.next = new_node
            # La cola se actualiza para ser el nuevo nodo
            self.tail = new_node

    def search(self, data):
        # Paso 1: Iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        # Paso 2: Recorrer la lista mientras el nodo temporal no sea None
        while temp is not None:
            # Paso 3: Comparar el valor del nodo temporal con el valor buscado
            if temp.data == data:
                # Paso 4: Si se encuentra el valor, retornar True
                return True
            else:
                # Paso 5: Si no se encuentra el valor, avanzar al siguiente nodo
                temp = temp.next
        # Paso 6: Si se recorre toda la lista y no se encuentra el valor, retornar False
        return False

    def delete_at_beginning(self):
        if self.head is None:
            print("Lista vacía")
            return

        # Si head == tail 
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Si No (Más de un nodo: movemos head al siguiente)
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Lista vacía")
            return

        # Si head == tail 
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            # Mientras temp.next != tail
            while temp.next != self.tail:
                temp = temp.next
            
            # Al salir del ciclo, asignamos la cola al penúltimo nodo encontrado
            self.tail = temp
            # Rompemos el enlace apuntando el siguiente de la nueva cola a None
            self.tail.next = None