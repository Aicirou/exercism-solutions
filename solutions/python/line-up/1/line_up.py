"""Module to format customer line position messages with correct ordinal suffixes."""

def line_up(name: str, number: int) -> str:
    """Returns a formatted string announcing a customer's position in line."""
    
    # Numbers 11-13 always take "th"
    if 11 <= (number % 100) <= 13:
        suffix = "th"
    else:
        # Determine suffix based on the last digit
        last_digit = number % 10
        match last_digit:
            case 1: suffix = "st"
            case 2: suffix = "nd"
            case 3: suffix = "rd"
            case _: suffix = "th"
            
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"