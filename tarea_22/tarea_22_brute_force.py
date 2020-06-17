import itertools
import pandas

def generate_all_combinations(total_number_of_cows):
    """Esta función devuelve en forma de lista binaria todas las combinaciones
    de vacas posibles"""
    combinations = list(itertools.product([0, 1], repeat=total_number_of_cows))
    return combinations

def get_allowed_combinations(combinations, weights, production):
    full_info_list=[]
    for combination in combinations:
        total_weight_per_combination = sum([bit * weights for bit, weights in zip(list(combination), weights)])
        total_production_per_combination = sum([bit * production for bit, production in zip(list(combination), production)])
        if total_weight_per_combination <= 600:
            full_info_list.append([combination, total_weight_per_combination, total_production_per_combination])
    return full_info_list

def main():
    # Definimos un DataFrame con a información de las vacas del csv
    cow_df = pandas.read_csv('cows.csv')

    total_number_of_cows = len(cow_df.index) - 1
    cows = cow_df.Name.tolist()
    weights = cow_df.Weight.tolist()
    production = cow_df.Production.tolist()
    max_weight = 600

    # Generar todas las combinaciones y conseguir aquellas que cumplen el criterio de peso
    combinations = generate_all_combinations(total_number_of_cows)
    allowed_combinations = get_allowed_combinations(combinations, weights, production)

    # Ordenamos allowed_combinations por el tercer elemento (Production) de cada elemento de la lista
    # y calculamos la que maximiza el el tercer elemento (Production). 
    max_combination = max(sorted(allowed_combinations, key = lambda x: int(x[2])), key = lambda x: int(x[2]))
    
    # Imprimimos la producción máxima esperada
    print("Producción máxima:", max_combination[2])

    # Opcionalmente podemos conseguir el peso de la combinación que maximiza la producción
    print("Peso de la combinación:", max_combination[1])

    # Opcionalmente podemos conseguir los nombre de las vacas que deberíamos comprar 
    mask = list(max_combination[0])
    print("Listado de vacas que deberíamos comprar:", list(itertools.compress(cows, mask)))

main()
