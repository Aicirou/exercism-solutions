EQUAL = 0
SUPERLIST = 1
SUBLIST = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        return 0 if list_one == list_two else 3
    if len(list_one) > len(list_two):
        for k, v in enumerate(list_one):
            if list_two == list_one[k:k+len(list_two)]:
                return 1
    if len(list_one) < len(list_two):
        for k, v in enumerate(list_two):
            if list_one == list_two[k:k+len(list_one)]:
                return 2
    return 3
        
    
        
    