from defs import *

def main():

    input_text = normalize_input(sys.argv[1])
    deck = generate_shuffled_deck()
    keystream = generate_keystream(input_text, deck)
    
    if sys.argv[2] == 'cypher':
        cypher = encrypt_text(keystream, input_text)
        plain_text = decrypt_text(keystream, ''.join(cypher))
        print("Texto sin cifrar: ", ''.join(plain_text))
        print("Clave de cifrado: ", keystream_to_char(keystream))
        print("Texto cifrado   : ", ''.join(cypher))
    elif sys.argv[2] == 'decypher':
        plain_text = decrypt_text(keystream, input_text)
        cypher = encrypt_text(keystream, ''.join(plain_text))
        print("Texto cifrado   : ", ''.join(cypher))
        print("Clave de cifrado: ", keystream_to_char(keystream))
        print("Texto sin cifrar: ", ''.join(plain_text))
        
main()


