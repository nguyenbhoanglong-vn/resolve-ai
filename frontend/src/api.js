const API_URL = "http://127.0.0.1.8000";

export async function createTicket(ticket) {
     const response = await fetch(
          `${API_URL}/tickets/`,
          {
               method: "POST",
               headers: {
                    "Content-Type": "application/json"
               },
               body: JSON.stringify(ticket)
          }
     );

     return response.json();
}

export async function analyzeTicket(id){
     const response = await fetch(
          `${API_URL}/tickets/${id}/analyze`,
          {
               method: "POST"
          }
     );

     return response.json();
}

export async function resolveTicket(id){
     const response = await fetch(
          `${API_URL}/tickets/${id}/resolve`,
          {
               method: "PATCH"
          }
     );
     
     return response.json();
}