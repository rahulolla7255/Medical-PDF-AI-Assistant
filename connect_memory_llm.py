import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    max_tokens=512,
    api_key=os.getenv("GROQ_API_KEY")
)

# Initialize Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS Vector Database
db = FAISS.load_local(
    "vectorstore/db_faiss",
    embedding,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})


def get_answer(query):
    """
    Returns answer from the RAG pipeline.
    """

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an expert medical assistant.

Use ONLY the following context to answer the user's question.

If the answer is not present in the context, reply:
"I couldn't find this information in the provided medical documents."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content


# Optional: Run from terminal
if __name__ == "__main__":
    while True:
        query = input("\nAsk a Question (type 'exit' to quit): ")

        if query.lower() == "exist":
            break

        answer = get_answer(query)

        print("\nAnswer:\n")
        print(answer)