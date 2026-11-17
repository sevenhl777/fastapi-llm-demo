from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import uuid
import datetime

Base = declarative_base()

class ChatMsg(Base):
    __tablename__ = "chat_msg"
    
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey("conversation.id"))
    title = Column(String(200))
    content = Column(String(2000))
    role = Column(String(100), default="role")
    created_at = Column(DateTime, default=datetime.datetime.now)

    chat_conversation = relationship("Conversation", back_populates="chat_msgs")

class Conversation(Base):
    __tablename__ = "conversation"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    title = Column(String(200))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)

    chat_msgs = relationship("ChatMsg", back_populates="chat_conversation")
