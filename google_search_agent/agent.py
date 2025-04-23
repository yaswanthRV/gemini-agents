from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="basic_google_search_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to search the web for information."
    ),
    instruction=(
        "You are an expert researcher. You always stick to the facts."
    ),
    tools=[google_search],
)