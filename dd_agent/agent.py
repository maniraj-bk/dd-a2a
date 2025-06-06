from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .sub_agents.logs import logs_agent



root_agent = LlmAgent(
    name="dd_agent",
    description="A simple agent that can be used to interact with the Datadog API.",
    model="gemini-2.0-flash",
    instruction="An agent that can be used to interact with the Datadog API. It can be used to query logs, metrics, and other data from Datadog. But currently only logs data is supported.",
    tools=[AgentTool(agent=logs_agent)],
    )