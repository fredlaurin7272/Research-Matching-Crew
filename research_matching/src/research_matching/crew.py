from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import TXTSearchTool
from crewai_tools import SerperDevTool

@CrewBase
class ResearchMatchingCrew():
    """ResearchMatchingCrew crew"""

    @agent
    def data_collection_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collection_expert'],
            tools=[ScrapeWebsiteTool(), TXTSearchTool(), SerperDevTool()],
        )

    @agent
    def interest_matching_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['interest_matching_specialist'],
            
        )

    @agent
    def reporting_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_specialist'],
            
        )


    @task
    def collect_company_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['collect_company_data_task'],
            tools=[ScrapeWebsiteTool(), SerperDevTool()],
        )

    @task
    def gather_research_publications_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_research_publications_task'],
            tools=[TXTSearchTool(), SerperDevTool()],
        )

    @task
    def match_interests_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_interests_task']
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AligningResearchInterestsForCollaborativeAiDevelopment crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            task_dependencies={
                'match_interests_task': ['collect_company_data_task', 'gather_research_publications_task'],
                'generate_report_task': ['match_interests_task']
            }
        )