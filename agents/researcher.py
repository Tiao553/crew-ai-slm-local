from crewai import Agent
from utils.prompts import RESEARCHER_SYSTEM_PROMPT
from utils.ollama_wrapper import OllamaWrapper

ollama = OllamaWrapper()

def create_researcher_agent():
    return Agent(
        role='Senior Research Analyst',
        goal='Break down topics and identify the best research approaches',
        backstory="""You're an expert researcher with years of experience in both 
        technical and non-technical domains. You know how to find the most reliable 
        sources and structure information effectively.""",
        verbose=True,
        tools=[],
        llm=ollama.llm,
        system_prompt=RESEARCHER_SYSTEM_PROMPT
    )

