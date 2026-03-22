from groq import AsyncGroq
from app.core.config import settings
from typing import List, Dict

class GroqService:
    def __init__(self):
        self.client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL

    async def get_chat_response(self, messages: List[Dict[str, str]], temperature: float = 0.0) -> str:
        chat_completion = await self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=temperature,
            stream=False,
        )
        return chat_completion.choices[0].message.content

groq_service = GroqService()
