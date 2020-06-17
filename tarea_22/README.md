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

El input lo daremos como fichero ``.csv`` de 3 columas: nombre (Name), peso (Weight) y producción de leche (Production) y lo convertiremos a DataFrame con Pandas.

# Soluciones propuestas

| Programa           | Lenguaje | Observaciones                                                                      |
|--------------------|----------|------------------------------------------------------------------------------------|
| tarea_22_brute_force.py | Python   | Probamos todas las combinaciones.              |
| tarea_22_smart_search.py        | Python   | Descartamos las que ya sabemos que se pasan de peso y no las calculamos.


# Notas para el evaluador

En el fichero [tarea_22.ipynb](https://github.com/ethoreum/theegg_ai/blob/master/tarea_22/tarea_22.ipynb) se pueden encontrar el planteamiento del problema y las soluciones 
planteadas explicadas con detalle.

Si hubiera algún problema para ejecutar alguno de los programas me puedes encontrar como DiegoLasa en la plataforma de la escuela o en [mailto](mailto:dilasgoi@protonmail.com).

# Links de interés

* [Reto](http://www.nachocabanes.com/retos/reto.php?n=07)
