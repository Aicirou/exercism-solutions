from string import ascii_uppercase

def rows(letter):
    alphabets = list(ascii_uppercase)
    
    if letter.upper() == 'A':
        return ["A"]
    
    alpha_index = alphabets.index(letter.upper())
    alpha_list = alphabets[:alpha_index + 1]
    
    diamond = []

    for i in range(alpha_index + 1):
        current_char = alpha_list[i]
        spaces_outside = alpha_index - i
        if i == 0:
            line = ' ' * spaces_outside + current_char + ' ' * spaces_outside
        else:
            spaces_inside = 2 * i - 1
            line = ' ' * spaces_outside + current_char + ' ' * spaces_inside + current_char + ' ' * spaces_outside
        print(line)
        diamond.append(line)
    
    for i in range(alpha_index - 1, -1, -1):
        diamond.append(diamond[i])
    
    return diamond