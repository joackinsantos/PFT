from google.adk.agents import llm_agent

from lib import fetch_model

root_agent = llm_agent.Agent(
    model=fetch_model.get_base_model(),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)