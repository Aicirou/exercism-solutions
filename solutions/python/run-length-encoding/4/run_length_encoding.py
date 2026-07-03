def decode(input_string):
    decoded = []
    count = ""
    
    for char in input_string:
        if char.isdigit():
            count += char
        else:
            decoded.append(char * (int(count) if count else 1))
            count = ""
    
    return "".join(decoded)


def encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((str(count) if count > 1 else "") + current_char)
            current_char = char
            count = 1
    
    encoded.append((str(count) if count > 1 else "") + current_char)
    
    return "".join(encoded)