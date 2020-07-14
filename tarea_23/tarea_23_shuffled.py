from defs import *

def main():
    input_text = normalize_input(sys.argv[1])
    deck = generate_shuffled_deck()
    keystream = generate_keystream(input_text, deck)
    
    if sys.argv[2] == 'encrypt':
        cypher = encrypt_text(keystream, input_text)
        print("Texto sin cifrar: ", ''.join(sys.argv[1]))
        print("Clave de cifrado: ", keystream_to_char(keystream))
        print("Texto cifrado   : ", ''.join(cypher))
    elif sys.argv[2] == 'decrypt':
        plain_text = decrypt_text(keystream, input_text)
        print("Texto cifrado   : ", ''.join(sys.argv[1]))
        print("Clave de cifrado: ", keystream_to_char(keystream))
        print("Texto sin cifrar: ", ''.join(plain_text))
main()


