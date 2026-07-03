def twelve_days_of_christmas():
    # List of gifts for each day (index 0 corresponds to day 1)
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    # List of ordinal numbers (index 0 corresponds to day 1)
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    # Initialize the song lyrics as a list of verses
    song = []

    # Build each verse
    for day in range(12):
        # Start the verse with the introductory line
        verse = f"On the {ordinals[day]} day of Christmas my true love gave to me: "

        # Add the gifts for the current day in reverse order
        for i in range(day, -1, -1):
            if i == 0 and day > 0:  # Add "and" before the last gift for days > 1
                verse += "and "
            verse += gifts[i]
            if i > 0:  # Add a comma between gifts
                verse += ", "

        # Add the verse to the song
        song.append(verse)

    return song

def recite(start_verse, end_verse):
    # Get the full song
    song = twelve_days_of_christmas()
    # Return the requested verses (adjusting for 0-based indexing)
    return song[start_verse - 1:end_verse]