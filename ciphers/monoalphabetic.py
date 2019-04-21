'''Monoalphabetic cipher algorithm.'''


def cipher(plaintext, mapping):
    return ''.join(
        mapping[c.upper()] if c.upper() in mapping else c
        for c in plaintext.replace('ç', 'c')
    )
