import itertools

def solve_cryptarithmetic(word1, word2, result):
    # Normalize words to uppercase
    w1, w2, res = word1.upper(), word2.upper(), result.upper()
    
    # Extract all unique characters
    unique_chars = list(set(w1 + w2 + res))
    
    # Cryptarithmetic constraints: a single character can only map to digits 0-9
    if len(unique_chars) > 10:
        print("❌ Invalid puzzle: More than 10 unique letters cannot fit into digits 0-9.")
        return None

    # Identify leading letters (they cannot be assigned the digit 0)
    leading_chars = {w1[0], w2[0], res[0]}
    
    # Store found solutions
    solutions = []

    def backtrack(char_index, assigned_digits, current_mapping):
        # Base Case: All letters have been assigned a digit
        if char_index == len(unique_chars):
            # Convert words to numbers based on current mapping
            num1 = int("".join(str(current_mapping[c]) for c in w1))
            num2 = int("".join(str(current_mapping[c]) for c in w2))
            num_res = int("".join(str(current_mapping[c]) for c in res))
            
            # Check if the arithmetic equation holds true
            if num1 + num2 == num_res:
                solutions.append(dict(current_mapping))
            return

        char = unique_chars[char_index]
        
        for digit in range(10):
            # Check constraints: 
            # 1. Digit must not be already used (Each letter gets a unique digit)
            # 2. Leading characters cannot be zero
            if digit in assigned_digits:
                continue
            if digit == 0 and char in leading_chars:
                continue

            # Place choice
            current_mapping[char] = digit
            assigned_digits.add(digit)

            # Move to next character
            backtrack(char_index + 1, assigned_digits, current_mapping)

            # Backtrack (Undo choice)
            del current_mapping[char]
            assigned_digits.remove(digit)

    # Start the backtracking algorithm
    backtrack(0, set(), {})
    return solutions

def display_solutions(w1, w2, res, solutions):
    print(f"Puzzle: {w1} + {w2} = {res}\n")
    
    if not solutions:
        print("❌ No valid solutions found.")
        return

    print(f"✅ Found {len(solutions)} solution(s):\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"--- Solution #{idx} ---")
        # Format map output nicely
        sorted_map = ", ".join(f"'{k}': {v}" for k, v in sorted(sol.items()))
        print(f"Mapping: {{{sorted_map}}}")
        
        # Calculate resulting values
        n1 = "".join(str(sol[c]) for c in w1)
        n2 = "".join(str(sol[c]) for c in w2)
        nr = "".join(str(sol[c]) for c in res)
        
        print(f"  {n1:>6}   ({w1})")
        print(f"+ {n2:>6}   ({w2})")
        print(f"------")
        print(f"  {nr:>6}   ({res})\n")

if __name__ == "__main__":
    # Standard classic cryptarithmetic puzzle
    word1 = "SEND"
    word2 = "MORE"
    result = "MONEY"
    
    all_sol = solve_cryptarithmetic(word1, word2, result)
    display_solutions(word1, word2, result, all_sol)
