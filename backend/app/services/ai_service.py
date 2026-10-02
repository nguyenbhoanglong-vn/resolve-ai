import os
import json
import re
from urllib import response
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ticket_with_ai(title: str, description: str):
     prompt = f"""Analyze the following customer support ticket and return a JSON object with:
     - category (Billing, Technical, Account, Delivery, Other)- priority (HIGH, MEDIUM, LOW)
     - summary (Brief summary in 1-2 sentences)
     - suggested_action (Action steps for support agent)
     - draft_response (Polite draft response to customer)
     Ticket Title: {title}
     Ticket Description: {description}
     """
     try:
          response = client.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[
                    {"role": "system", "content": "You are an AI support assistant. Return output strictly in valid JSON format."},
                    {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"}
          )

          content = response.choices[0].message.content or "{}"
          result = json.loads(content)
          return result
     except Exception as e:
          print(f"Error AI service: {e}")

          return{
               "category": "General",
               "priority": "MEDIUM",
               "summary": "Cannot analyze automatically.",
               "suggested_action": "Manual review required.",
               "draft_response": "Hello, we received your issue and are reviewing it."
          }