'''Playfair cipher algorithm.'''
from unicodedata import normalize

from ciphers.utils import ALPHABET, grouper


def remove_accents(text: str) -> str:
    return normalize('NFKD', text).encode('ascii', 'ignore').decode()


def cipher(text: str, key: str) -> str:
    def row_col(c, mapping):
        return (
            mapping.index(c) % 5,
            mapping.index(c) // 5,
        )

    def replace(pair, mapping):
        pos = [
            [mapping.index(rc) % 5,
             mapping.index(c) // 5]
            # if rc in mapping else [-1, -1]
            for c, rc in zip(pair, reversed(pair))
        ]

        # if on the same line...
        if pos[0][1] == pos[1][1]:
            pos[0][0], pos[1][0] = pos[1][0] + 1, pos[0][0] + 1

        # if on the same column...
        if pos[0][0] == pos[1][0]:
            pos[0][1] += 1
            pos[1][1] += 1

        return ''.join(
            mapping[p[0] % 5 + p[1] * 5]
            if p != [-1, -1] else c
            for c, p in zip(pair, pos)
        )

    missing_letters = ''.join(
        a for a in ''.join(ALPHABET.split('J')) if a not in key
    )
    mapping = key + missing_letters

    text = remove_accents(''.join(
        c + 'x' if c == next_c or next_c == '\0' else c
        for c, next_c in zip(text, text[1:] + '\0')
    ).replace('j', 'i').upper())

    return ''.join(
        replace(pair, mapping)
        for pair in grouper(text, 2, 'x')
    )


if __name__ == '__main__':
    cipher('', 'LABSEC')
