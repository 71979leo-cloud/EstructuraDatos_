# Convertidor de Expresiones Infijas a Posfijas (Notación Polaca Inversa)

Bueno pues este proyecto se basa en que, es una aplicación gráfica hecha en Python con **PyQt5** que sirve para convertir expresiones matemáticas de toda la vida (notación **Infija**, como `A+B*C`) a la forma en que las procesan las computadoras (notación **Posfija** , como `ABC*+`).

Para lograrlo, programamos y generamos con los codigos con ayuda de la IA pero claro respentando las clases y los demas archivos que ya tenemos en este proyecto y analizando en todo lo momento lo que nos generaba la IA y bueno pues en si es una estructura lineal de tipo **Pila (Stack)** que se mueve de forma dinámica usando nodos enlazados (`Node`), acoplándola con una interfaz que diseñé en Qt Designer.

(Estructura del Proyecto)

El código me quedó acomodado en este orden para no revolver las clases que ya teníamos de clase con las vistas de la ventana flotante:

```text
estructuradatos/
│
├── estructuras/
│   └── lineales/
│       ├── nodo.py          # Clase Node con variables en inglés (.data y .next)
│       └── stack.py         # Mi Pila (LIFO) usando la clase Node
│
├── load/
│   └── load_convertidor.py  # Aquí metí el algoritmo de conversión y la lógica de Qt
│
├── ui/
│   └── convertidor_infijo.ui # El diseño gráfico que hice en Qt Designer
│
└── main.py                  # El archivo principal que corre todo el menú