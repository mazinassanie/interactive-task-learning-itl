class InstructionParser:
    """
    Parses natural language instructions into agent-executable goal structures.
    """
    def __init__(self, vocabulary):
        self.vocab = vocabulary

    def parse(self, instruction):
        words = instruction.lower().split()
        if "pick" in words and "up" in words:
            item = self._extract_target(words, ["pick", "up"])
            return {"goal": "achieve_possession", "object": item}
        return {"goal": "unknown"}

    def _extract_target(self, words, keywords):
        target = [w for w in words if w not in keywords and w in self.vocab]
        return target[0] if target else "unknown"

class ITLAgent:
    def __init__(self):
        self.parser = InstructionParser(["ball", "block", "key"])
        self.task_memory = {}

    def process_instruction(self, instruction):
        goal = self.parser.parse(instruction)
        print(f"DEBUG: ITL Agent decoded goal: {goal}")
        # Map goal to internal procedure
        self.task_memory[goal['object']] = "execute_grasp"
        return goal
