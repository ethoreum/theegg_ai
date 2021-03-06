# Cifrado y descifrado con el solitario	

Según la descripción de la wikipedia, el cifrado es un procedimiento que utiliza un algoritmo con cierta
clave (clave de cifrado) para transformar un mensaje, sin atender a su estructura lingüística o
significado, de tal forma que sea incomprensible o, al menos, difícil de comprender a toda persona que
no tenga la clave secreta (clave de descifrado) del algoritmo. Las claves de cifrado y de descifrado
pueden ser iguales (criptografía simétrica), distintas (criptografía asimétrica) o de ambos tipos
(criptografía híbrida), tal y como se describe en el siguiente link de genbeta.
Pues bien, en la siguiente tarea, el alumno debe construir una comunicación cifrada entre dos funciones
utilizando el algoritmo del solitario:

1. Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la
función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings,
enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de
tipo String.

2. Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo.


# Soluciones propuestas 

| Programa        | Lenguaje | Observaciones                                                                        |
|-----------------|----------|--------------------------------------------------------------------------------------|
| tarea_23.py     | Python   | Clave generada con una baraja barajada aleatoriamente. Input como CLA\*.             |

\* CLA: **C**ommand **L**ine **A**rgument (Argumento de Línea de Comandos).

| Fichero | Lenguaje | Observaciones                                                                        |
|---------|----------|--------------------------------------------------------------------------------------|
| defs.py |  Python  | Contiene las funciones utilizadas en el main.                                        |

# Ejecución de los programas

## ``tarea_23.py``

Habría que aportar dos argumentos de línea de comandos de manera obligatoria:

* Texto de entrada entre comillas simples.
* Operación a realizar sobre el texto de entrada: "encrypt" o "decrypt"

Se puede consultar la ayuda con un:
```
$ python tarea_23.py -h
usage: tarea_23.py [-h] input_text operation

positional arguments:
  input_text  Texto de entrada entre comillas simples.
  operation   Operación: puede ser "encrypt" o "decrypt".

optional arguments:
  -h, --help  show this help message and exit
```

En estos ejemplos se ha empleado una baraja ordenada (1,2,3,...,52,53,54) para generar la clave. El primer argumento habría que darlo entre comillas simples para que todos los caracteres se interpreten de manera literal. Si sólo hubiera caracteres alfabéticos no sería necesario.

### Cifrado

```
$ python tarea_23_shuffled.py 'Bienvenidos al salvaje oeste.' encrypt
Texto sin cifrar:  BIENVENIDOSALSALVAJEOESTE
Clave de cifrado:  EXKYIZSGEHUNTIQVVSYKAZXZI
Texto cifrado   :  FFOLDDFOHVMNEAQGQSHOODPSM
```

El programa es capaz de eliminar los caracteres: ,.;:¡!?¿ y también admite mayúsculas y minusculas:

```
$ python tarea_23_shuffled.py 'Bi,.,.,.,,envenidosalsalvajeoeste!!!!!!!!!' encrypt
Texto sin cifrar:  BIENVENIDOSALSALVAJEOESTE
Clave de cifrado:  EXKYIZSGEHUNTIQVVSYKAZXZI
Texto cifrado   :  FFOLDDFOHVMNEAQGQSHOODPSM
```

### Descifrado

```
$ python tarea_23_shuffled.py 'FFOLDDFOHVMNEAQGQSHOODPSM' decrypt
Texto cifrado   :  FFOLDDFOHVMNEAQGQSHOODPSM
Clave de cifrado:  EXKYIZSGEHUNTIQVVSYKAZXZI
Texto sin cifrar:  BIENVENIDOSALSALVAJEOESTE
```

```
$ python tarea_23_shuffled.py 'FFOLDDFOHVMN!!EAQGQ..;.;.;.SHOODPSM' decrypt
Texto cifrado   :  FFOLDDFOHVMNEAQGQSHOODPSM
Clave de cifrado:  EXKYIZSGEHUNTIQVVSYKAZXZI
Texto sin cifrar:  BIENVENIDOSALSALVAJEOESTE
```

# Links de interés

* [Cifrado con el solitario](https://sindominio.net/biblioweb/telematica/solitario.html)
