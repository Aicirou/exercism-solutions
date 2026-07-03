def is_valid(isbn):
    # Remove hyphens and convert to lowercase
    isbn = list(isbn.replace("-", "").lower())
    
    # Check if the length is correct
    if len(isbn) != 10:
        return False

    # Check the last character
    if isbn[-1] == 'x':
        isbn[-1] = '10'

    # Check the non digit characters
    if any(not char.isdigit() for char in isbn):
        return False
 
    # Calculate the sum
    total = sum(int(char) * (10-position) for position, char in enumerate(isbn))
    
    # Validate the ISBN
    return total % 11 == 0