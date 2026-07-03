def resistor_label(colors):
    # Dictionary mapping color names to their corresponding numerical values
    COLORS_MAP = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    
    # Dictionary mapping color names to their corresponding tolerance values
    TOLERANCE_MAP = {
        'grey': 0.05, 'blue': 0.25, 'violet': 0.1, 'green': 0.5,
        'brown': 1, 'red': 2, 'gold': 5, 'silver': 10
    }

    # Special case for 1-band resistor (0 ohms)
    if len(colors) == 1:
        return '0 ohms'

    # Calculate the main value by concatenating the numerical values of the first colors
    main_value = int(''.join(str(COLORS_MAP[color]) for color in colors[:-2]))
    
    # Calculate the multiplier value based on the third color (or fourth color for 5-band resistors)
    multiplier = 10 ** COLORS_MAP[colors[-2]]
    
    # Get the tolerance value from the last color
    tolerance = TOLERANCE_MAP[colors[-1]]

    # Calculate the final value by multiplying the main value with the multiplier
    value = main_value * multiplier

    # Dictionary mapping exponents to their corresponding unit names
    units = {9: 'gigaohms', 6: 'megaohms', 3: 'kiloohms', 0: 'ohms'}
    
    # Loop through the units to find the appropriate one for the value
    for exp, unit in units.items():
        if value >= 10 ** exp:
            # Return the formatted string with the value, unit, and tolerance
            return f"{value / 10 ** exp:g} {unit} ±{tolerance}%"