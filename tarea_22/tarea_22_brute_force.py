import itertools
import pandas

def generate_all_combinations(total_number_of_cows):
    """Esta función devuelve en forma de lista binaria todas las combinaciones
    de vacas posibles"""
    combinations = list(itertools.product([0, 1], repeat=total_number_of_cows))
    return combinations

def main():
    # Definimos un DataFrame con a información de las vacas del csv
    cow_df = pandas.read_csv('cows.csv')

    total_number_of_cows = len(cow_df.index) - 1
    cows = cow_df.Name.tolist()
    weights = cow_df.Weight.tolist()
    production = cow_df.Production.tolist()
    max_weight = 600

    combinations = generate_all_combinations(total_number_of_cows)

    full_info_list=[]

    for combination in combinations:
        total_weight_per_combination = sum([bit * weights for bit, weights in zip(list(combination), weights)])
        total_production_per_combination = sum([bit * production for bit, production in zip(list(combination), production)])
        if total_weight_per_combination <= 600:
            full_info_list.append([combination, total_weight_per_combination, total_production_per_combination])
    
    mask = list(max(sorted(full_info_list, key = lambda x: int(x[2])), key = lambda x: int(x[2]))[0])
    print(list(itertools.compress(cows, mask)))

main()
