def convert(lines):
    # Validate input lines
    if not lines:
        raise ValueError("Input lines are empty")

    num_lines = len(lines)
    if num_lines % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    line_lengths = [len(line) for line in lines]
    if any(length != line_lengths[0] for length in line_lengths):
        raise ValueError("All lines must have the same length")

    num_cols = line_lengths[0]
    if num_cols % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    # Define the mapping for digits 0-9
    digit_map = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }

    result = []
    # Process each set of 4 lines
    for i in range(0, num_lines, 4):
        current_lines = lines[i:i+4]
        num_digits = num_cols // 3
        digits = []
        for j in range(num_digits):
            digit_chars = [line[j*3:(j+1)*3] for line in current_lines]
            digit_str = ''.join(digit_chars)
            digits.append(digit_map.get(digit_str, '?'))
        result.append(''.join(digits))
    return ','.join(result)
