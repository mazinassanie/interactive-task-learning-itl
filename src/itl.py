class HTNTask:
    def __init__(self, name, is_primitive=True):
        self.name = name
        self.is_primitive = is_primitive
        self.methods = [] # For non-primitive tasks

class ITLAgent:
    """
    Advanced ITL Agent using Hierarchical Task Networks (HTN) for planning.
    """
    def __init__(self):
        self.primitive_operators = {
            "move_to": lambda target: f"Executing: Move to {target}",
            "grasp": lambda target: f"Executing: Grasp {target}",
            "release": lambda target: f"Executing: Release {target}"
        }
        self.task_network = {
            "fetch": [
                {"condition": "is_at_table", "subtasks": ["move_to", "grasp", "move_to", "release"]}
            ]
        }

    def solve_hierarchical(self, complex_task, target):
        print(f"[HTN Planner] Solving task: {complex_task} for {target}")
        if complex_task in self.task_network:
            plan = self.task_network[complex_task][0]["subtasks"]
            execution_plan = []
            for step in plan:
                if step in self.primitive_operators:
                    execution_plan.append(self.primitive_operators[step](target))
            return execution_plan
        return ["Error: No decomposition found."]

def run_htn_demo():
    agent = ITLAgent()
    plan = agent.solve_hierarchical("fetch", "red_ball")
    for action in plan:
        print(f"  -> {action}")

if __name__ == "__main__":
    run_htn_demo()
