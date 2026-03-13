from pathlib import Path

def set_instructions(agent_dir: Path) -> str:
    instruction_file = agent_dir / 'instructions.md'
    return instruction_file.read_text(encoding='utf-8')