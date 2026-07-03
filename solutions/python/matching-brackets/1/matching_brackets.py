def is_paired(input_string):
    """Check if brackets in a string are balanced.

    :param input_string: str - the input string.
    :return: bool - True if brackets are balanced, False otherwise.
    """
    # Create an empty list to store opening brackets
    stack = []

    # Map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Go through each character in the input string
    for char in input_string:
        # If the character is an opening bracket, add it to the stack
        if char in bracket_map.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_map.keys():
            # If the stack is empty or the top of the stack doesn't match the closing bracket, return False
            if not stack or bracket_map[char] != stack.pop():
                return False

    # If the stack is empty after going through all characters, return True (brackets are balanced)
    # Otherwise, return False (brackets are not balanced)
    return not stack