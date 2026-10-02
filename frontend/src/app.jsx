import { useEffect, useState } from "react";

import { 
     getTickets,
     createTicket,
     analyzeTicket,
     resolveTicket
} from "./api";

function App(){
     const [tickets, setTickets] = useState([]);

     async function loadTickets() {
          const data = await getTickets();
          setTickets(data);
     }

     useEffect(() => {
          loadTickets();
     }, []);

     async function handleResolve(id){
          await resolveTicket(id);
          await loadTickets();
     }

     return (
          <div>
               <h1>ResolveAI</h1>

               <p>
                    AI-powered support ticket management
               </p>

               {ticket.map(ticket => (
                    <div key={ticket.id}>
                         <h3>{ticket.title}</h3>

                         <p>{ticket.description}</p>

                         <p>
                              Priority: {ticket.priority || "Not analyzed"}
                         </p>

                         <button
                              onClick={() =>
                                   handleAnalyze(ticket.id)
                              }
                         >
                              Analyze
                         </button>

                         <button
                              onClick={() => 
                                   handleResolve(ticket.id)
                              }
                         >
                              Resolve
                         </button>
                    </div>    
               ))}
          </div>
     );
}

export default App;