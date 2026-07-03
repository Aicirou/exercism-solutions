def is_pangram(sentence):
    alphabet = 26
    letters = set()
    for letter in sentence.lower():
        if letter.isalpha():  # Check if the character is a letter
            letters.add(letter)
    if len(letters) != alphabet:
        return False
    return True