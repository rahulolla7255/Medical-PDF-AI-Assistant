import streamlit as st
from connect_memory_llm import get_answer

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stChatMessage {
    border-radius:12px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🩺 Medical AI Assistant")
st.caption("Powered by Groq • Llama 3.1 • LangChain • FAISS")

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    st.header("📚 About")

    st.write(
        """
This chatbot answers questions from the medical PDF
using Retrieval-Augmented Generation (RAG).

**LLM**
- Llama 3.1 8B Instant

**Vector DB**
- FAISS

**Embeddings**
- all-MiniLM-L6-v2
"""
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# User Input
# -------------------------------
prompt = st.chat_input("Ask a medical question...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching medical knowledge..."):

            try:
                answer = get_answer(prompt)

            except Exception as e:
                answer = f"❌ Error:\n\n{e}"

        st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    