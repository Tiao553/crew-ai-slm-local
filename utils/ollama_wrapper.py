from crewai import LLM
import ollama

class OllamaWrapper:
    def __init__(self):
        self.model_name = "llama3"
        self.base_url = "http://localhost:11434"
        
        # Configuração compatível com CrewAI
        self.llm = LLM(
            model=f"ollama/{self.model_name}",
            provider="ollama",
            config={
                "base_url": self.base_url,
                "model": self.model_name
            },
            temperature=0.7
        )
    
    def generate(self, prompt, system_prompt=None):
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            # Chamada direta ao Ollama como fallback
            response = ollama.chat(
                model=self.model_name,
                messages=messages
            )
            return response['message']['content']
        except Exception as e:
            print(f"Erro no Ollama: {str(e)}")
            return f"Erro na geração: {str(e)}"