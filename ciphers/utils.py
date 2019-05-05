'''General utilities for cipher algorithms.'''
from itertools import zip_longest


ALPHABET = ''.join(chr(c + ord('A')) for c in range(26))


def grouper(iterable, n, fillvalue=None):
    '''
    (From itertools#recipes)
    Collect data into fixed-length chunks or blocks.

    Example: grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    '''
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
