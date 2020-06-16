import sys 

def check_and_assign_input():
    """ Esta función checkea que el input es un número"""
    try:
        int(sys.argv[1])
    except ValueError:
        print('Not a integer number')
    else:
        return int(sys.argv[1])


def decimal_to_binary(decimal_number):
    """Esta función convierte un número decimal a su
    representación binaria"""
    bit_list=[]

    while decimal_number > 1:
        remainder = decimal_number % 2
        decimal_number  = int(decimal_number/2)
        bit_list.append(remainder)
    bit_list.append(1)
 
    # Imprimir elementos de una lista sin separación en orden inverso
    print(*bit_list[::-1], sep="")

def main():
    decimal_number = check_and_assign_input()
    decimal_to_binary(decimal_number)

main()


