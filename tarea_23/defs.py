import random
import sys
import re

def normalize_input(text):
    """Esta funcion elimina espacios en blanco, los caracteres
    ,.:;¿?¡! y convierte minusculas en mayusculas"""
    return re.sub('[.,:;¿?¡! ]', '', text).upper()

def generate_shuffled_deck():
    """Esta función genera una baraja mezclada. Las
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
    """Esta función desplaza una carta hacia abajo"""
    index = deck.index(card)
    if index < 53:
        deck[index], deck[index + 1] = deck[index + 1], deck[index]
    else:
        deck[1:] = deck[-1:] + deck[1:-1]        
    return deck

def split_in_three(deck):
    """Esta función corta en 3 trozos una baraja 
    tomando los comodines como pivotes y reordena"""
    first_joker_index  = min(deck.index(53), deck.index(54))
    second_joker_index = max(deck.index(53), deck.index(54))

    return deck[second_joker_index + 1:] + deck[first_joker_index:second_joker_index + 1] + deck[:first_joker_index]
    
def final_cut(deck):
    """ Corte final de la baraja"""
    if deck[-1] is not 53 or deck[-1] is not 54:
        return deck[deck[-1]:-1] + deck[:deck[-1]] + [deck[-1]]

def generate_keystream(input_text, deck):
    keystream = []
    while len(keystream) < len(input_text):
        deck = move_1_card_down(deck, 53)
        deck = move_1_card_down(deck,54)
        deck = move_1_card_down(deck,54)
        deck = split_in_three(deck)
        deck = final_cut(deck)
        if deck[0] < 54:
            if deck[deck[0]] != 53 and deck[deck[0]] != 54:
                keystream.append(deck[deck[0]])
        else:
            if deck[deck[0] - 1] != 54 and deck[deck[0] - 1] != 53:
                keystream.append(deck[deck[0] - 1])
    return keystream

def encrypt_text(keystream, message):
    """Dada una ristra (keystream) cifra un mensaje (message)"""
    ascii_value_list = [ord(char) - 65 for char in message]
    cypher = [(keystr_val + ascii_val) % 26 for keystr_val, ascii_val in zip(keystream, ascii_value_list)]
    return [chr(item + 65) for item in cypher]

def decrypt_text(keystream, cypher):
    """Dado un mensaje cifrado (cypher) devuelve el texto descifrado"""
    ascii_value_list = [ord(char) - 65 for char in cypher]
    text = [(ascii_val - keystr_val ) % 26 for keystr_val, ascii_val in zip(keystream, ascii_value_list)]
    return [chr(item + 65) for item in text] 

def keystream_to_char(keystream):
    """Convierte la ristra a carácteres"""
    return ''.join([chr((item % 26) + 65) for item in keystream])