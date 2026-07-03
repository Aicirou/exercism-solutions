def is_isogram(string):
    string = string.replace(" ","").replace("-","").lower()
    if len(string) == len(set(string)):
        return True
    return False
