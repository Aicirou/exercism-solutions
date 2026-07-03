def factors(n):
    """
    Finds the prime factors of a given number.

    Args:
        n (int): The number to find prime factors for.

    Returns:
        list: A list of prime factors.
    """
    prime_factors = []
    current_divisor = 2
    while n > 1:
        if n % current_divisor == 0:
            prime_factors.append(current_divisor)
            n = n // current_divisor
        else:
            current_divisor += 1
    return prime_factors
