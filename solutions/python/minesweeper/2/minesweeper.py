def validate_minefield(minefield):
    if not minefield:
        return minefield
    if len(set(len(row) for row in minefield)) > 1:
        raise ValueError("The board is invalid with current input.")
    if any(c not in ' *' for row in minefield for c in row):
        raise ValueError("The board is invalid with current input.")
    return True

def count_adjacent_mines(minefield, i, j):
    rows, cols = len(minefield), len(minefield[0])
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and minefield[ni][nj] == '*':
                count += 1
    return count

def annotate(minefield):
    if not validate_minefield(minefield):
        return minefield
    
    rows, cols = len(minefield), len(minefield[0])
    result = []
    
    for i in range(rows):
        row = ''
        for j in range(cols):
            if minefield[i][j] == '*':
                row += '*'
            else:
                count = count_adjacent_mines(minefield, i, j)
                row += str(count) if count else ' '
        result.append(row)
    
    return result