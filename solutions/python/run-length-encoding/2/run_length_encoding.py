def decode(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            result.append(s[j] * count)
            i = j + 1
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)


def encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append((str(count) if count > 1 else '') + s[i-1])
            count = 1
    result.append((str(count) if count > 1 else '') + s[-1])
    return ''.join(result)