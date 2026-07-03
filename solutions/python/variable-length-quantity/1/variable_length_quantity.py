def encode(numbers):
    encoded_bytes = []
    for number in numbers:
        if number < 0:
            raise ValueError("negative numbers are not supported")
        if number > 0xFFFFFFFF:
            raise ValueError("numbers larger than 32-bit unsigned are not supported")
        
        # Encode the number into VLQ bytes
        bytes_ = []
        while True:
            byte = number & 0x7F  # Extract the least significant 7 bits
            number >>= 7  # Right-shift the number by 7 bits
            if len(bytes_) > 0:
                byte |= 0x80  # Set the continuation bit if not the first byte
            bytes_.append(byte)
            if number == 0:
                break
        
        # Reverse to get big-endian order and add to the result
        bytes_.reverse()
        encoded_bytes.extend(bytes_)
    
    return encoded_bytes  # Return a list of integers


def decode(bytes_):
    if not bytes_:
        return []
    
    numbers = []
    current_number = 0
    for byte in bytes_:
        # Shift and add the 7 bits
        current_number = (current_number << 7) | (byte & 0x7F)
        # If the continuation bit is not set, the number is complete  
        if not (byte & 0x80):  
            numbers.append(current_number)
            current_number = 0  # Reset for the next number
    
    # If there's an incomplete number at the end, raise an error
    if not numbers:
        raise ValueError("incomplete sequence")
    
    return numbers
