"""
This module converts Arabic integers to traditional 
Roman numerals.
"""

def roman(number: int) -> str:
    """
    Convert an integer between 1 and 3999 (inclusive) to a Roman numeral.
    """
    
    # Mapping of values to symbols, including subtractive combinations,
    # ordered from largest to smallest.
    mappings: list[tuple[int, str]] = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result: str = ''
    
    for value, symbol in mappings:
        while number >= value:
            result += symbol
            number -= value
            
    return result