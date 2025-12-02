from ..services.openai_service import OpenAIService

class GenerateContentUseCase:
    def __init__(self):
        self.ai = OpenAIService()

    def execute(self, prompt: str) -> str:
        """
        Usecase que recebe um prompt e devolve o texto gerado pelo GPT.
        """
        return self.ai.run_gpt(prompt)
