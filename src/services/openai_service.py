from openai import OpenAI
import os

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run_gpt(self, prompt: str):
        """
        Sends a prompt to your GPT and returns the response text.
        Adjust model name if needed.
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
