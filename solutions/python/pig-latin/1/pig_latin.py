def translate(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return ' '.join(translated_words)

def translate_word(word):
    vowels = 'aeiou'
    
    # Rule 1: words beginning with vowel, "xr", or "yt"
    if word[0] in vowels or word.startswith(('xr', 'yt')):
        return word + 'ay'
    
    # Rule 3: words starting with consonants followed by "qu"
    qu_index = word.find('qu')
    if qu_index != -1 and all(c not in vowels for c in word[:qu_index]):
        return word[qu_index+2:] + word[:qu_index+2] + 'ay'
    
    # Rule 4: words starting with consonants followed by "y"
    y_index = word.find('y')
    if y_index != -1 and y_index != 0 and all(c not in vowels for c in word[:y_index]):
        return word[y_index:] + word[:y_index] + 'ay'
    
    # Rule 2: words beginning with consonants
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + 'ay'
    
    # If no vowels found, return the original word + 'ay'
    return word + 'ay'