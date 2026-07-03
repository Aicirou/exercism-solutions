def label(colors):
    COLORS_MAP = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    
    # Calculate main value from first two colors
    main_value = COLORS_MAP[colors[0]] * 10 + COLORS_MAP[colors[1]]
    
    # Add zeros based on third color
    zeros = COLORS_MAP[colors[2]]
    value = main_value * (10 ** zeros)
    
    # Determine appropriate unit
    if value >= 10 ** 9:
        return f"{value // 10 ** 9} gigaohms"
    elif value >= 10 ** 6:
        return f"{value // 10 ** 6} megaohms"
    elif value >= 10 ** 3:
        return f"{value // 10 ** 3} kiloohms"
    else:
        return f"{value} ohms"