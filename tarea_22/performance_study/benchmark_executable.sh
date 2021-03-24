#!/bin/bash

#############################################################
# Este script genera una serie de ficheros                  #
# con nombre random.csv en el directorio "data"             #
# con un número dado de vacas de nombre aleatorio           #
# y pesos en un rango predeterminado en el fichero          #
# generate_random_file.sh que se encuentra                  #
# en directorio "data". Posteriormente, lanza               #
# a ejecución los programas brute_force.py y                #
# dynamic_programming.py y guarda los tiempos de ejecución. #
#                                                           #
# Modo de empleo:                                           #
#                                                           #
# $ ./benchmark_executable                                  #
#                                                           #
# El tamaño máximo del problema esta "hardcodeado" a 20 en  #
# el segundo loop del programa                              #
#                                                           #
#############################################################

for i in dynamic_programming brute_force
  do
    echo "Size Time" > ${i}_performance.txt
    for j in {1..20}
      do
        cd ../data
        ./generate_random_file.sh $j
        cd ../performance_study
    
        TIME=$(python -m cProfile ../${i}/${i}.py random.csv 600 | 
        grep "function calls" |
        awk '{print $(NF-1)}')

        echo "${j} ${TIME}" >> ${i}_performance.txt
      done
  done
