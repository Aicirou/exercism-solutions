def annotate(garden):
    if not garden:
        return []
        
    rows = len(garden)
    cols = len(garden[0])

    # validate the board
    for row in garden:
        if not len(row) == cols:
            raise ValueError('The board is invalid with current input.')
        for char in row:
            if char not in (' ','*'):
                raise ValueError('The board is invalid with current input.')

    annotated_garden = []

    # Iterate through the grid
    for r in range(rows):
        new_row = ''
        for c in range(cols):
            if garden[r][c] == '*':
                new_row += '*'
            else:
                flower_count = 0
                # Check 8 directions
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        new_r, new_c = r + dr, c + dc

                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            if garden[new_r][new_c] == '*':
                                flower_count += 1

                # Append cound or space
                new_row += str(flower_count) if flower_count > 0 else ' '
                
        annotated_garden.append(new_row)

    return annotated_garden
        