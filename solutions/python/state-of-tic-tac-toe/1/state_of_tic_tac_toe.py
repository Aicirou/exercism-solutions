def gamestate(board):
    # Count the number of 'X's and 'O's on the board
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    
    # 1. Check for invalid turn orders
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    # Helper to determine if a specific player has a winning line
    def check_win(player):
        # Check rows
        if any(row == player * 3 for row in board):
            return True
        # Check columns
        if any(board[0][i] == player and board[1][i] == player and board[2][i] == player for i in range(3)):
            return True
        # Check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

    x_wins = check_win('X')
    o_wins = check_win('O')
    
    # 2. Check for impossible win states (games played after a win)
    if x_wins and o_wins:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    # If X won, O couldn't have taken another turn
    if x_wins and x_count == o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    # If O won, X couldn't have taken another turn
    if o_wins and x_count > o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")
        
    # 3. Determine the final game state
    if x_wins or o_wins:
        return "win"
    if x_count + o_count == 9:
        return "draw"
        
    return "ongoing"