import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(user_query, persona, retrieved_docs):

    context = "\n\n".join(retrieved_docs)

    if persona == "Technical Expert":

        style = """
Provide:
- Detailed explanation
- Technical terminology
- Root cause analysis
- Step-by-step troubleshooting
"""

    elif persona == "Frustrated User":

        style = """
Provide:
- Empathetic response
- Simple language
- Reassurance
- Action-oriented steps
"""

    else:

        style = """
Provide:
- Concise response
- Business impact
- Resolution guidance
- Minimal technical jargon
"""

    prompt = f"""
You are a customer support assistant.

Persona:
{persona}

Response Style:
{style}

Knowledge Base Context:
{context}

User Question:
{user_query}

Important:
Only answer using the provided context.
Do not make up information.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text