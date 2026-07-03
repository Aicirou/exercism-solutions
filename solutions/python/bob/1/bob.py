def response(hey_bob):
    hey_bob = hey_bob.strip()  # Remove leading and trailing whitespace
    if hey_bob.isupper() and hey_bob.endswith('?'): 
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith('?'): return "Sure."
    if hey_bob.isupper(): return "Whoa, chill out!"
    if hey_bob == "": return "Fine. Be that way!"
    return "Whatever."
        
    
        
    
