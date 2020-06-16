import sys

def check_and_assign_input():
    """ Esta función checkea que el input es un número"""
    try:
        int(sys.argv[1])
    except ValueError:
        print('Not a integer number')
    else:
        return int(sys.argv[1])

def main():
    decimal_number = check_and_assign_input()
    print(bin(decimal_number)[2:])

main()
