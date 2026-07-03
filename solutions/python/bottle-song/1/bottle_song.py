def recite(start, take=1):
    # Mapping numbers to words
    numbers = {
        10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six",
        5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 0: "no"
    }
    
    def get_verse(n):
        # Determine pluralization
        bottle_curr = "bottle" if n == 1 else "bottles"
        bottle_next = "bottle" if (n - 1) == 1 else "bottles"

        # Current count word, handling capitalization
        current_word = numbers[n]
        next_word = numbers[n - 1].lower()

        return [
            f"{current_word} green {bottle_curr} hanging on the wall,",
            f"{current_word} green {bottle_curr} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_word} green {bottle_next} hanging on the wall."
        ]
        

    lyrics = []
    # Loop from the starting number down to the end of the 'take' count
    for i in range(start, start - take, -1):
        # Use .extend() to add the 4 strings into the main list individually
        lyrics.extend(get_verse(i))
        
        # Add an empty string if it's not the last verse
        if i > (start - take + 1):
            lyrics.append("")
            
    return lyrics
        
