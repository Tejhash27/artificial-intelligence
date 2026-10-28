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
    # The 8 possible lines to win Tic-Tac-Toe
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False


def check_draw(board):
    """Checks if the board is full."""
    return all(space in ['X', 'O'] for space in board)


def get_empty_cells(board):
    """Returns a list of available indices on the board."""
    return [i for i, space in enumerate(board) if space not in ['X', 'O']]


def minimax(board, depth, is_maximizing):
    """
    Core Minimax algorithm.
    Maximizer: AI ('O') -> Wants highest score (+10)
    Minimizer: Human ('X') -> Wants lowest score (-10)
    """
    # Base cases: evaluate terminal states
    if check_win(board, 'O'):
        return 10 - depth  # Prefer quicker wins
    if check_win(board, 'X'):
        return depth - 10  # Prefer stalling losses
    if check_draw(board):
        return 0

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells:
            board[cell] = 'O'
            score = minimax(board, depth + 1, False)
            board[cell] = str(cell + 1)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells:
            board[cell] = 'X'
            score = minimax(board, depth + 1, True)
            board[cell] = str(cell + 1)
            best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    """Iterates through empty cells to pick the AI move with the highest Minimax score."""
    best_score = -math.inf
    best_move = -1
    
    for cell in get_empty_cells(board):
        board[cell] = 'O'
        move_score = minimax(board, 0, False)
        board[cell] = str(cell + 1)
        
        if move_score > best_score:
            best_score = move_score
            best_move = cell
            
    return best_move


def play_game():
    """Main game loop managing turns."""
    board = [str(i) for i in range(1, 10)]
    print("Welcome to Tic-Tac-Toe vs Unbeatable AI!")
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
            print("Congratulations! You beat the unbeatable AI! (This shouldn't happen!)")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
            
        # --- AI Turn ('O') ---
        print("AI is thinking...")
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
