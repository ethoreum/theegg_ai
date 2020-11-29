import argparse
from defs import *

def main():
    # Parsear argumentos de línea de commandos
    parser = argparse.ArgumentParser()

    # Argumentos de línea de comandos requeridos
    parser.add_argument('input_text', type=str, help='Texto de entrada entre comillas simples.')
    parser.add_argument('operation', type=str, help='Operación: puede ser "encrypt" o "decrypt".')

    # Parsear los argumentos dados y almacenarlos en una lista
    args = parser.parse_args()

    input_text = normalize_input(args.input_text)
    deck = generate_shuffled_deck()
    keystream = generate_keystream(input_text, deck)

    # Ejecutar la operación requerida sobre el input y mostrar salida
    eval(args.operation)(args, keystream, input_text)

main()


