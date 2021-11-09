def cipher(text, shift, encrypt=True):
    """A cipher which encrypts and decrypts strings of text.

        This package allows the user to input a string of text, a numerical
        shift in integer format to indicate the direction and number of steps
        in which the cipher should move along the alphabet, and the option to
        encrypt or decrypt the text. The cipher defaults to encrypt=True.
        Negative shifts values will direct the cipher to move backwards through
        the alphabet. The cipher will output a string of text, either encrypted
        or decrypted. Non-alphabetical values will be ignored.

        Parameters
        ----------
        text: str
           the string of text to encrypt or decrypt
        shift: int
            the number of steps to be taken by the cipher along the alphabet
        encrypt: bool
            True = encrypt; False = decrypt; defaults to True.


        Returns
        ------
        str
            the text, encrypted or decrypted.



        Typical Usage Example
        ---------------------
        >>> from cipher_jlg2273 import cipher_jlg2273
        >>> cipher(text = "apple", shift = 1, encrypt = True)
        bqqmf
        >>> cipher(text = "bqqmf", shift = 1, encrypy = False)
        apple
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

