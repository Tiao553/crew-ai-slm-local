from crewai import Task

def create_research_task(agent, topic):
    return Task(
        name="research_task",
        description=f"""Analyze the topic '{topic}' and create:
        1. A complete hierarchical structure for the article
        2. Technical key points for each section
        3. Required visualization indications
        4. Complexity classification per section""",
        agent=agent,
        expected_output="""Structure in markdown format containing:
        - Main title
        - 5-7 main sections (##)
        - 3-5 subsections per main section (###)
        - Technical key points for each subsection
        - [VISUAL] indications where graphs/diagrams are needed
        - Complexity level (Basic/Intermediate/Advanced)"""
    )