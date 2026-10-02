function TicketList({ tickets, selectedTicket, onSelectTicket, loadingList }) {
  if (loadingList) {
    return <div className="state-box">Loading...</div>;
  }

  if (tickets.length === 0) {
    return (
      <div className="state-box">
        <p>No support tickets yet.</p>
        <p className="sub-text">Create your first ticket.</p>
      </div>
    );
  }

  return (
    <div className="ticket-list">
      {tickets.map((ticket) => (
        <div
          key={ticket.id}
          className={`ticket-item ${
            selectedTicket?.id === ticket.id ? "active" : ""
          }`}
          onClick={() => onSelectTicket(ticket)}
        >
          <span>#{ticket.id} {ticket.title}</span>
          <span>{ticket.category || "General"}</span>
          <span className={`badge priority-${(ticket.priority || "LOW").toLowerCase()}`}>
            {ticket.priority || "NORMAL"}
          </span>
        </div>
      ))}
    </div>
  );
}

export default TicketList;