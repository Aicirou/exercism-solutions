def classify(n):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = [i for i in range(1, n) if n % i == 0]
    aliquot_sum = sum(factors)
    
    if aliquot_sum == n:
        return "perfect"
    elif aliquot_sum > n:
        return "abundant"
    else:
        return "deficient"
    
            
        
