import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify_persona(user_message):
    
    msg = user_message.lower()

    # Rule-based detection first
    if any(word in msg for word in ["api", "log", "authentication", "config"]):
        return "Technical Expert"

    if any(word in msg for word in ["angry", "frustrated", "terrible", "nothing works"]):
        return "Frustrated User"

    if any(word in msg for word in ["business", "operations", "revenue", "timeline"]):
        return "Business Executive"


    prompt = f"""
You are a customer support persona classifier.

Classify the user into EXACTLY ONE persona.

Technical Expert:
- Talks about APIs
- Logs
- Authentication
- Configurations
- Technical troubleshooting

Frustrated User:
- Angry
- Emotional
- Complaining
- Urgent requests

Business Executive:
- Business impact
- Operations
- Revenue
- Timeline
- Management concerns

User Message:
{user_message}

Return ONLY one of:

Technical Expert
Frustrated User
Business Executive
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


if __name__ == "__main__":

    tests = [
        "Can you explain the API authentication failure and provide logs?",
        "I've tried everything and nothing works!",
        "How does this issue impact business operations?"
    ]

    for t in tests:
        print("\nMessage:", t)
        print("Persona:", classify_persona(t))