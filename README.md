# 🩺 Medical RAG Chatbot

An AI-powered Medical PDF Chatbot that answers questions from medical documents using Retrieval-Augmented Generation (RAG).

The chatbot reads medical PDF files, creates vector embeddings using HuggingFace, stores them in a FAISS vector database, and retrieves the most relevant information to generate accurate responses with Groq's Llama 3.1 model.

---

## 🚀 Features

- 📄 Medical PDF Question Answering
- 🤖 AI-Powered Responses using Groq Llama 3.1
- 🔍 Retrieval-Augmented Generation (RAG)
- 📚 FAISS Vector Database
- 🧠 HuggingFace Embeddings
- 💬 Interactive Streamlit Chat Interface
- ⚡ Fast Semantic Search
- 🔐 Secure API Key Management using .env
- 📖 Answers Generated Only from Uploaded Documents

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Llama 3.1 8B Instant
- HuggingFace Embeddings
- FAISS
- PyPDF
- Python Dotenv

---

## 📂 Project Structure

```
Medical-RAG-Chatbot/
│
├── app.py
├── connect_memory_llm.py
├── create_memory_llm.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│   └── medical.pdf
│
└── vectorstore/
    └── db_faiss/
```

---

## ⚙️ Installation

### Clone Repository

```bash
cd Medical-RAG-Chatbot
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Add API Key

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📄 Add Medical PDF

Place your PDF inside

```
data/
```

---

## 🧠 Create Vector Database

```bash
python create_memory_llm.py
```

This will

- Read PDF
- Split text into chunks
- Create embeddings
- Save FAISS vector database

---

## ▶️ Run Chatbot

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What is Diabetes?
- What are the symptoms of Pneumonia?
- Explain Chickenpox.
- What causes Asthma?
- What are the treatment options for Hypertension?

---

## 🧠 How RAG Works

```
Medical PDF
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
User Question
      │
      ▼
Semantic Search
      │
      ▼
Relevant Context
      │
      ▼
Groq Llama 3.1
      │
      ▼
Generated Answer
```

---

## 📦 Requirements

- Python 3.10+
- Groq API Key

---

## 🔮 Future Improvements

- Upload PDF from UI
- Multiple PDF Support
- Source Page References
- Deploy on Streamlit Cloud



## 👨‍💻 Author

Rahul

Learning Data Science | Machine Learning | Deep Learning | Generative AI

---

## ⭐ If you found this project helpful, don't forget to star the repository.
