# ITL Framework (HTN Advanced) 🗣️🏗️

[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT)

A high-fidelity framework implementing **Hierarchical Task Networks (HTN)** for autonomous task learning and planning. This allows the agent to decompose high-level instructions into executable primitive operators.

## 🚀 Key Upgrades
- **HTN Planner**: Decomposes complex tasks (e.g., "fetch") into a structured sequence of primitive actions.
- **Hierarchical Decomposition**: Supports mapping natural language instructions to multi-level task networks.
- **Primitive Operator Execution**: Concrete implementation of low-level robotic/simulated actions.

## 📂 Architecture
- `src/itl.py`: Contains the `HTN` logic and `ITLAgent`.

## 🛠️ Usage
```bash
python -m src.itl
```
