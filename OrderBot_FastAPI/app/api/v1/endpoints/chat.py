from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.db.session import get_session
from app.models.order import ChatMessage
from app.schemas.chat import ChatResponse
from app.services.groq_service import groq_service
from typing import List, Optional
import uuid
from pathlib import Path

router = APIRouter()

# Read System Prompt from file
PROMPT_FILE = Path("app/core/system_prompt.txt")
if PROMPT_FILE.exists():
    SYSTEM_PROMPT = PROMPT_FILE.read_text()
else:
    # Fallback or error
    SYSTEM_PROMPT = "You are OrderBot, an automated pizza order assistant."

@router.post("/chat", response_model=ChatResponse)
async def chat(message: str, session_id: Optional[str] = None, db: AsyncSession = Depends(get_session)):
    if not session_id:
        session_id = str(uuid.uuid4())
    
    # 1. Fetch history
    result = await db.execute(select(ChatMessage).where(ChatMessage.session_id == session_id).order_by(ChatMessage.timestamp))
    history = result.scalars().all()
    
    # 2. Prepare messages for Groq
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for h in history:
        messages.append({"role": h.role, "content": h.content})
    
    messages.append({"role": "user", "content": message})
    
    # 3. Save User message to DB
    user_msg = ChatMessage(role="user", content=message, session_id=session_id)
    db.add(user_msg)
    
    # 4. Get Groq Response
    ai_response = await groq_service.get_chat_response(messages)
    
    # 5. Save AI message to DB
    ai_msg = ChatMessage(role="assistant", content=ai_response, session_id=session_id)
    db.add(ai_msg)
    
    await db.commit()
    
    return ChatResponse(response=ai_response, session_id=session_id)
