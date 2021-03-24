import sys

def sort_dna_chain(chain1, chain2):
    if len(chain1) < len(chain2):
        dna_short = chain1
        dna_long = chain2
    else:
        dna_short = chain2
        dna_long = chain1
    return dna_short, dna_long

if __name__ == "__main__":

    (dna_short, dna_long) = sort_dna_chain(sys.argv[1], sys.argv[2])

    for window in reversed(range(len(dna_short))):
        for pivot in range(len(dna_short) - window):
            check_sequence = dna_short[pivot : pivot + window + 1]
            try:
                dna_long.index(check_sequence)
            except ValueError:
                    print("Not found!")
            else:
                    print("Found!")
    
#    for item in sorted(sequence_list, key=len, reverse = True):
#        if item in dna_long:
#            print(item)
#            break

#    for window in range(len(dna_short)):
#        for pivot in range(len(dna_sort))
#            check_sequence = dna_short[pivot:window + 1]
#            print(check_sequence)
#
