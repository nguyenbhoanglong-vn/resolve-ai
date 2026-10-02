import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

// Export hàm getTickets
export const getTickets = async () => {
  const response = await axios.get(`${API_URL}/tickets`);
  return response.data;
};

// Export các hàm khác nếu App.jsx có import
export const createTicket = async (ticketData) => {
  const response = await axios.post(`${API_URL}/tickets/`, ticketData);
  return response.data;
};

export const analyzeTicket = async (id) => {
  const response = await axios.post(`${API_URL}/tickets/${id}/analyze`);
  return response.data;
};

export const resolveTicket = async (id) => {
  const response = await axios.patch(`${API_URL}/tickets/${id}/resolve`);
  return response.data;
};

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