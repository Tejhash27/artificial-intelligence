def solve_8_queens():
    # Board size
    n = 8
    solutions = []
    
    # Track attacks on columns, positive diagonals (row + col), and negative diagonals (row - col)
    cols = set()
    pos_diag = set()  # (row + col)
    neg_diag = set()  # (row - col)
    
    # current_state stores the column index for each row
    current_state = [-1] * n

    def backtrack(row):
        # Base case: All 8 queens successfully placed
        if row == n:
            solutions.append(list(current_state))
            return

        for col in range(n):
            # Check if this position is under attack
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # Place the queen and mark constraints
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            current_state[row] = col

            # Move to the next row
            backtrack(row + 1)

            # Backtrack: Remove the queen and clear constraints
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    # Start the recursive search from row 0
    backtrack(0)
    return solutions

def print_board(solution):
    """Helper function to print the board visually."""
    n = len(solution)
    for col_index in solution:
        row_str = [" . "] * n
        row_str[col_index] = " Q "
        print("".join(row_str))
    print("\n" + "=" * 25 + "\n")

if __name__ == "__main__":
    all_solutions = solve_8_queens()
    
    print(f"Total solutions found: {len(all_solutions)}\n")
    
    # Print the first 3 solutions as an example
    print("Displaying the first 3 solutions:")
    for idx, sol in enumerate(all_solutions[:3], 1):
        print(f"Solution #{idx}:")
        print_board(sol)
