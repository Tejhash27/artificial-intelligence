from collections import deque

class State:
    def __init__(self, m_left, c_left, boat_side, path=None):
        # State tracking: items on the LEFT bank
        self.m_left = m_left
        self.c_left = c_left
        self.boat_side = boat_side  # 0 for Left, 1 for Right
        
        # Items on the RIGHT bank are derived automatically
        self.m_right = 3 - m_left
        self.c_right = 3 - c_left
        
        # History tracking for printing the path
        self.path = path if path is not None else []

    def is_valid(self):
        """Checks if the state obeys the safety rules."""
        # Boundaries check
        if not (0 <= self.m_left <= 3 and 0 <= self.c_left <= 3):
            return False
            
        # Left bank constraint: Missionaries cannot be outnumbered unless there are 0
        if self.m_left > 0 and self.m_left < self.c_left:
            return False
            
        # Right bank constraint: Missionaries cannot be outnumbered unless there are 0
        if self.m_right > 0 and self.m_right < self.c_right:
            return False
            
        return True

    def is_goal(self):
        """True if everyone safely reached the right side."""
        return self.m_left == 0 and self.c_left == 0

    def to_tuple(self):
        """Unique identifier for visited tracking."""
        return (self.m_left, self.c_left, self.boat_side)


def solve_missionaries_cannibals():
    # Initial state: 3M, 3C, Boat on Left (0)
    initial_state = State(3, 3, 0)
    
    if initial_state.is_goal():
        return initial_state.path
        
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state.to_tuple())

    # All possible moves for the boat: (Missionaries, Cannibals)
    # Boat capacity is max 2, min 1
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return current.path + [current]

        for m_move, c_move in moves:
            # If boat is on Left bank (0), we SUBTRACT people to move them Right
            if current.boat_side == 0:
                next_m = current.m_left - m_move
                next_c = current.c_left - c_move
                next_boat = 1
                action_str = f"Move {m_move}M and {c_move}C to Right Bank"
            # If boat is on Right bank (1), we ADD people back to the Left bank
            else:
                next_m = current.m_left + m_move
                next_c = current.c_left + c_move
                next_boat = 0
                action_str = f"Bring {m_move}M and {c_move}C back to Left Bank"

            # Create next state evaluation step
            next_state = State(next_m, next_c, next_boat, current.path + [(current, action_str)])

            if next_state.is_valid() and next_state.to_tuple() not in visited:
                visited.add(next_state.to_tuple())
                queue.append(next_state)

    return None


def print_solution(path):
    if not path:
        print("❌ No solution found!")
        return

    print("✅ Optimal Solution Found! Step-by-Step Moves:\n")
    print(f"{'Left Bank':<12} | {'Boat':<6} | {'Right Bank':<12} | Action")
    print("-" * 65)

    for i, step in enumerate(path):
        if isinstance(step, tuple):
            state, action = step
        else:
            state, action = step, "Goal Achieved!"

        # Create localized text representation
        boat_pos = "Left" if state.boat_side == 0 else "Right"
        left_str = f"{state.m_left}M, {state.c_left}C"
        right_str = f"{state.m_right}M, {state.c_right}C"
        
        print(f"{left_str:<12} | {boat_pos:<6} | {right_str:<12} | {action}")


if __name__ == "__main__":
    solution_path = solve_missionaries_cannibals()
    print_solution(solution_path)
