plain_cipher_map = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 
    'z': 'a'
}

def encode(plain_text):
    encoded_text = ''.join(plain_cipher_map[text] if text.isalpha() else text for text in plain_text.lower().strip() if text.isalnum())
    return ' '.join(encoded_text[i:i+5] for i in range(0, len(encoded_text), 5))

def decode(ciphered_text):
    decoded_text = ''.join(plain_cipher_map[text] if text.isalpha() else text for text in ciphered_text.lower().strip() if text.isalnum())
    return ''.join(decoded_text)
