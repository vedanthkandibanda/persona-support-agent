# Persona-Aware Customer Support Agent

## Project Overview

This project is an AI-powered customer support assistant that adapts its responses based on the customer's persona. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant support information from a knowledge base and generate grounded responses. It also supports escalation to a human support representative when required.

## Features

- Persona Detection
  - Technical Expert
  - Frustrated User
  - Business Executive

- Knowledge Base Retrieval (RAG)
- ChromaDB Vector Database
- Gemini Embeddings
- Adaptive Response Generation
- Escalation Logic
- Human Handoff Summary
- Streamlit User Interface

---

## Tech Stack

### Backend
- Python 3.12

### LLM
- Gemini 2.5 Flash

### Embeddings
- Gemini Embedding Model

### Vector Database
- ChromaDB

### UI
- Streamlit

### Libraries
- google-genai
- chromadb
- streamlit
- python-dotenv
- pypdf

---

## Architecture

User Query
↓
Persona Detection
↓
Knowledge Base Retrieval (RAG)
↓
Adaptive Response Generation
↓
Escalation Check
↓
Human Handoff Summary

---

## Persona Detection Strategy

The system classifies users into one of three personas:

### Technical Expert
Uses technical terminology such as APIs, logs, configurations, and authentication.

### Frustrated User
Uses emotional language, complaints, or urgent requests.

### Business Executive
Focuses on business impact, operations, timelines, and outcomes.

---

## RAG Pipeline Design

1. Load support documents
2. Generate embeddings
3. Store embeddings in ChromaDB
4. Convert user query into embedding
5. Retrieve top matching documents
6. Generate grounded response using Gemini

---

## Escalation Logic

The system escalates conversations when:

- Billing issues occur
- Refund requests are raised
- Legal concerns are mentioned
- Sensitive account operations are requested
- Relevant information is unavailable

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository_url>
cd persona-support-agent
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Example Queries

### Technical Expert

Can you explain the API authentication failure and provide logs?

### Frustrated User

I've tried everything and nothing works!

### Business Executive

How does this issue impact business operations?

### Escalation Example

I was charged twice and need a refund.

---

## Future Improvements

- Multi-turn conversation memory
- Confidence scoring
- LangGraph workflow
- Analytics dashboard
- Human approval workflow

---

## Author

Vedanth Kandibanda
