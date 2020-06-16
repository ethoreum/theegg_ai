# Enunciado

Crea un programa que dado un número entre 0.0001 y 0.9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

Por ejemplo, el número 0.25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.



# Observaciones

Dado un número de la forma <img src="https://render.githubusercontent.com/render/math?math=0.abcd">, es decir, <img src="https://render.githubusercontent.com/render/math?math=\frac{abcd}{10000}"> hayar su fracción irreducible.

La solución pasa por hallar los factores primos en común de un numerador <img src="https://render.githubusercontent.com/render/math?math=abcd"> de 4 cifras y el número 10000.

El número 10000 será siempre nuestro denominador, por lo tanto tiene sentido utilizar un conocimiento *a priori* de sus factores primos:

<img src="https://render.githubusercontent.com/render/math?math=10000 = 5^4 \cdot 2^4 = 5 \cdot 5 \cdot 5 \cdot 5 \cdot 2 \cdot 2 \cdot 2 \cdot 2">

# Soluciones propuestas

| Programa           | Lenguaje | Observaciones                                                                      |
|--------------------|----------|------------------------------------------------------------------------------------|
| tarea_21_simple.py | Python   | No calculamos los factores primos de 10000. Los damos por conocidos.               |
| tarea_21.py        | Python   | Calculamos los factores de 10000 y reducimos *abcd* todo lo que se pueda con ellos.|
| tarea_21_ultra_simple.py | Python | Halla el máximo común divisor con la función gcd de *numpy*. 

# Ejecución de los programas

## Programas en Python

### tarea_21_simple.py
```
python tarea_21_simple.py 0.2340
117 / 500
```

### tarea_21.py
```
python tarea_21.py 0.2340
117 / 500
```

### tarea_21_ultra_simple.py 
```
python tarea_21_ultra_simple.py 0.2340
117 / 500
```
