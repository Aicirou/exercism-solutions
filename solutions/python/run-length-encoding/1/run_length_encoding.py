def decode(s):
    result = ""
    i = 0
    while i < len(s):
        if i+2 < len(s) and s[i].isdigit() and s[i+1].isdigit() and not s[i+2].isdigit():
            count = int(s[i:i+2])
            result += s[i+2] * count
            i += 3
        elif i+1 < len(s) and s[i].isdigit() and not s[i+1].isdigit():
            count = int(s[i])
            result += s[i+1] * count
            i += 2
        else:
            result += s[i]
            i += 1
    return result


def encode(s):
    if not s:
        return ""
    result, count, prev = "", 1, s[0]
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            if count > 1:
                result += str(count) + prev
            else:
                result += prev
            count, prev = 1, char
    if count > 1:
        result += str(count) + prev
    else:
        result += prev
    return result
        
