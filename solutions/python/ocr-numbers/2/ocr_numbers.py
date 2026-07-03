def convert(lines):
    # Ensure the number of lines is a multiple of 4
    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Ensure the number of columns is a multiple of 3
    if any(len(line) % 3 != 0 for line in lines):
        raise ValueError("Number of input columns is not a multiple of three")

    # Define the binary font for digits 0-9
    font = {
        " _ | ||_|": "0",
        "     |  |": "1",
        " _  _||_ ": "2",
        " _  _| _|": "3",
        "   |_|  |": "4",
        " _ |_  _|": "5",
        " _ |_ |_|": "6",
        " _   |  |": "7",
        " _ |_||_|": "8",
        " _ |_| _|": "9"
    }

    result = []

    # Process each line group of 4 lines
    for i in range(0, len(lines), 4):
        line_result = []
        num_digits = len(lines[i]) // 3

        # Process each digit in the line
        for j in range(num_digits):
            # Extract the 3x3 character for each digit
            digit_str = (lines[i][j*3:j*3+3] +
                         lines[i+1][j*3:j*3+3] +
                         lines[i+2][j*3:j*3+3])

            # Append the corresponding digit or '?' if not found
            line_result.append(font.get(digit_str, "?"))

        # Join the digits into a string for this line
        result.append("".join(line_result))

    # Join the results for each line with commas
    return ",".join(result)
