import ciphers.caesar as caesar


def test_caesar():
    cipher = caesar.cipher

    entries = [
        ('vamos estudar segurança', 3, 'YDPRV HVWXGDU VHJXUDQFD'),
        ('PHHW PH DIWHU WKH WRJD SDUWB', -3, 'MEET ME AFTER THE TOGA PARTY')
    ]

    for source, shift, expected in entries:
        assert cipher(source, shift) == expected

    assert cipher('vamos estudar segurança', 3) != 'aaaaaaaaaaaaaaaaaaaaaaa'
    assert cipher('vamos estudar segurança', 4) != 'YDPRV HVWXGDU VHJXUDQFD'
