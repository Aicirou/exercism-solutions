"""Module for solving the Bottle Song exercise."""

def recite(start, take=1):
    """
    Generates the lyrics for the bottle song.

    :param start: int, the starting number of bottles.
    :param take: int, the number of verses to recite.
    :return: list of str, the lyrics of the song.
    """
    # Mapping numbers to words
    number_words = {
        10: "Ten", 9: "Nine", 8: "Eight", 7: "Seven", 6: "Six",
        5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 0: "no"
    }

    def get_verse(bottle_count: int) -> list:
        """
        Constructs a single verse for the given bottle count.

        :param bottle_count: int, the current number of bottles.
        :return: list of str, the four lines of the verse.
        """
        # Determine pluralization
        bottle_curr = "bottle" if bottle_count == 1 else "bottles"
        bottle_next = "bottle" if (bottle_count - 1) == 1 else "bottles"
        
        # Current count word, handling capitalization
        current_word = number_words[bottle_count]
        next_word = number_words[bottle_count - 1].lower()
        
        return [
            f"{current_word} green {bottle_curr} hanging on the wall,",
            f"{current_word} green {bottle_curr} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_word} green {bottle_next} hanging on the wall."
        ]

    lyrics = []
    # Loop from the starting number down to the end of the 'take' count
    for verse_num in range(start, start - take, -1):
        # Use .extend() to add the 4 strings into the main list individually
        lyrics.extend(get_verse(verse_num))
        
        # Add an empty string if it's not the last verse
        if verse_num > (start - take + 1):
            lyrics.append("")
            
    return lyrics