from crewai import Task


def debate_task(agent, topic):

    return Task(
        description=f"""
Debate this topic:

{topic}

Generate:

• pros
• cons
• research questions
""",

        expected_output="Debate summary",

        agent=agent
    )


def research_task(agent, topic):

    return Task(
        description=f"""
Research this topic:

{topic}

Include:

• statistics
• trends
• sources
""",

        expected_output="Detailed research with sources",

        agent=agent
    )


def writing_task(agent, topic):

    return Task(
        description=f"""
Write SEO blog article about:

{topic}

Include:

SEO title
Meta description
Keywords
Hashtags

Article sections + conclusion
""",

        expected_output="SEO article",

        agent=agent
    )


def editing_task(agent):

    return Task(
        description="""
Edit the article for grammar,
clarity and readability
""",

        expected_output="Final article",

        agent=agent
    )