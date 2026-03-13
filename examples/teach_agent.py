from src.itl import ITLAgent

def teach_agent_conditional_logic():
    print("--- Interactive Task Learning (ITL) Session ---")
    agent = ITLAgent()

    # Scenario: Teaching the agent a safety rule
    # Instructor: "If red light is on, then stop moving."
    instruction = "If red light is on then stop moving"
    
    print(f"Instructor says: '{instruction}'")
    agent.learn_task(instruction)

    # Scenario: Teaching a manipulation task
    # Instructor: "Pick up the blue box"
    instruction_2 = "Pick up the blue box"
    print(f"\nInstructor says: '{instruction_2}'")
    agent.learn_task(instruction_2)

if __name__ == "__main__":
    teach_agent_conditional_logic()
