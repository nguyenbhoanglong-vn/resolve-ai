from pydantic import BaseModel, EmailStr

class TicketCreate(BaseModel):
     title: str
     description: str
     customer_email: EmailStr


class TicketResponse(BaseModel):
     id: int
     title: str
     description: str
     customer_email: str
     category: str | None
     priority: str | None
     summary: str | None
     suggested_action: str | None
     draft_response: str | None
     status: str

class Config:
     from_attributes = True
