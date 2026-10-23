import random
import time

class VacuumEnvironment:
    def __init__(self):
        # Randomly initialize rooms as Clean (0) or Dirty (1)
        self.location_status = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }
        # Randomly place the vacuum agent in Room A or Room B
        self.agent_location = random.choice(['A', 'B'])
        self.total_score = 0  # Tracks performance (points given for cleaning)

    def display_status(self):
        """Prints the current state of the environment."""
        print(f"📍 Vacuum Location: {self.agent_location}")
        print(f"🧹 Room Status     : Room A is [{self.location_status['A']}], Room B is [{self.location_status['B']}]")
        print(f"📊 Performance Score: {self.total_score}")
        print("-" * 50)


class ReflexVacuumAgent:
    def __init__(self):
        pass

    def act(self, environment):
        current_loc = environment.agent_location
        current_status = environment.location_status[current_loc]

        print(f"🤖 Agent senses that Room {current_loc} is {current_status}.")

        if current_status == 'Dirty':
            # Action: Clean the room
            environment.location_status[current_loc] = 'Clean'
            environment.total_score += 10  # Reward points for cleaning
            print(f"⚡ Action: SUCKED dirt from Room {current_loc}.")
        else:
            # Action: Move to the other room if current is clean
            if current_loc == 'A':
                environment.agent_location = 'B'
                print("⚡ Action: Room A is clean. Moving RIGHT to Room B.")
            elif current_loc == 'B':
                environment.agent_location = 'A'
                print("⚡ Action: Room B is clean. Moving LEFT to Room A.")


def run_simulation(steps=4):
    print("==================================================")
    print("       VACUUM CLEANER AGENT SIMULATION            ")
    print("==================================================\n")
    
    # Initialize environment and agent
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent()
    
    # Run the simulation for a designated number of steps
    for step in range(1, steps + 1):
        print(f"🎬 --- STEP {step} ---")
        env.display_status()
        agent.act(env)
        time.sleep(1) # Visual delay for tracking steps
        print("\n")
        
    print("==================================================")
    print("               SIMULATION ENDED                   ")
    print("==================================================")
    print(f"🏆 Final Cleanliness Status: Room A: {env.location_status['A']} | Room B: {env.location_status['B']}")
    print(f"📈 Total Performance Score : {env.total_score} points")

if __name__ == "__main__":
    # Run simulation for 4 cycles to ensure both rooms are handled
    run_simulation(steps=4)
