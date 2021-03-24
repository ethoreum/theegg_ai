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

El input lo daremos como fichero ``.csv`` de 3 columas que se ubica en el directorio``data``: nombre (Name), peso (Weight) y producción de leche (Production) y lo convertiremos a DataFrame con Pandas.

# Soluciones propuestas

| Programa                 | Lenguaje | Observaciones                                                                      |
|--------------------------|----------|------------------------------------------------------------------------------------|
| [brute_force.py](https://github.com/ethoreum/theegg_ai/blob/master/tarea_22/brute_force/brute_force.py)           | Python   | Probamos todas las combinaciones. [Documentación del programa](https://github.com/ethoreum/theegg_ai/blob/master/tarea_22/brute_force/brute_force.ipynb)                                                  |
| [dynamic_programming.py](https://github.com/ethoreum/theegg_ai/blob/master/tarea_22/dynamic_programming/dynamic_programming.py)   | Python   | Utilizando programación dinámica.                                                  |

# Ejecución de los programas

Si hubiera algún problema para ejecutar alguno de los programas me puedes encontrar como DiegoLasa en la plataforma de la escuela o en [mailto](mailto:dilasgoi@protonmail.com).

## Programas en Python

### ``brute_force.py``

Habría que dar dos argumentos de línea de comandos:

* **Argumento 1**: fichero ``csv`` con los datos de entrada.
* **Argumento 2**: peso máximo permitido por el camión.

```
python brute_force.py cows.csv 600
Producción máxima: 92
Peso de la combinación: 570
Listado de vacas que deberíamos comprar: ['Flora', 'Miguelita']
```

```
python brute_force.py cows.csv 6000
Producción máxima: 244
Peso de la combinación: 1900
Listado de vacas que deberíamos comprar: ['Jacinta', 'Bernarda', 'Margarita', 'Flora', 'Miguelita', 'Fulgencia']
```

### ``dynamic_programming.py``

Habría que dar dos argumentos de línea de comandos:

* **Argumento 1**: fichero ``csv`` con los datos de entrada.
* **Argumento 2**: peso máximo permitido por el camión.

```
python dynamic_programming.py cows.csv 600
Producción máxima: 92
Peso de la combinación: 570
Listado de vacas que deberíamos comprar: ['Miguelita', 'Flora']
```

```
python dynamic_programing.py cows.csv 6000
Producción máxima: 244
Peso de la combinación: 1900
Listado de vacas que deberíamos comprar: ['Fulgencia', 'Miguelita', 'Flora', 'Margarita', 'Bernarda', 'Jacinta']
```

# Análisis de rendimiento

Navegando al directorio [performance_study](https://gitlab.com/dilasgoi/theegg_ai/-/tree/master/tarea_22/performance_study) puedes echar el ojo a un sencillo análisis de rendimiento de las dos implementaciones.

# Links de interés

* [Reto](http://www.nachocabanes.com/retos/reto.php?n=07)
