# Define a tuple of actions
CMDS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(binary_str):
    """
    Convert a binary string to a list of actions.
    Args:
        binary_str (str): A binary string of length 5.
    Returns:
        list: A list of actions corresponding to the binary string.
    """
    
    # Convert the binary string to an integer using base 2
    number = int(binary_str, 2)
    
    # Initialize an empty list to store the actions
    actions = []
    
    # Iterate through the actions tuple with index and value
    for i, action in enumerate(CMDS):
        # Check if the i-th bit of the binary number is 1
        if number & 1 << i:
            # If the bit is 1, add the corresponding action to the list
            actions.append(action)
    
    # Check if the 5th bit (index 4) of the binary number is 1
    if number & 1 << 4:
        # If the bit is 1, reverse the list of actions
        actions.reverse()
    
    # Return the final list of actions
    return actions