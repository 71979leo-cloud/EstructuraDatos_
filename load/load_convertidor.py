import sys
from PyQt5 import QtWidgets, uic
from estructuras.lineales.stack import Stack

class VentanaConvertidor(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/convertidor_infijo.ui", self)
        
        self.btn_convertir.clicked.connect(self.procesar_conversion)

    def prioridad(self, operador):
        """Define la jerarquía de los operadores según el PDF del profesor"""
        if operador == '(' or operador == ')':
            return 1
        if operador == '+' or operador == '-':
            return 2
        if operador == '*' or operador == '/':
            return 3
        if operador == '^' or operador == '$': 
            return 4
        return 0

    def obtener_top_valor(self, pila):
        if pila.is_empty():
            return None
        nodo_temporal = pila.pop()
        pila.push(nodo_temporal.data)
        return nodo_temporal

    def convertir_infija_a_posfija(self, expresion_infija):
        """Algoritmo de conversión utilizando tu clase Stack basada en Nodos"""
        pila_operadores = Stack()
        resultado_posfija = "" 
        
        for caracter in expresion_infija:
            if caracter != " ":
                
                if (caracter >= 'A' and caracter <= 'Z') or (caracter >= 'a' and caracter <= 'z'):
                    resultado_posfija = resultado_posfija + caracter
                
                elif caracter == '(':
                    pila_operadores.push(caracter)
                    
                elif caracter == ')':
                    top_nodo = self.obtener_top_valor(pila_operadores)
                    while top_nodo is not None and top_nodo.data != '(':
                        nodo_sacado = pila_operadores.pop()
                        resultado_posfija = resultado_posfija + nodo_sacado.data
                        top_nodo = self.obtener_top_valor(pila_operadores)
                        
                    if pila_operadores.is_empty() == False:
                        pila_operadores.pop()
                
                else:
                    top_nodo = self.obtener_top_valor(pila_operadores)
                    while (top_nodo is not None and 
                           self.prioridad(top_nodo.data) >= self.prioridad(caracter)):
                        nodo_sacado = pila_operadores.pop()
                        resultado_posfija = resultado_posfija + nodo_sacado.data
                        top_nodo = self.obtener_top_valor(pila_operadores)
                    
                    pila_operadores.push(caracter)

        while pila_operadores.is_empty() == False:
            nodo_sacado = pila_operadores.pop()
            resultado_posfija = resultado_posfija + nodo_sacado.data

        return resultado_posfija

    def procesar_conversion(self):
        """Lee tu objeto txt_inypost, manda a hacer la conversión y pinta el resultado"""
        texto_infijo = self.txt_inypost.text()
        if texto_infijo != "":
            try:
                resultado = self.convertir_infija_a_posfija(texto_infijo)
                self.lbl_resultado.setText(resultado) # Tu etiqueta de Qt
            except Exception as e:
                print(f"Error interno: {e}")
                self.lbl_resultado.setText("Error en la expresión")
        else:
            self.lbl_resultado.setText("Escribe una expresión primero")