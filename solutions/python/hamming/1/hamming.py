def distance(strand_a, strand_b):
    # When the sequences being passed are not the same length.
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count=0
    for i, a_value in enumerate(strand_a):
        if not a_value == strand_b[i]:
            count+=1
    return count
