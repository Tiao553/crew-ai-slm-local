from crewai import Agent
from utils.prompts import WRITER_SYSTEM_PROMPT
from utils.ollama_wrapper import OllamaWrapper

ollama = OllamaWrapper()

def create_writer_agent():
    return Agent(
        role='Professional Content Writer',
        goal='Create well-structured, engaging content with appropriate visual markers',
        backstory="""You're an experienced writer who can adapt to different styles 
        and formats. You know exactly when to include visuals to enhance understanding.""",
        verbose=True,
        tools=[],
        llm=ollama.llm,
        system_prompt=WRITER_SYSTEM_PROMPT
    )
