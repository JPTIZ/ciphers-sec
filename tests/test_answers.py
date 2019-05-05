from ciphers import (
    caesar,
    monoalphabetic,
    playfair,
    vigenere,
)


def test_caesar():
    cipher = caesar.cipher

    ENTRIES = [
        ('vamos estudar segurança', 3, 'YDPRV HVWXGDU VHJXUDQFD'),
        ('PHHW PH DIWHU WKH WRJD SDUWB', -3, 'MEET ME AFTER THE TOGA PARTY')
    ]

    for source, shift, expected in ENTRIES:
        assert cipher(source, shift) == expected

    assert cipher('vamos estudar segurança', 3) != 'aaaaaaaaaaaaaaaaaaaaaaa'
    assert cipher('vamos estudar segurança', 4) != 'YDPRV HVWXGDU VHJXUDQFD'


def test_monoalphabetic():
    MAPPING = {
        'A': 'Z',
        'B': 'A',
        'C': 'K',
        'D': 'L',
        'E': 'J',
        'F': 'P',
        'G': 'Q',
        'H': 'T',
        'I': 'E',
        'J': 'R',
        'K': 'B',
        'L': 'M',
        'M': 'X',
        'N': 'C',
        'O': 'W',
        'P': 'S',
        'Q': 'H',
        'R': 'G',
        'S': 'F',
        'T': 'I',
        'U': 'U',
        'V': 'Y',
        'W': 'O',
        'X': 'D',
        'Y': 'N',
        'Z': 'V',
    }

    assert (
        monoalphabetic.cipher('vamos estudar segurança', MAPPING) ==
        'YZXWF JFIULZG FJQUGZCKZ'
    )


def test_playfair():
    KEY = 'LABSEC'

    assert (
        playfair.cipher('departamentodeinformática', KEY) ==
        'HAQLTUBKSOUNHAKOHMXRSQPIBW'
    )


def test_vigenere():
    KEY = 'secretofmana'

    assert (
        vigenere.cipher('The hero shall wield the sword', KEY) ==
        'LLG LXFT SUADP NMXZI TUE WYFVW'
    )
