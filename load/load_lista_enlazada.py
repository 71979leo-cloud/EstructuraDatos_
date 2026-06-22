import sys
from PyQt5 import QtWidgets, uic

from estructuras.lineales.lista_enlazada_simple import LinkedList

class VentanaLista(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        

        uic.loadUi("ui/funciones_lista.ui", self)
        

        self.lista = LinkedList()
        
        # Conexión de todos tus botones
        self.btn_agregar_inicio.clicked.connect(self.metodo_agregar_inicio)
        self.btn_agregar_final.clicked.connect(self.metodo_agregar_final)
        self.btn_imprimir.clicked.connect(self.metodo_imprimir)
        self.btn_eliminar_inicio.clicked.connect(self.metodo_eliminar_inicio)
        self.btn_eliminar_final.clicked.connect(self.metodo_eliminar_final)
        self.btn_buscar.clicked.connect(self.metodo_buscar)

    def metodo_agregar_inicio(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_beginning(dato)
            self.lbl_resultado.setText(f"Agregado al inicio: {dato}")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Escribe un dato primero")

    def metodo_agregar_final(self):
        dato = self.txt_dato.text()
        if dato:
            self.lista.insert_at_end(dato)
            self.lbl_resultado.setText(f"Agregado al final: {dato}")
            self.txt_dato.clear()
        else:
            self.lbl_resultado.setText("Escribe un dato primero")

    def metodo_imprimir(self):
        actual = self.lista.head
        elementos = []
        
        while actual is not None:
            elementos.append(str(actual.data))
            actual = actual.next
            
        elementos.append("None")
        texto_lista = " -> ".join(elementos)
        
        self.lbl_resultado.setText(texto_lista)

    def metodo_eliminar_inicio(self):
        self.lista.delete_at_beginning()
        self.lbl_resultado.setText("Se eliminó el primer elemento")

    def metodo_eliminar_final(self):
        self.lista.delete_at_end()
        self.lbl_resultado.setText("Se eliminó el último elemento")

    def metodo_buscar(self):
        dato = self.txt_dato.text()
        if dato:
            encontrado = self.lista.search(dato)
            if encontrado:
                self.lbl_resultado.setText(f"El elemento {dato} SÍ existe")
            else:
                self.lbl_resultado.setText(f"El elemento {dato} NO existe")
        else:
            self.lbl_resultado.setText("Escribe el dato a buscar")