from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from pathlib import Path
from lib import fetch_model, instructions
from expense_agent import agent as expense_agent

root_agent = LlmAgent(
    model=fetch_model.get_base_model(),
    name='financial_coordinator',
    description='A helpful assistant for user questions.',
    instruction=instructions.set_instructions(Path(__file__).parent),
    tools=[
        AgentTool(agent=expense_agent.expense_agent())
    ],
)