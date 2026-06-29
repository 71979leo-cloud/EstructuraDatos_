import sys
from PyQt5 import QtWidgets, uic

import load.load_lista_enlazada as interfaz_lista
from load.load_convertidor import VentanaConvertidor

class MainWindowPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/lista_enlazada.ui", self)
        
        self.actionLista_Enlazada.triggered.connect(self.abrir_dialogo_funciones)
        
        self.actionConvertidor.triggered.connect(self.abrir_convertidor)

    def abrir_dialogo_funciones(self):
        dialogo = interfaz_lista.VentanaLista()
        dialogo.exec_() 

    def abrir_convertidor(self):
        ventana = VentanaConvertidor()
        ventana.exec_() 

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = MainWindowPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()