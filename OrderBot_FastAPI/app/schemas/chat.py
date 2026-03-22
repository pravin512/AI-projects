from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChatMessageSchema(BaseModel):
    role: str
    content: str
    timestamp: datetime

class ChatResponse(BaseModel):
    response: str
    session_id: str

class OrderResponse(BaseModel):
    id: int
    items: str
    total_price: float
    status: str
    created_at: datetime
    session_id: str
