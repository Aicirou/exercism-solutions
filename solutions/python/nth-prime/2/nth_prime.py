def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    counter = 2
    prime_count = 0
    while True:
        for test in range(2, int(counter ** 0.5) + 1):
            if counter % test == 0:
                break
        else:
            prime_count += 1
        if prime_count == number:
            return counter
        counter += 1