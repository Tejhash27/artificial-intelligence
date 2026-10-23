from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    # Queue stores tuple of: (current_jug1, current_jug2, list_of_steps_taken)
    queue = deque([(0, 0, [])])
    # Track visited states to prevent infinite loops
    visited = set()
    visited.add((0, 0))

    while queue:
        j1, j2, steps = queue.popleft()

        # Check if either jug has reached the target quantity
        if j1 == target or j2 == target:
            return steps + [(j1, j2)]

        # Generate all 6 possible rules/actions from the current state
        possible_moves = [
            (jug1_cap, j2, "Fill Jug 1"),                       # 1. Fill Jug 1
            (j1, jug2_cap, "Fill Jug 2"),                       # 2. Fill Jug 2
            (0, j2, "Empty Jug 1"),                             # 3. Empty Jug 1
            (j1, 0, "Empty Jug 2"),                             # 4. Empty Jug 2
            # 5. Pour Jug 1 -> Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2), "Pour Jug 1 into Jug 2"),
            # 6. Pour Jug 2 -> Jug 1
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1), "Pour Jug 2 into Jug 1")
        ]

        for next_j1, next_j2, action in possible_moves:
            if (next_j1, next_j2) not in visited:
                visited.add((next_j1, next_j2))
                # Build the history tracking for the steps path
                new_steps = steps + [(j1, j2, action)]
                queue.append((next_j1, next_j2, new_steps))

    return None  # Return None if the target is impossible to reach

def print_solution(jug1_cap, jug2_cap, target):
    print(f"Target: Measure exactly {target} liters using a {jug1_cap}L and a {jug2_cap}L jug.\n")
    
    # Check mathematical impossibility using Greatest Common Divisor (GCD)
    import math
    if target > max(jug1_cap, jug2_cap) or target % math.gcd(jug1_cap, jug2_cap) != 0:
        print("❌ Solution is mathematically impossible!")
        return

    path = solve_water_jug(jug1_cap, jug2_cap, target)
    
    if path:
        print("✅ Success! Optimal steps found:")
        print(f"{'Jug 1':<8} | {'Jug 2':<8} | Action")
        print("-" * 45)
        
        # Print transitions
        for step in path[:-1]:
            j1, j2, action = step
            print(f"{j1:<8} | {j2:<8} | {action}")
        
        # Print final state reached
        final_j1, final_j2 = path[-1]
        print(f"{final_j1:<8} | {final_j2:<8} | Goal Reached!")
    else:
        print("❌ No solution could be found.")

if __name__ == "__main__":
    # Example constraints: Jug 1 = 4L, Jug 2 = 3L, Target = 2L
    print_solution(jug1_cap=4, jug2_cap=3, target=2)
