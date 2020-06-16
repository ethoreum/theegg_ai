# Construye un simulador

En este caso hay que desarrollar un programa donde una vez enviado un valor decimal a una función
este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor
analógico digital mediante un programa (software). El hardware lo dejamos para otro día.

# Observaciones

## Para números positivos

Iremos dividiendo por 2 y guardando el resto. Por ejemplo:

| Número decimal | Cociente | Resto |
|----------------|----------|-------|
| 67             | 33       | **1** |
| 33             | 16       | **1** |
| 16             | 8        | **0** |
| 8              | 4        | **0** |
| 4              | 2        | **0** |
| 2              | **1**    | **0** |

La representacón en binario será la lista de *bits* de la columna *Resto* leída de abajo a arriba 
comenzando por el último cociente. Para este caso:

<img src="https://render.githubusercontent.com/render/math?math=1000011">

## Para números positivos y negativos

### Complemento de unos

### Complemento de dos

# Soluciones propuestas

| Programa           | Lenguaje | Observaciones                                                                      |
|--------------------|----------|------------------------------------------------------------------------------------|
| tarea_24_positivos.py | Python   | Obtenemos la representación binaria para números positivos únicamente               |
| tarea_24_complemento_de_dos.py        | Python   | Obtenemos la representación binaria par números positivos y negativos hasta de 8 bits [-127,128].|
| tarea_21_builtin_bin.py | Python | Obtenermos la representación binaria con la función *bin* de Python |

# Ejecución de los programas

## tarea_24.py
```
python tarea_24.py 8
100
```

# Links de interés

* [Simulador online](https://www.calculadoraconversor.com/decimal-a-binario-online/)
