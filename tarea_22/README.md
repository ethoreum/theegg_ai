# El algoritmo del lechero	

En esta tarea debes desarrollar (en el lenguaje o lenguajes de programación que tú quieras) el siguiente
algoritmo:

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.

1. Para este propósito tienes que definir las siguientes entradas:

* Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
* Entrada: Peso total que el camión puede llevar.
* Entrada: Lista de pesos de las vacas.
* Entrada: Lista de la producción de leche por vaca, en litros por día.

2. El algoritmo que programes tiene que calcular la siguiente salida:

* Salida: Cantidad máxima de producción de leche se puede obtener.

# Observaciones

El input lo daremos como fichero csv de 3 columas: nombre (Name), peso (Weight) y producción de leche (Production) y lo convertiremos a DataFrame con Pandas.

# Soluciones propuestas

| Programa           | Lenguaje | Observaciones                                                                      |
|--------------------|----------|------------------------------------------------------------------------------------|
| tarea_22_brute_force.py | Python   | Probamos todas las combinaciones.              |
| tarea_22_smart_search.py        | Python   | Descartamos las que ya sabemos que se pasan de peso y no las calculamos.

## Propuesta por fuerza bruta (tarea_22_brute_force.py)

* Vamos a definir todas las combinaciones en forma de lista binaria. Por ejemplo, si tenemos 3 vacas la combinaciones son las siguientes:

- [0,0,0]
- [0,0,1]
- [0,1,0]
- [0,1,1]
- [1,0,0]
- [1,0,0]
- [1,1,0]
- [1,1,1]

El numero total de combinaciones para *n* vacas sería el número mas grande que se puede representar con *n* bits y el 0. Para el caso de 3 el número más grande representable con 3 bits es el 7 (111). A este le sumamos el 0 (000) y las combinaciones
son 8 como las que mostramos. Vamos, que si no me fallan las cuentas, dadas *n* vacas el total de posibilidades es:

<img src="https://render.githubusercontent.com/render/math?math=2^{n}">


* Después calcularemos el peso total y la producción total para cada una de las combinaciones y añadiremos a una lista todas aquellas que tengan un peso menor a un peso máximo dado (en nuestro caso 600 kilos). Calcularemos el máximo de esa lista en
  base a la producción y aplicaremos la máscara binaria a la lista de nombres de vaca con el fin de obtener el listado de las vacas que vamos a comprar.

### Requisitos

Requiere tener *pandas* y Python 3 instalado. Si el evaluador no tuviera la posibilidad de usar Pandas se podría modificar el código para generar las listas a mano o podría poner una VM en la nube
para que el evaluador pudiera ejecutar el código.


## Propuesta sin probar todas las combinaciones (tarea_22_smart_search.py)

Desde el punto de vista de la eficiencia no tiene sentido probar **todas** las combinaciones. Podemos ordenar las vacas de la más pesada a la menos pesada e ir metiendo vacas mientras no sobrepasemos el peso máximo (600 kilos). Por ejemplo:

weights = [202, 201, 200, 150, 203]

* Metemos la primera vaca: [1,0,0,0,0]. Peso total: 202
* Metemos la segunda vaca: [1,1,0,0,0]. Peso total: 403
* Metemos la tercera vaca: [1,1,1,0,0]. Peso total: 603 (PESO SOBREPASADO)

Llegados a este punto no tendría sentido considerar [1,1,1,1,0] o [1,1,1,1,1,], ¿Por qué calcularlas entonces?

## Links de interés

* [Reto](http://www.nachocabanes.com/retos/reto.php?n=07)
