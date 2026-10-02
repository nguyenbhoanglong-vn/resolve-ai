from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Ticket
from ..schemas import TicketCreate

router = APIRouter(
     prefix = "/tickets",
     tags = ["tickets"]
)

@router.post("/")
def create_ticket(
     ticket: TicketCreate,
     db: Session = Depends(get_db)
):
     new_ticket = Ticket(
          title=ticket.title,
          description=ticket.description,
          customer_email=ticket.customer_email
     )

     db.add(new_ticket)
     db.commit()
     db.refresh(new_ticket)

     return new_ticket

@router.get("/")
def get_tickets(
     db: Session = Depends(get_db)
):
     return db.query(Ticket).order_by(
          Ticket.create_at.desc()
     ).all()

@router.get("/{ticket_id}")
def get_ticket(
     ticket_id: int,
     db: Session = Depends(get_db)
):
     return db.query(Ticket).filter(
          Ticket.id == ticket_id
     ).first()

@router.patch("/{ticket.id}/resolve")
def resolve_ticket(
     ticket_id: int, 
     db: Session = Depends(get_db)
):
     ticket = db.query(Ticket).filter(
          Ticket.id == ticket_id
     ).first()

     ticket.status = "resolved" # type: ignore

     db.commit()
     db.refresh(ticket)

     return ticket

@router.post("/{ticket_id}/analyze")
def analyze_ticket(
     ticket_id: int,
     db: Session = Depends(get_db)
):
     ticket: Ticket = db.query(Ticket).filter(
          Ticket.id == ticket_id
     ).first()

     # Call AI service
     if not ticket:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Ticket not found"
          )
     
     ticket.category = "Billing" # type: ignore
     ticket.priority = "High" # type: ignore
     ticket.summary = "Customer reports duplicate billing." # type: ignore
     ticket.suggested_action = "Review payment records." # type: ignore
     ticket.draft_response = ( # type: ignore
          "We are sorry for the inconvenience..."
     )

     db.commit()
     db.refresh(ticket)

     return ticket