import random
import re

def normalize_input(text):
    """Elimina espacios en blanco, los caracteres
    ,.:;¿?¡! y convierte minusculas en mayusculas"""
    return re.sub('[.,:;¿?¡! ]', '', text).upper()

def generate_shuffled_deck():
    """Genera una baraja mezclada. Las
    cartas están así representadas:
    1-13  : Clubs
    14-26 : Diamonds
    27-39 : Hearts
    40-52 : Spades
    53    : A
    54    : B
    """
    deck = [item for item in range(1,55,1)]
    #random.shuffle(deck)
    return deck

def move_1_card_down(deck, card):
    """Desplaza una carta hacia abajo"""
    index = deck.index(card)
    if index < 53:
        deck[index], deck[index + 1] = deck[index + 1], deck[index]
    else:
        deck[1:] = deck[-1:] + deck[1:-1]        
    return deck

def split_in_three(deck):
    """Corta en 3 trozos una baraja 
    tomando los comodines como pivotes y reordena"""
    first_joker_index  = min(deck.index(53), deck.index(54))
    second_joker_index = max(deck.index(53), deck.index(54))

    return deck[second_joker_index + 1:] + deck[first_joker_index:second_joker_index + 1] + deck[:first_joker_index]
    
def final_cut(deck):
    """Corte final de la baraja"""
    if deck[-1] != 53 or deck[-1] != 54:
        return deck[deck[-1]:-1] + deck[:deck[-1]] + [deck[-1]]

def generate_keystream(input_text, deck):
    """Genera la ristra a partir de la baraja de entrada"""
    keystream = []
    # Hay que generar tantos elementos de ristra como caracteres hay
    # en el texto de entrada
    while len(keystream) < len(input_text):
        deck = move_1_card_down(deck, 53)
        deck = move_1_card_down(deck, 54)
        deck = move_1_card_down(deck, 54)
        deck = split_in_three(deck)
        deck = final_cut(deck)
        if deck[0] < 54:
            if deck[deck[0]] != 53 and deck[deck[0]] != 54:
                keystream.append(deck[deck[0]])
        else:
            if deck[deck[0] - 1] != 54 and deck[deck[0] - 1] != 53:
                keystream.append(deck[deck[0] - 1])
    return keystream

def encrypt(args, keystream, message):
    """Dada una ristra (keystream) cifra un mensaje (message) y muestra la salida de la operación"""
    ascii_value_list = [ord(char) - 65 for char in message]
    numeric_cypher = [(keystr_val + ascii_val) % 26 for keystr_val, ascii_val in zip(keystream, ascii_value_list)]
    cypher = [chr(item + 65) for item in numeric_cypher]
    print("Texto sin cifrar: ", ''.join(args.input_text))
    print("Clave de cifrado: ", keystream_to_char(keystream))
    print("Texto cifrado   : ", ''.join(cypher))

def decrypt(args, keystream, cypher):
    """Dado un mensaje cifrado (cypher) devuelve el texto descifrado y muestra la salida de la operación"""
    ascii_value_list = [ord(char) - 65 for char in cypher]
    numeric_text = [(ascii_val - keystr_val ) % 26 for keystr_val, ascii_val in zip(keystream, ascii_value_list)]
    plain_text = [chr(item + 65) for item in numeric_text] 
    print("Texto cifrado   : ", ''.join(args.input_text))
    print("Clave de cifrado: ", keystream_to_char(keystream))
    print("Texto sin cifrar: ", ''.join(plain_text))

def keystream_to_char(keystream):
    """Convierte la ristra a carácteres"""
    return ''.join([chr((item % 26) + 65) for item in keystream])
