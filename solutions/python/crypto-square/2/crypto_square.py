import math

def cipher_text(text):
    def normalize_text(text):
        # Remove spaces and punctuation, keep lowercase alphabets and digits
        return ''.join(ch for ch in text.lower() if ch.isalnum())

    def get_smallest_possible_int(length):
        r = 1
        while True:
            c = r
            if r * c >= length:
                return c
            c = r + 1
            if r * c >= length:
                return c
            r += 1

    normalized_text = normalize_text(text)
    length = len(normalized_text)

    if length == 0:
        return ""

    c = get_smallest_possible_int(length)
    r = math.ceil(length / c)

    # Break the text into rows
    rows = [normalized_text[i * c:(i + 1) * c] for i in range(r)]
    
    # Read the text column-wise and pad shorter columns with spaces
    encoded_parts = []
    for col in range(c):
        encoded_part = ''.join(row[col] if col < len(row) else ' ' for row in rows)
        encoded_parts.append(encoded_part)
    
    # Join with spaces and return
    return ' '.join(encoded_parts)

