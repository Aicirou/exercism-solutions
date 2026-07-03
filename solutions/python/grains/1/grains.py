def square(number):
    if not (1<=number<=64):
        # when the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)
    
def total():
    # Sum of the first 64 positive integers
    return 2 ** 64 - 1
