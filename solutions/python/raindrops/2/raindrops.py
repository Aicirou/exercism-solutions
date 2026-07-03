"""
Exercism solution for "raindrops"
"""
DROPS = ("i", 3), ("a", 5), ("o", 7)


def convert(num: int) -> str:
    """
    Convert a number to an appropriate raindrops string.
    """
    return "".join(f"Pl{i}ng" for i, v in DROPS if not num % v) or str(num)
        
    
    