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
    # Predefined combinations of winning indexes
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    """Checks if the board is completely full, resulting in a draw."""
    # If there are no numerical placeholders left, the board is full
    return all(space in ['X', 'O'] for space in board)


def play_game():
    """Main function to handle the game loop and mechanics."""
    # Initialize the board with positions 1 through 9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    
    while not game_over:
        print_board(board)
        
        # Keep asking for input until a valid selection is made
        while True:
            try:
                move = int(input(f"Player {current_player}, choose a position (1-9): "))
                
                # Check if the number is within bounds
                if move < 1 or move > 9:
                    print("Invalid input. Please choose a number between 1 and 9.")
                    continue
                    
                # Check if the chosen position is already occupied
                if board[move - 1] in ['X', 'O']:
                    print("That position is already taken. Try again.")
                    continue
                
                # Valid move found, exit input validation loop
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Place the player's symbol on the board
        board[move - 1] = current_player

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        # Check for a draw
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch player turn
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
