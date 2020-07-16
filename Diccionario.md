# Diccionario

## Alan Turing

Padre teórico del ordenador y el precursor de la inteligencia artificial.

### Máquina de Turing

### Aportaciones

* Ideó el test que lleva su nombre que consiste en medir la capacidad de una computadora o programa
de hacerse pasar por humano.
* Fue capaz de cracker Enigma (la máquina que usaban los alemanes para cifrar sus mensajes) otorgando al ejército
británico la capacidad de localizar a los submarinos alemanes.
* Demostró que habia problemas no resolubles algorítmicamente.

## Algoritmo 

Secuencia de pasos o tareas destinadas a llevar a cabo una función específica.

## API 

La API (**A**pplication **P**rogramming **I**nterface) se trata de una especie de reglas de traducción para poder interactuar con un servicio ya creado; una especie de intermediario de alto nivel. De este modo, haciendo llamadas a la API, podemos interactuar con ese servicio sin tener que saber demasiado de cómo está desarrollado.

El número de llamadas a la API que podemos hacer está limitado por el proveedor del servicio y dado un número muy grande de llamadas podemos tener que pasar por caja.

Las APIs también pueden ser utilizadas por servicios para intercambiar información entre sí.

## Arduino

Es un proyecto de software y hardware libre que fabrica placas de desarrollo con finalidad educativa.

Los procesadores son de arquitectura ARM actualmente, pero eran AVR en sus inicios.

## Arquitectura cliente-servidor

Consiste en, básicamente, una arquitectura en la que un cliente (el que hace peticiones) realiza peticiones a un sistema que responde a dichas peticiones (servidor).

Ejemplo:

- cliente(s) solicita(n) valores de una tabla de una base de datos. Existe por tanto un servidor que procesa la petición y envía la información solicitada al cliente.
- cliente(s) solicita(n) una página web. Existe por tanto un servidor web que procesa la petición y devuelve la página web.

## Arquitectura Von Neumann

Se trata de arquitectura de computadoras ideada por por el matemático y físico John von Neumann. 

Está formado por una CPU que a su vez contiene una ALU (Arithmetic Logic Unit), los registros del procesador, una unidad de control y un contador de programa. También posee una memoria principal y un mecanismo de entrada y salida.

## Arquitectura Harvard

Se diferencia de la Von Neumann principalmente por la división de las instrucciones de los datos que se comunican con la unidad central de proceso en dos espacis de memoria separados.

## Bases de datos

Se trata de una colección de datos ordenada. En función del tipo de dato que almacenan las bases de datos pueden ser de muchos tipos (estáticos o dinámicos) y tener diferentes formatos (SQL, CSV).

Del mismo modo, también atienden a modelos diferentes: jerarquicas (LDAP), relacionales (SQL), noSQL(MongoDB).


## Bucles

Se trata de un conjunto de instrucciones que se repite hasta que una situación es satisfecha. Pueden ser de tipo ``while`` o de tipo ``for``, por ejemplo.

## Criptografía

La ciencia y el arte de esconder información.

### Cifrado simétrico

También conocido como "Cifrado de clave simétrica". Se trata de un método de cifrado que utiliza la misma clave para cifrar y descifrar.

El problema de estos sistemas de cifrado es la compartición y distribución de las claves, ya que toda la seguridad del cifrado recae en esta.

### Cifrado asimétrico

Es un método de cifrado que utiliza dos claves: una pública (la que se distribuye)  y una privada (que el propietario debe guardar celosamente).

Cuando queremos cifrar un mensaje, utilizamos la clave pública del destinatario para hacerlo, ya que sólo la clave privada de este último puede descifrar el mensaje.qqqq

## Compilador

Un compilador es un programa que traduce código escrito en un lenguage de programación (código fuente) en otro lenguage de programación. El lenguaje objetivo puede ser lenguaje máquina (0s y 1s) o algún lenguaje intermedio.

## Control de versiones

Conjunto de aplicaciones que permiten gestionar cambios en la vida de desarrollo de un elemento de software. También reducen los poblemas a la hora de establecer edición concurrente de un mismo proyecto

### Github, Gitlab

Son servicios web que permiten almacenar tu proyecto y aplicarle control de versiones de una manera amigable.

## CSS

Es un lenguaje utilizado para dotar de estilos a los elementos propios del lenguaje HTML. Por ejemplo: definir fuentes y sus tamaños, color o posición del elemento.

## Data processing

Como su nombre indica se trata del procesado/manipulación de datos. Esto puede incluir:

- Normalización (para ajustarlo a un formato requerido).
- Ordenación.
- Eliminación de entradas innecesarias.
- Reconstrucción de datos faltantes.
- Análisis.
- Resumen.
- CLasificación.


## Diagrama de flujo

Un diagrama de flujo es un tipo de diagrama que nos permite visualizar, con la ayuda de cajas de diferentes formas y flechas, los pasos que sigue un proceso (un algoritmo, por ejemplo). 

## DNS

Del inglés Domain Name System. Es un sistema descentralizado que permite traducir los nombres de las páginas web (URL) a direcciones IP.

Cada una de las máquinas que forman el sistema se denomina servidor DNS.

También podemos tener servidores DNS locales para poder traducir hostnames y URLs en nuestra propia red.

## Editor de código

Programa que permite la creación/edición de programas utilizando un lenguaje de programación. Dependiendo de lo complejos que sean o los plug-ins que tengan instalados tienen más o menos funcionalidades que pueden asistir al programador: navegador de archivos, resaltado de sintaxis, integración con control de versiones, integración con el compilador, etc.

Sólo existen dos que merezcan la pena en el mundo y los demás son innecesarios:

* Vim
* Emacs

## ETL

- Extraer (Extract)
- Transformar (Transform)
- Cargar (Load)


ETL es un proceso que extrae/adquiere información de diferentes fuentes, la trata/transforma + valida y finalmente la presenta de modo que pueda ser util.

## FTP

Se trata de un protocolo de red para el intercambio de ficheros entre un cliente y un servidor. Existe una variante segura que utiliza el protocolo SSH y que cifra las comunicaciones denominado sFTP.

## Hardware

Colección de elementos físicos que componen un computador.

## HTML

Se trata de un lenguaje por marcas que se utiliza para confeccionar páginas web, es decir, para confeccionar páginas que serán mostradas en un navegador web.

## Inteligencia artificial

Conjunto de estrategias y técnicas ejecutadas por las máquinas para resolver problemas y responder
a los estímulos a las que son sometidas. 

Estas técnicas o estrategias pueden haber sido desarroladas por humanos o por las propias máquinas.

### Inteligencia artificial débil

Estrategia de alcance muy específico desarrollada por máquina.

### Inteligencia artificial fuerte o general

Inteligencia emergente de una máquina que es elevada al nivel de la humana.

## Intérprete

Un intérprete es un programa que analiza y ejecuta simultáneamente un programa escrito en un lenguaje fuente. Esto es cómodo, y que no hay necesidad de compilar el código fuente, pero la contrapartida es que los lenguajes interpretados son, generalmente, más lentos que los compilados.

## IP

Una dirección IP (Internet Protocol address) es un código númerico que se utiliza para identificar equipos que están conectados a una red.

Existen actualmente dos protolocos:

- IPv4: donde las direcciones vienen dadas por 4 bytes: byte1.byte2.byte3.byte4. Un ejemplo en representación decimal: 192.168.2.3

- IPv6: debido a que el número de IPs codificadas por IPv4 se está agotando, se crea este protocolo. Aquí las direcciones pasan a tener 128 bits (por los 32 del protocolo IPv4). Ejemplo de dirección IP en IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

## Java

Es una lenguaje de programación de alto nivel y orientado a objetivos. 

Los programas de Java se ejecutan en la máquina virtual de Java (JVM) lo que lo hace independiente de la arquitectura y lo hace realmente portable. Actualmente la JVM es capaz de traducir a lenguaje máquina directamente (no a bytecode en exclusiva) lo que hace que el lenguaje sea un poco más rápido sacrificando la portabilidad.

## Javascript

Es un lenguaje de programación interpretado utilizado en la parte del cliente para mejorar la usabilidad y las capacidades de las páginas web otorgándoles dinamismo.

<details>
  <summary><code>Hola Mundo</code> en Javascript</summary>
  ```
  console.log("Hello world!");
  ```
</details>

## JSON

JSON (**J**avaScript **O**bject **No**tation) es un formato de texto sencillo para el intercambio de datos. Ejemplo de JSON:
```
{
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitems": [
                {
                    "value": "New", "onclick": "CreateNewDoc()"
                },{
                    "value": "Open", "onclick": "OpenDoc()"
                },{
                    "value": "Close", "onclick": "CloseDoc()"
                }
            ]
        }
    }
}
```

Ejemplo que usamos en el programa de proceso de logs:
```
[
    {
        "job identifier": "12334",
        "username": "dilasgoi",
        "group": "scicomp",
        "queue": "p-slow-small",
        "qtime": "1473500781",
        "start": "1473506777",
        "end": "1473703916",
        "Resource_List.cput": "720000",
        "Resource_List.mem": "1",
        "total_execution_slots": "1",
        "unique_node_count": "1",
        "Exit_status": "0",
        "resources_used.mem": "379804kb",
        "resources_used.walltime": "23342"
    }
]
```

## Lenguaje de programación

Abstración sobre el lenguaje máquina (0s y 1s) que permite interactuar con esta a un nivel más alto.

### Lenguaje de alto nivel

Un lenguaje de alto nivel es aquel que se aproxima más al lenguaje natural humano que al lenguaje de máquina. Cuantas más abstracciones nos alejen del lenguaje de máquina más se asemejará un lenguaje de alto nivel al del ser humano. Las contrapartidas más notables son:

* Menor capacidad para interactuar directamente con los componentes físicos (hardware) de la computadora. Por tanto, no es posible confeccionar programas tan rápidos ni eficientes (en términos de uso de memoria, por ejemplo) como los que se consiguen con lenguajes de bajo nivel.

* Los programas utilizan, típicamente, más recursos.

### Lenguaje de bajo nivel

### Lenguaje compilado

### Lenguaje interpretado

Son lenguajes, generalmente, de alto nivel cuyo código no necesita ser procesado mediante un compilador. Es el propio intérprete el que se encarga de la traducción a un lenguaje que entienda la máquina.

Son lenguajes, generalmente, más lentos que los compilados.

### Lenguaje de máquina

Es el lenguaje capaz de ser ejecutado por las unidades procesadoras de los computadores.

Cada familia de procesadores tiene su conjunto de instrucciones en este lenguaje. Es por ello que algunos procesadores son capaces de realizar operaciones más rápidamente que otros. Ejemplos de set de instrucciones:

* SSE
* SSE2
* AVX 
* AVX-521

## LISP

Se trata de un lenguaje (con muchos dialectos) de programación multiparadigma y, en sus versiones actuales, compilado. Aunque pueda parecer de nicho, es un lenguaje de propósito general.

Lo curioso de este lenguaje es que su elemento funcional es la lista (el nombre procede de *ListProcessing*), que se utiliza para todo. Como éstas están delimitadas con paréntesis, la estructura del código queda muy curiosa en ocasiones.

## Ley de Moore

La ley de Moore expresa que aproximadamente cada dos años se duplica el número de transistores en un microprocesador.

Actualmente, debido a las dificultades para crear transistores más pequeños debido a el estancamiento en las tecnologías de miniaturización y a los efectos cuáticos que aparecen a estas escalas, la Ley de Moore no se está cumpliendo.

## NoSQL

El nombre de la base de datos NoSQL proviene de Not only SQL. Esto se debe a que este tipo de base de datos suele evitar el uso del SQL. El hecho de evitar el SQL es porque se usa para proyectos en los que se necesita trabajar en la base de datos con un gran volumen. En las bases de datos con lenguaje SQL, los distintos atributos de un elemento, están en diferentes columnas, mientras que en una NoSQL todos los atributos se encuentran en una misma columna, ahorrando espacio y ganando en rendimiento. Algunos ejemplos de lenguajes usados por bases de datos NoSQL son: JSON (JavaScript Object Notation); CQL (Contextual Query Language, anteriormente conocido como Common Query Language); o GQL (Graph Query Language). 

## Periféricos

Dispositivos de entrada y salida con los que interacturar con las componentes internos de un computador. Por ejemplo:

* Teclado
* Ratón
* Monitor
* Impresora

## PHP

## Programación

Ciencia y arte de interactuar con un computador a través de un lenguaje que abstrae el lenguaje máquina.

## Protocolo de comunicación

Conjunto de normas que tienen que cumplir dos interlocutores para poder entenderse. 

Estas reglas se definen a nivel de la sintaxis, la semántica, sincronización de la comunicación así como de la reduncancia de los mensajes y la corrección de errores.

## Protocolo TCP/IP

En inglés Internet protocol o IP, es un protocolo de comunicación de datos al nivel de red.

TCP/IP es un estándar de red que define las reglas para el intercambio de datos entre dispositivos de red y le permite acceder a Internet cada vez que necesita enviar un mensaje o recibir información de otro dispositivo. 

## Puertas lógicas

Dispositivo electrónico que opera sobre un conjunto de entradas binarias. Pueden usarse para definir funciones booleanas o sumadores. Las funciones booleanas más usuales son:

* AND
* OR
* XOR
* NAND
* NOT

Todas las puertas lógicas pueden constuirse con puertas NAND o XOR.

## [Python](https://www.python.org/psf/)

Python es un lenguaje de programación de alto nivel e interpretado de proposito general (además de gratuito y abierto). Del mismo modo es un lenguaje de programación multiparadigma: OOP, funcional, imperativo.

Entre sus objetivo está también el de la legibilidad.

Se trata de un lenguaje muy utilizado para Machine Learning ya que ofrece modulos y frameworks para abordar problemas de este campo de manera bastante directa: Tensorflow, Keras, PyTorch, SciKit-Learn, etc.

## [R](https://www.r-project.org/)

R es un lenguaje de programación de alto nivel, interpretado, gratuito y abierto además de un entorno de software para el análisis estadístico y gráfico. 

## Raspberry Pi

Pequeño computador de precio asequible con procesador de arquitectura ARM para pequeños proyectos.

## Servidor web

Un servidor web se trata de una capa de software (y el hardware) que puede responder peticiones en la web. Un servidor web es capaz de procesar peticiones de red sobre el protocolo HTTP, HTTPS, FTP, IPsec, etc.

Los servidores web más usados son:

- Apache
- Nginx
- Tomcat

## Sistema operativo

Se trata de un software para la gestión de los recursos computacionales de un computador. Se encarga de orquestar la gestión del usuario con el hardware y de facilitar la interacción con el mismo. Ejemplo:

* OpenBSD
* GNU/Linux
* Windows
* macOS
* Plan 9

## Software

Colección de programas y datos que permiten ejecutar instrucciones en un computador.

## SQL

Se trata de un lenguaje de programación para la gestión de bases de datos relacionales. Es por tanto, un lenguaje de propósito específico.

## Transistor

Elemento de circuitería digital que permite el paso de corriente o no en función de un voltaje de entrada. Sería una especie de grifo que deja no pasar el agua eléctrica o corriente.

En los procesadores modernos sirve para construir puertas lógicas que a su vez se utilizan para construir circuitería digital.

## XML

XML significa e**X**tensible **Ma**rkup **L**anguage.

Se trata de un lenguaje de marcas utilizado para almacenar datos en forma legible. Surgió debido a la necesidad de almacenar grandes cantidades de información, por lo que es muy común que sea utilizado en hojas de cálculo, bases de datos, editores de texto, etc.

Al contrario del HTML permite crear marcas propias para describir el contenido, creando un conjunto de símbolos ilimitado y autodefinido (de ahí Extensible).
