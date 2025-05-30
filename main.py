from crewai import Crew, Process
from agents.researcher import create_researcher_agent
from agents.writer import create_writer_agent
from tasks.research_task import create_research_task
from tasks.structure_task import create_structure_task
from tasks.writing_task import create_writing_task
import os
from pathlib import Path

# Environment setup
os.environ["OPENAI_API_KEY"] = "sk-ignore"  # Bypass for local LLMs
os.environ["CHROMA_OPENAI_API_KEY"] = "sk-ignore"  # Disable vector DB

def run_crewai_project(topic):
    # Create output directory
    outputs_dir = Path("./outputs")
    outputs_dir.mkdir(exist_ok=True)

    # 1. Initialize agents
    researcher = create_researcher_agent()
    writer = create_writer_agent()

    # 2. Create tasks
    research_task = create_research_task(researcher, topic)
    structure_task = create_structure_task(researcher, research_task)
    writing_task = create_writing_task(writer, structure_task)

    # 3. Configure and run crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, structure_task, writing_task],
        process=Process.sequential,
        verbose=True,
        memory=False,
        manager_llm=researcher.llm
    )

    # 4. Execute the crew workflow
    print(f"🚀 Starting workflow for topic: {topic}")
    result = crew.kickoff()

    # 5. Save outputs
    with open(outputs_dir/"final_article.md", "w") as f:
        f.write(str(result))

    print(f"""
    ✅ Process completed!
    Final article saved to: outputs/final_article.md
    """)

    return result

if __name__ == "__main__":
    topic = input("Enter the topic to research and write about: ")
    result = run_crewai_project(topic)
    print("\n\nFinal Output:")
    print(result)