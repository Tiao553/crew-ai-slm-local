from crewai import Task

def create_writing_task(agent, research_data):
    return Task(
        name="writing_task",
        description=f"""Produce the complete article FOLLOWING EXACTLY this structure:
        {research_data}
        
        Requirements:
        - Expand each key point into 2-3 paragraphs
        - Include technical examples when marked as [EXAMPLE]
        - Add smooth transitions between sections
        - Maintain terminological consistency""",
        agent=agent,
        expected_output="Complete technical article in markdown with 3500-4000 words"
    )