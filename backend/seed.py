import requests

API_URL = "http://127.0.0.1:8000/tickets/"

demo_tickets = [
    {"title": "Payment failed", "description": "My credit card was charged but order status says unpaid.", "customer_email": "alex@example.com"},
    {"title": "Cannot login to account", "description": "Forgot password reset link is not arriving in my inbox.", "customer_email": "sarah@example.com"},
    {"title": "Delivery delayed", "description": "Package #8821 was supposed to arrive yesterday.", "customer_email": "john@example.com"},
    {"title": "Charged twice for subscription", "description": "I see two line items on my bank statement for this month.", "customer_email": "mira@example.com"},
    {"title": "App crashing on checkout", "description": "Whenever I click submit order on iOS app, it closes.", "customer_email": "dev@example.com"},
    {"title": "Request refund for order #102", "description": "Item received was damaged during shipping.", "customer_email": "clara@example.com"},
    {"title": "Update shipping address", "description": "I entered wrong house number on my recent order.", "customer_email": "tom@example.com"},
    {"title": "API Rate limit exceeded error", "description": "Getting 429 status code on production endpoint.", "customer_email": "tech@example.com"},
    {"title": "Invoice receipt request", "description": "Need VAT invoice PDF for company accounting.", "customer_email": "finance@example.com"}
]

print("Seeding demo tickets...")
for ticket in demo_tickets:
    try:
        res = requests.post(API_URL, json=ticket)
        if res.status_code == 200 or res.status_code == 201:
            print(f"Created: {ticket['title']}")
        else:
            print(f"Failed: {ticket['title']} - Status: {res.status_code}")
    except Exception as e:
        print(f"Error connecting to backend: {e}")
        break

print("Done seeding data!")