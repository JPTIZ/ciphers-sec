'''Contains Vigenère cipher algorithm implementation.'''
from itertools import cycle

from . import caesar
from .utils import ALPHABET


def cipher(text, key):
    key = key.upper()

    return ''.join(
        caesar.cipher(
            char,
            shifts=ALPHABET.index(k) if k in ALPHABET else 0
        )
        for char, k in zip(text, cycle(key))
    )
