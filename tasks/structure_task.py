from crewai import Task

def create_structure_task(agent, research_data):
    return Task(
        description=f"""Analyze the research data below and create:
        {research_data}

        1. Complete hierarchical structure
        2. Technical key points based on research
        3. Required visualizations
        4. Complexity classification""",
        agent=agent,
        expected_output="""Detailed structure containing:
        - Research-based title
        - Technically aligned sections
        - [VISUAL] research-supported indications
        - Data-justified complexity levels""",
        output_file="outputs/research_based_structure.md"
    )