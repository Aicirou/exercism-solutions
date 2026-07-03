def commands(binary_str):
    # Extract the last 5 digits
    binary_str = binary_str[-5:]
    
    # Map each digit to an action
    actions_map = {
        '1': ['wink', 'double blink', 'close your eyes', 'jump', 'Reverse'],
    }
    
    # Create a list of actions based on the binary string, only including actions for '1' digits
    actions = [actions_map[digit][i] for i, digit in enumerate(reversed(binary_str)) if int(digit) == 1]
    
    # Check if 'Reverse' is in the actions list and reverse the list if so
    if 'Reverse' in actions:
        actions.remove('Reverse')
        actions.reverse()
    
    # Return the final list of actions
    return actions