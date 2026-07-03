def is_valid(isbn):
    # Remove hyphens and convert to lowercase
    isbn = isbn.replace("-", "").lower()
    
    # Check if the length is correct
    if len(isbn) != 10:
        return False
    
    # Calculate the sum
    total = 0
    for i, char in enumerate(isbn[:-1]):
        if not char.isdigit():
            return False
        total += int(char) * (10 - i)
    
    # Check the last character
    if isbn[-1] == 'x':
        total += 10
    elif isbn[-1].isdigit():
        total += int(isbn[-1])
    else:
        return False
    
    # Validate the ISBN
    return total % 11 == 0