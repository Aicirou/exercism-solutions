def annotate(minefield):
    # Input validation
    if not minefield:
        return minefield
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    if not all(c in ' *' for row in minefield for c in row):
        raise ValueError("The board is invalid with current input.")
    
    # Get dimensions of the minefield
    rows, cols = len(minefield), len(minefield[0])
    
    # Define all possible directions to check around a cell
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Create a new 2D list to store the result
    result = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Iterate through each cell in the minefield
    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                # If it's a mine, mark it as such in the result
                result[i][j] = '*'
            else:
                # Count adjacent mines
                count = 0
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < rows and 0 <= nj < cols and minefield[ni][nj] == '*':
                        count += 1
                # Set the count in the result (or space if count is 0)
                result[i][j] = str(count) if count else ' '
    
    # Convert the 2D list of characters to a list of strings
    return [''.join(row) for row in result]