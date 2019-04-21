'''Caesar's cipher.'''
from ciphers.utils import ALPHABET


def cipher(plaintext, shifts=3):
    plaintext = plaintext.upper().replace('Ç', 'C')
    return ''.join(
        ALPHABET[(ALPHABET.index(c) + shifts) % len(ALPHABET)]
        if c >= 'A' and c <= 'Z' else c
        for c in plaintext
    )
