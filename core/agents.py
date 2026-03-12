from crewai import Agent
from core.tools import web_research_tool


class ContentAgents:

    def debate_agent(self):

        return Agent(
            role="Debate Analyst",
            goal="Analyze topic from multiple perspectives",
            backstory="Expert analyst exploring pros and cons",
            verbose=True
        )

    def research_agent(self):

        return Agent(
            role="Research Analyst",
            goal="Perform web research",
            backstory="Expert researcher collecting data",
            tools=[web_research_tool],
            verbose=True
        )

    def writer_agent(self):

        return Agent(
            role="Content Writer",
            goal="Write SEO optimized article",
            backstory="Professional tech writer",
            verbose=True
        )

    def editor_agent(self):

        return Agent(
            role="Content Editor",
            goal="Improve clarity and grammar",
            backstory="Senior editor",
            verbose=True
        )