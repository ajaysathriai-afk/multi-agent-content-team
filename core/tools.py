from crewai.tools import BaseTool
from tavily import TavilyClient
import os


class WebResearchTool(BaseTool):

    name: str = "web_research"
    description: str = "Search the web for latest information"

    def _run(self, query: str):

        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        results = []

        for r in response["results"]:
            results.append(
                f"""
TITLE: {r['title']}
URL: {r['url']}
CONTENT: {r['content']}
"""
            )

        return "\n".join(results)


web_research_tool = WebResearchTool()