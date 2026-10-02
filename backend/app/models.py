from pydoc import describe

from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from .database import Base

class Ticket(Base):
     __tablename__ = "tickets"

     id = Column(Integer, primary_key=True, index=True)

     title = Column(String(200), nullable=False)

     description = Column(Text, nullable=False)

     customer_email = Column(String(255), nullable=False)

     category = Column(String(50), nullable=True)

     priority = Column(String(20), nullable=True)

     summary = Column(Text, nullable=True)

     suggested_action = Column(Text, nullable=True)

     draft_response = Column(Text, nullable=True)

     status = Column(String(20), default="open")

     create_at = Column(
          DateTime,
          default=datetime.utcnow
     )

