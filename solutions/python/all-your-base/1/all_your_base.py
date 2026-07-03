def rebase(input_base, digits, output_base):
    # Validate input base
    if  not (input_base >= 2):
        raise ValueError("input base must be >= 2")

    # Validate digits
    if not digits:
        return [0]  # Handle empty input list

    for digit in digits:
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Validate output base
    if not (output_base >= 2):
        raise ValueError("output base must be >= 2")

    # Convert to decimal
    decimal_value = sum(digit * (input_base ** i) for i, digit in enumerate(digits[::-1]))

    # Handle zero case
    if decimal_value == 0:
        return [0]

    # Convert to output base
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    return output_digits[::-1]