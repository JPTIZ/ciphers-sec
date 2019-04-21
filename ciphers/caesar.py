'''Caesar's cipher.'''


def cipher(plaintext, shifts=3):
    ALPHABET = [chr(c + ord('A')) for c in range(26)]

    plaintext = plaintext.upper().replace('Ç', 'C')
    return ''.join(
        ALPHABET[(ALPHABET.index(c) + shifts) % len(ALPHABET)]
        if c >= 'A' and c <= 'Z' else c
        for c in plaintext
    )
