from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pprint import pprint

from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters # For Stdio Server

# Example server_params (choose one based on your server type):
# 1. Stdio Server:
server_params = StdioServerParameters(
    command="npx",  # Use node to run the JavaScript server
    args=["@playwright/mcp@latest"],  # Path to the built server
)

# Example usage (uncomment and adapt once server_params is set):
with MCPServerAdapter(server_params) as mcp_tools:
    # print(f"Available tools: {[tool.name for tool in mcp_tools]}")

    @CrewBase
    class RealEstateIntelligenceUnit:
        """RealEstateIntelligenceUnit crew"""

        mcp_server_params = [
            StdioServerParameters(
                command="npx",  # Use node to run the JavaScript server
                args=["@playwright/mcp@latest"],  # Path to the built server
            )
        ]

        agents: List[BaseAgent]
        tasks: List[Task]


        # Learn more about YAML configuration files here:
        # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
        # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

        # If you would like to add tools to your agents, you can learn more about it here:
        # https://docs.crewai.com/concepts/agents#agent-tools
        @agent
        def senior_property_scout(self) -> Agent:
            return Agent(
                config=self.agents_config['senior_property_scout'], # type: ignore[index]
                verbose=True,
                reasoning=False,
                tools=mcp_tools,
            )

        @agent
        def real_estate_analyst(self) -> Agent:
            return Agent(
                config=self.agents_config['real_estate_analyst'], # type: ignore[index]
                verbose=True,
                reasoning=False,
                tools=mcp_tools,
            )

        # To learn more about structured task outputs,
        # task dependencies, and task callbacks, check out the documentation:
        # https://docs.crewai.com/concepts/tasks#overview-of-a-task
        @task
        def initial_market_scan(self) -> Task:
            return Task(
                config=self.tasks_config['initial_market_scan'], # type: ignore[index]
                output_file='scout_report.md'
            )

        @task
        def in_depth_analysis_and_reporting(self) -> Task:
            return Task(
                config=self.tasks_config['in_depth_analysis_and_reporting'], # type: ignore[index]
                output_file='property_analysis_report.md'
            )

        @crew
        def crew(self) -> Crew:
            """Creates the RealEstateIntelligenceUnit crew"""
            # To learn how to add knowledge sources to your crew, check out the documentation:
            # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

            return Crew(
                agents=self.agents, # Automatically created by the @agent decorator
                tasks=self.tasks, # Automatically created by the @task decorator
                process=Process.sequential,
                verbose=True,
                # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            )

    inputs = {
        'portals': ", ".join(['https://www.kleinanzeigen.de/s-haus-kaufen/bungalow,einfamilienhaus,villa/nordrhein-westfalen/preis::500000/c208l928+haus_kaufen.haustyp_s:(bungalow%2Ceinfamilienhaus%2Cvilla)+options:haus_kaufen.celler_loft_b,haus_kaufen.garage_b']),
    }

    RealEstateIntelligenceUnit().crew().kickoff(inputs=inputs)
