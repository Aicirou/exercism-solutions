"""
Exercism solution for "raindrops"
"""
DROPS = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}

def convert(num: int) -> str:
    """
    Convert a number to an appropriate raindrops string.
    """
    drop_strings = (_value for _key, _value in DROPS.items() if num % _key == 0)
    return "".join(drop_strings) or str(num)
    