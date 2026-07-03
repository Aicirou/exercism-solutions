from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(plain_text):
    plain_text = ''.join(char for char in plain_text if char.isalnum())
    return ' '.join(plain_text.lower().translate(ENCODING)[i:i+5] for i in range(0, len(plain_text), 5))

def decode(ciphered_text):
    return ciphered_text.replace(' ', '').translate(ENCODING)