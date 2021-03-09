def caesar_cipher(ciphered_text, key):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    deciphered_text = ""
    for ciphered_alphabet in ciphered_text:
        if ciphered_alphabet.isalpha():
            location_in_alphabets = alphabets.index(ciphered_alphabet)
            deciphered_text += alphabets[(location_in_alphabets - key) % 26]
    return deciphered_text
