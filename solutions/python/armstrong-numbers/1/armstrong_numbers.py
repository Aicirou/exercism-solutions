def is_armstrong_number(number):
    #Convert to string
    number_str = str(number)

    #Define sum
    sum = 0

    #Extract and convert digits
    for digit_str in number_str:
        sum += int(digit_str) ** len(number_str)

    #Result
    return sum == number