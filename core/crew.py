from crewai import Crew
from core.agents import ContentAgents
from core.tasks import debate_task, research_task, writing_task, editing_task


class ContentCrew:

    def run(self, topic):

        agents = ContentAgents()

        debate = agents.debate_agent()
        researcher = agents.research_agent()
        writer = agents.writer_agent()
        editor = agents.editor_agent()

        tasks = [

            debate_task(debate, topic),

            research_task(researcher, topic),

            writing_task(writer, topic),

            editing_task(editor)

        ]

        crew = Crew(
            agents=[debate, researcher, writer, editor],
            tasks=tasks,
            verbose=True
        )

        result = crew.kickoff()

        return result