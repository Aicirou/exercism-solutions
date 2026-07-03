"""
Exercism solution for "raindrops"
"""
DROPS = {
    3: "i",
    5: "a",
    7: "o"
}

def convert(num: int) -> str:
    """
    Convert a number to an appropriate raindrops string.
    """
    drop_strings = [f"Pl{DROPS[v]}ng" for v in DROPS if num % v == 0]
    return "".join(drop_strings) or str(num)
    