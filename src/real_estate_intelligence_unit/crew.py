from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class RealEstateIntelligenceUnit():
    """RealEstateIntelligenceUnit crew"""

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
            verbose=True
        )

    @agent
    def real_estate_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['real_estate_analyst'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def initial_market_scan(self) -> Task:
        return Task(
            config=self.tasks_config['initial_market_scan'], # type: ignore[index]
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
