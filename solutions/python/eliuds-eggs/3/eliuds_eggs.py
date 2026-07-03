def decimal_to_binary(n):
    binary_number = ""
    while n > 0:
        binary_number = str(n % 2) + binary_number
        n = n // 2
    return binary_number


def egg_count(display_value):
    binary_number = decimal_to_binary(display_value)
    return str(binary_number).count('1')