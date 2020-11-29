import sys 

def check_and_assign_input():
    """ Esta función checkea que el input es un número entero"""
    try:
        int(sys.argv[1])
    except ValueError:
        print('Not an integer number')
    else:
        return int(sys.argv[1])

def decimal_to_binary(decimal_number):
    """Esta función convierte un número decimal a su
    representación binaria"""
    bit_list=[]
    if decimal_number > 0:
        while decimal_number > 0:
            remainder = decimal_number % 2
            decimal_number  = decimal_number // 2
            bit_list.append(remainder)
    else:
        bit_list.append(0)
 
    # Imprimir elementos de una lista sin separación en orden inverso
    print(*bit_list[::-1], sep="")

def main():
    decimal_number = check_and_assign_input()
    decimal_to_binary(decimal_number)

if __name__ == "__main__":
    main()


