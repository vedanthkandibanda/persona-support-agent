import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import search_documents
from src.generator import generate_response
from src.escalator import should_escalate, generate_handoff

st.set_page_config(
    page_title="Persona Support Agent",
    page_icon="🤖"
)

st.title("🤖 Persona-Aware Customer Support Agent")

query = st.text_area(
    "Enter Customer Query"
)

if st.button("Submit"):

    if query:

        persona = classify_persona(query)

        results = search_documents(query)

        retrieved_docs = results["documents"][0]

        sources = []

        if "metadatas" in results:
            sources = [
                item["source"]
                for item in results["metadatas"][0]
            ]

        st.subheader("Detected Persona")
        st.success(persona)

        st.subheader("Retrieved Sources")

        for source in sources:
            st.write(source)

        if should_escalate(query, retrieved_docs):

            st.error("Escalation Required")

            handoff = generate_handoff(
                persona,
                query,
                sources
            )

            st.subheader("Human Handoff Summary")

            st.json(handoff)

        else:

            response = generate_response(
                query,
                persona,
                retrieved_docs
            )

            st.subheader("Generated Response")

            st.write(response)