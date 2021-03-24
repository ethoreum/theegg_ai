import math
import numpy as np
import pandas as pd
import sys

def find_max_value_index(M):
    '''Encuentra la primera ocurrencia
    (leyendo de izquierda a derecha y de arriba a abajo)
    del número máximo de la matriz M.'''
    result = np.where(M == np.amax(M))
    return list(zip(result[0], result[1]))[0]

def calculate_matrix(weights, range_of_weights):
    '''Calcula la Matrix M con las producciones
    maximas para cada escenario.'''
    M = np.zeros((len(weights), len(range_of_weights)))
    for i in range(len(weights)):
        for j in range(len(range_of_weights)):
            if (weights[i] <= range_of_weights[j]):
                k = range_of_weights.index(range_of_weights[j] - weights[i])
                M[i][j] = max(production[i] + M[i-1][k], M[i-1][j])
            else:
                # Es importante comentar que fuera de los límites de un array
                # inicializado a 0, por ejemplo la entrada M[-1][0], el valor
                # del elemento es 0. De ahí que no hagamos casuística explicita 
                # para estos elementos
                M[i][j] = M[i-1][j]
    return M

def find_cows(weights, M, max_value_index, range_of_weights):
    '''Encuentra la combinación de vacas que máximiza la producción'''
    cow_list=[]
    x = max_value_index[0]
    y = max_value_index[1]
    peso = range_of_weights[y]
    
    while(peso > 0):
        if M[x][y] != M[x-1][y]:
            cow_list.append(x)
            peso = peso - weights[x]
            y = range_of_weights.index(range_of_weights[y] -  weights[x])
            x = x - 1
        else:
            if x - 1 < 0:
                cow_list.append(x)
                break
            else:
                x = x - 1
    return cow_list

def print_results(cows):
    '''Imprime los resultados por pantalla'''
    total_weight = 0
    total_production = 0
    cow_list = []
    for cow in cows:
        cow_list.append(cows_names[cow])
        total_weight += weights[cow]
        total_production += production[cow]
    print("Producción máxima:", total_production)
    print("Peso de la combinación:", total_weight)
    print("Listado de vacas que deberíamos comprar:", cow_list)

if __name__ == "__main__":

    # Datos de entrada
    cow_df = pd.read_csv('../data/' + sys.argv[1])

    # Convertimos a listas algunas columnas del DataFrame
    cows_names = cow_df.Name.tolist()
    weights = cow_df.Weight.tolist()
    production = cow_df.Production.tolist()
    
    # Leemos el peso máximo y generamos una lista con un rango
    # de pesos desde 0 hasta el peso máximo.
    max_weight = int(sys.argv[2])
    range_of_weights = list(range(0, max_weight + 1))
 
    # Calcular resultados
    M = calculate_matrix(weights, range_of_weights)
    max_value_index = find_max_value_index(M)
    cows = find_cows(weights, M, max_value_index, range_of_weights)
    
    # Impresión de resultados
    print_results(cows)
