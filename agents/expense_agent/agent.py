from google.adk.agents import LlmAgent

from pathlib import Path
from lib import fetch_model, instructions

def expense_agent() -> LlmAgent:
    return LlmAgent(
        model=fetch_model.get_base_model(),
        name='expense_agent',
        description='A helpful assistant for user questions.',
        instruction=instructions.set_instructions(Path(__file__).parent)
    )