from src.classifier import classify_persona
from src.rag_pipeline import search_documents
from src.generator import generate_response
from src.escalator import should_escalate, generate_handoff

query = input("Enter your question: ")

persona = classify_persona(query)

results = search_documents(query)

retrieved_docs = results["documents"][0]

sources = []

if "metadatas" in results:
    sources = [
        item["source"]
        for item in results["metadatas"][0]
    ]

print("\nDetected Persona:")
print(persona)

print("\nRetrieved Sources:")
for source in sources:
    print("-", source)

if should_escalate(query, retrieved_docs):

    print("\nESCALATION REQUIRED")

    handoff = generate_handoff(
        persona,
        query,
        sources
    )

    print("\nHandoff Summary:")
    print(handoff)

else:

    response = generate_response(
        query,
        persona,
        retrieved_docs
    )

    print("\nResponse:")
    print(response)