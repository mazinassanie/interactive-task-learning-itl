# Interactive Task Learning (ITL) Framework V2 🗣️🎓

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT)

A robust framework enabling AI agents to learn new procedural tasks from natural language instructions. This version introduces **conditional logic parsing** and **dynamic procedural memory encoding**, allowing agents to learn rules, not just simple commands.

## 🚀 Key Upgrades
- **Conditional Parsing**: Supports complex "If-Then" rule structures, enabling the learning of constraints and reactive behaviors.
- **Procedural Memory (PM)**: A dedicated memory store for learned operators and rules.
- **World State Validation**: Simulates environment checks to ensure learned tasks are grounded in reality.

## 📂 Architecture
- `src/itl.py`: Contains `InstructionParser`, `ProceduralMemory`, and `WorldState`.
- `examples/teach_agent.py`: A script demonstrating how to teach an agent safety rules and manipulation tasks.

## 🛠️ Usage
```bash
python -m examples.teach_agent
```

## 📚 Research Context
Based on "Interactive Task Learning" (Laird et al.), focusing on One-Shot Learning of hierarchical task networks through natural interaction.
