"""Module to annotate a flower garden grid."""

def count_adjacent(garden: list[str], row_idx: int, col_idx: int, total_rows: int, total_cols: int) -> int:
    """Count the flowers in the 8 squares surrounding a given cell."""
    count = 0
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
                continue
            
            new_row = row_idx + row_offset
            new_col = col_idx + col_offset
            
            if 0 <= new_row < total_rows and 0 <= new_col < total_cols:
                if garden[new_row][new_col] == '*':
                    count += 1
    return count


def annotate(garden: list[str]) -> list[str]:
    """Annotate the garden with the number of adjacent flowers."""
    if not garden:
        return []

    rows = len(garden)
    cols = len(garden[0])

    for row in garden:
        if len(row) != cols or any(char not in (' ', '*') for char in row):
            raise ValueError("The board is invalid with current input.")

    annotated_garden: list[str] = []
    for row_idx in range(rows):
        new_row = ""
        for col_idx in range(cols):
            if garden[row_idx][col_idx] == '*':
                new_row += '*'
            else:
                flower_count = count_adjacent(garden, row_idx, col_idx, rows, cols)
                new_row += str(flower_count) if flower_count > 0 else ' '
        annotated_garden.append(new_row)

    return annotated_garden