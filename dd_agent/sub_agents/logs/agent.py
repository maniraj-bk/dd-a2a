from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

logs_agent = Agent(
    name="logs_agent",
    model="gemini-2.0-flash-lite",
    description=(
        "Agent to query datadog logs."
    ),
    instruction=(
        "You are a helpful agent who can find and return logs from Datadog within a time range from and to."
    ),
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@winor30/mcp-server-datadog"
                ],
                env = {
                    "DATADOG_API_KEY": "",
                    "DATADOG_APP_KEY": ""
                }
            ),
        )
    ]
)