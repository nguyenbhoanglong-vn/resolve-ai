function TicketDetail({ selectedTicket, isAnalyzing, onResolveTicket }) {
  if (!selectedTicket) {
    return (
      <div className="detail-card state-box">
        <p>Select a ticket to view details.</p>
      </div>
    );
  }

  return (
    <div className="detail-card">
      <h3>{selectedTicket.title}</h3>
      <p className="sub-text">{selectedTicket.customer_email}</p>

      <div className="section">
        <span className="section-label">CUSTOMER ISSUE</span>
        <p>{selectedTicket.description}</p>
      </div>

      <div className="section">
        <span className="section-label">AI ANALYSIS</span>
        {isAnalyzing ? (
          <div className="loading-text">Analyzing...</div>
        ) : (
          <>
            <p><strong>Category:</strong> {selectedTicket.category || "N/A"}</p>
            <p><strong>Priority:</strong> {selectedTicket.priority || "N/A"}</p>
            <p><strong>Summary:</strong> {selectedTicket.summary || "N/A"}</p>
            <p><strong>Suggested Action:</strong> {selectedTicket.suggested_action || "N/A"}</p>
            <div className="draft-box">
              {selectedTicket.draft_response || "N/A"}
            </div>
          </>
        )}
      </div>

      {selectedTicket.status !== "resolved" && (
        <button
          className="btn-resolve"
          onClick={() => onResolveTicket(selectedTicket.id)}
        >
          [Resolve Ticket]
        </button>
      )}
    </div>
  );
}

export default TicketDetail;