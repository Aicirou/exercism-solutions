def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    if key in [0,26]: return text
    for i, c in enumerate(text):
        if not str(c).isalpha():
            cipher += c
        else:
            shift = alphabet.find(str(c).lower()) + key
            if c.isupper():
                cipher += alphabet[shift % 26].upper()
            else:
                cipher += alphabet[shift % 26]
    return cipher