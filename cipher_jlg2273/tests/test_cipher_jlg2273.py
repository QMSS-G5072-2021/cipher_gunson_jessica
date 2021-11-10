from cipher_jlg2273 import cipher_jlg2273

def test_cipher_with_nonalphabet():
    text = 'apple!'
    shift = 1
    expected = 'bqqmf!'
    actual = cipher(text, shift)
    assert actual == expected
