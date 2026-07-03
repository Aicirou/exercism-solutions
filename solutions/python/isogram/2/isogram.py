def is_isogram(string):
    """Return True if <string> is isogram."""
    string_low_alpha = [c for c in string.lower() if c.isalpha()]

    return len(string_low_alpha) == len(set(string_low_alpha))