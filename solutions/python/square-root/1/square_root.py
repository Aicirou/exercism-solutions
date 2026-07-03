def square_root(number):
    """Calculate the square root of a number.

    :param number: float - the number to calculate the square root of.
    :return: float - the square root of the number.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    elif number == 0 or number == 1:
        return number
    return int(number ** (1/2))
    
