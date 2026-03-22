from sqlmodel import SQLModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class ChatMessageBase(SQLModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ChatMessage(ChatMessageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str = Field(index=True)

class OrderBase(SQLModel):
    items: str # JSON string or simplified text for now
    total_price: float
    status: str = "pending" # pending, confirmed, delivered
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None

class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    session_id: str = Field(index=True)
