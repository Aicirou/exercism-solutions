def reverse(s):
    # Convert the string to a list (since strings are immutable in Python)
    s = list(s)
    
    # Initialize two pointers, one at the start and one at the end
    left = 0
    right = len(s) - 1
    
    # Loop until the pointers meet in the middle
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards the middle
        left += 1
        right -= 1
    
    # Convert the list back to a string and return
    return ''.join(s)