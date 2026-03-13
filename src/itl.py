class WorldState:
    """
    Simulated environment state to validate if tasks are achievable.
    """
    def __init__(self):
        self.objects = {"red_block": "table", "blue_box": "shelf"}
        self.agent_hand = None

    def check_object(self, obj):
        return obj in self.objects

class ProceduralMemory:
    """
    Stores learned task structures (Operator representations).
    """
    def __init__(self):
        self.learned_tasks = {}

    def add_task(self, name, procedure):
        print(f"[PM] Learning new task: {name} -> {procedure}")
        self.learned_tasks[name] = procedure

class InstructionParser:
    def __init__(self):
        self.core_vocabulary = ["pick", "place", "move", "if", "then"]

    def parse_conditional(self, instruction):
        """
        Parses complex conditional instructions: 'If [condition], then [action]'
        """
        instruction = instruction.lower()
        if "if" in instruction and "then" in instruction:
            parts = instruction.split("then")
            condition_part = parts[0].replace("if", "").strip()
            action_part = parts[1].strip()
            return {
                "type": "conditional",
                "condition": self._extract_predicate(condition_part),
                "action": self._extract_action(action_part)
            }
        else:
            return {"type": "simple", "action": self._extract_action(instruction)}

    def _extract_action(self, text):
        return f"op_{text.replace(' ', '_')}"

    def _extract_predicate(self, text):
        return f"pred_{text.replace(' ', '_')}"

class ITLAgent:
    def __init__(self):
        self.world = WorldState()
        self.pm = ProceduralMemory()
        self.parser = InstructionParser()

    def learn_task(self, instruction):
        parsed = self.parser.parse_conditional(instruction)
        print(f"[Agent] Parsed Instruction: {parsed}")
        
        if parsed['type'] == 'conditional':
            rule_name = f"rule_{parsed['condition']}_to_{parsed['action']}"
            self.pm.add_task(rule_name, parsed)
        else:
            self.pm.add_task("simple_task", parsed)
