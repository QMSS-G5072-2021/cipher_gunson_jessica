
import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert isinstance(shift, int), "Shift should be numerical"
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_single_word():
    text = 'apple'
    shift = 1
    expected = 'bqqmf'
    actual = cipher(text, shift)
    assert actual == expected

@pytest.mark.parametrize("text, shift, expected", [
    ('apple', -1, 'Zookd'),
    ('apple', -10, 'QffbU'),
    ('apple', -27, 'zOOKD')
])
def test_cipher_neg_shift_loop(text, shift, expected):
    actual = cipher(text, shift)
    assert actual == expected

def test_cipher_with_nonalphabet():
    text = 'apple!'
    shift = 1
    expected = 'bqqmf!'
    actual = cipher(text, shift)
    assert actual == expected

def test_cipher_with_string_shift():
    with pytest.raises(AssertionError):
        text = 'apple'
        shift = 'one'
        cipher(text, shift)

@pytest.mark.parametrize("text, shift, expected", [
    ('apple', 1, 'bqqmf'),
    ('APPLE', 1, 'BQQMF'),
    ('apple', 2, 'crrng'),
    ('Apples are delicious!', 1, 'Bqqmft bsf efmjdjpvt!'),
    ('ApPlEs', 1, 'BqQmFt')
])
def test_cipher_expanded_set(text, shift, expected):
    actual = cipher(text, shift)
    assert actual == expected


@pytest.mark.parametrize("shift", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_cipher_encryption(shift):
    text = "apple"
    encrypted = cipher(text, shift, encrypt = True)
    return encrypted
    decrypted = cipher(encrypted, shift, encrypt = False)
    return decrypted
    assert text == decrypted
