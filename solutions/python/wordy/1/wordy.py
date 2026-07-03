def answer(question):
    """Evaluate a simple math word problem."""
    
    # Remove leading/trailing whitespace and question mark
    question = question.strip().rstrip('?')
    
    # Check if the question starts with "What is"
    if not question.lower().startswith("what is"):
        raise ValueError("unknown operation")
    
    # Extract the expression
    expression = question[7:].strip()
    tokens = expression.split()
    
    # Check for empty expression
    if not tokens:
        raise ValueError("syntax error")
    
    # Initialize result with the first number
    try:
        result = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")
    
    # Process the rest of the tokens
    ops = {
        "plus": "+",
        "minus": "-",
        "multiplied": "*",
        "divided": "/",
    }
    
    i = 1
    while i < len(tokens):
        if tokens[i] in ops:
            operation = ops[tokens[i]]
            if tokens[i] in ["multiplied", "divided"] and tokens[i + 1] == "by":
                i += 1
        elif tokens[i] == 'cubed':
            raise ValueError("unknown operation")
        else:
            raise ValueError("syntax error")
        
        try:
            number = int(tokens[i + 1])
        except (ValueError, IndexError):
            raise ValueError("syntax error")
        
        result = eval(f"{result} {operation} {number}")
        
        i += 2
    
    return result