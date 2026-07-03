def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question: 
        raise ValueError("syntax error")
    if question.isdigit(): 
        return int(question)

    OPS = {
        "plus": "+",
        "minus": "-",
        "multiplied by": "*",
        "divided by": "/",
    }

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op: 
        raise ValueError("unknown operation")

    try:
        question = question.split(" ")
        question.insert(0,'(')
        question.insert(4, ')')
        if question[1] in OPS.values():
            raise ValueError('Syntax error')
        return eval(''.join(question))
    except Exception as e:
        raise ValueError("syntax error") from e