import os
from dotenv import load_dotenv
from google import genai
import chromadb

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="support_kb"
)


def get_embedding(text):

    response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
    )

    return response.embeddings[0].values

def load_documents():

    docs = []

    data_folder = "data"

    for file in os.listdir(data_folder):

        path = os.path.join(data_folder, file)

        if file.endswith(".txt"):

            with open(path, "r", encoding="utf-8") as f:

                docs.append({
                    "source": file,
                    "content": f.read()
                })

    return docs

def ingest_documents():

    docs = load_documents()

    for idx, doc in enumerate(docs):

        embedding = get_embedding(
            doc["content"]
        )

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[{
                "source": doc["source"]
            }]
        )

    print("Documents Indexed Successfully")
    

def search_documents(query):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results

if __name__ == "__main__":

    ingest_documents()

    query = "How do I reset my password?"

    results = search_documents(query)

    print(results)