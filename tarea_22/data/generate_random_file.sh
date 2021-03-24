#!/bin/bash

#########################################################
# Este script crea un fichero con una lista             #
# de vacas de nombre aleatorio y peso en un rango       #
# de 140 a 400 kilos y una producción entre 20 y 65     #
# litros de leche diaria.                               #
#                                                       #
# Modo de empleo:                                       #
#                                                       #
# $ ./generate_random_file.sh N                         #
#                                                       #
# Donde N es el número de vacas que queremos considerar #
#                                                       #
# Este script ha de ser ejecutado por la shell "bash"   #
#                                                       #
#########################################################

if [ -f "random.csv" ] ; then
    rm "random.csv"
fi

echo "Name,Weight,Production" >> random.csv

for i in $(seq 1 $1) 
  do
    NAME=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13 ; echo '')
    WEIGHT=$(shuf -i 140-400 -n 1)
    PRODUCTION=$(shuf -i 20-65 -n 1)
    echo "${NAME},${WEIGHT},${PRODUCTION}" >> random.csv
  done
