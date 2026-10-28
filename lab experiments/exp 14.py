import math

def print_board(board):
    """Prints the current state of the game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    """Checks if the specified player has won the game."""
    # Defined as tuples to avoid markdown formatting glitches
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def check_draw(board):
    """Checks if the board is full."""
    return all(space in ['X', 'O'] for space in board)


def get_empty_cells(board):
    """Returns a list of available indices on the board."""
    return [i for i, space in enumerate(board) if space not in ['X', 'O']]


def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    """
    Minimax algorithm optimized with Alpha-Beta Pruning.
    alpha: Best score the maximizer (AI) can guarantee so far.
    beta: Best score the minimizer (Human) can guarantee so far.
    """
    if check_win(board, 'O'):
        return 10 - depth
    if check_win(board, 'X'):
        return depth - 10
    if check_draw(board):
        return 0

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells:
            board[cell] = 'O'
            score = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
            board[cell] = str(cell + 1)
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells:
            board[cell] = 'X'
            score = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
            board[cell] = str(cell + 1)
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def find_best_move(board):
    """Finds the optimal move for the AI using Alpha-Beta Pruning."""
    best_score = -math.inf
    best_move = -1
    alpha = -math.inf
    beta = math.inf
    
    for cell in get_empty_cells(board):
        board[cell] = 'O'
        move_score = minimax_alpha_beta(board, 0, alpha, beta, False)
        board[cell] = str(cell + 1)
        
        if move_score > best_score:
            best_score = move_score
            best_move = cell
            
    return best_move


def play_game():
    """Main game loop managing turns."""
    board = [str(i) for i in range(1, 10)]
    print("Welcome to Tic-Tac-Toe vs Unbeatable Alpha-Beta AI!")
    print("You are 'X' and the AI is 'O'.")
    
    while True:
        print_board(board)
        
        # --- Human Turn ('X') ---
        while True:
            try:
                move = int(input("Choose a position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid input. Choose a number between 1 and 9.")
                    continue
                if board[move] in ['X', 'O']:
                    print("Position already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        board[move] = 'X'
        
        # Check human status
        if check_win(board, 'X'):
            print_board(board)
            print("Congratulations! You won!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
            
        # --- AI Turn ('O') ---
        print("AI is calculating options...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        
        # Check AI status
        if check_win(board, 'O'):
            print_board(board)
            print("The AI wins! Better luck next time.")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
