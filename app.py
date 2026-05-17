import streamlit as st
import tempfile
import os
import asyncio

# -------- Utils --------
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_docs
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.qa_chain import build_chain

# =========================================================
# FIX EVENT LOOP (IMPORTANT FOR GEMINI + STREAMLIT)
# =========================================================

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# =========================================================
# GOOGLE API KEY
# =========================================================

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Chatbot")
st.caption("Chat with your PDF using RAG + Gemini")

# =========================================================
# SESSION STATE
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type="pdf"
    )

    if uploaded_file is not None:

        # Prevent reprocessing same PDF
        if st.session_state.current_pdf != uploaded_file.name:

            with st.spinner("Processing PDF..."):

                # Save temp PDF
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp_file:

                    tmp_file.write(uploaded_file.read())
                    file_path = tmp_file.name

                # =================================================
                # LOAD
                # =================================================

                documents = load_pdf(file_path)

                # =================================================
                # SPLIT
                # =================================================

                chunks = split_docs(documents)

                # =================================================
                # EMBEDDINGS
                # =================================================

                embeddings = get_embeddings()

                # =================================================
                # VECTOR STORE
                # =================================================

                db = create_vector_store(
                    chunks,
                    embeddings
                )

                # =================================================
                # QA CHAIN
                # =================================================

                qa_chain = build_chain(db)

                # Save in session
                st.session_state.qa_chain = qa_chain
                st.session_state.current_pdf = uploaded_file.name

                # Clear old chat
                st.session_state.chat_history = []

            st.success("✅ PDF Ready!")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()

# =========================================================
# MAIN CHAT UI
# =========================================================

if st.session_state.qa_chain is None:

    st.info("👈 Upload a PDF from sidebar to start chatting.")

else:

    # =====================================================
    # DISPLAY CHAT HISTORY
    # =====================================================

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # =====================================================
    # USER INPUT
    # =====================================================

    user_input = st.chat_input(
        "Ask something about your PDF..."
    )

    if user_input:

        # -------------------------------------------------
        # USER MESSAGE
        # -------------------------------------------------

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):

            st.markdown(user_input)

        # -------------------------------------------------
        # ASSISTANT RESPONSE
        # -------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                result = st.session_state.qa_chain.invoke({
                    "input": user_input
                })

                answer = result["answer"]

                st.markdown(answer)

        # Save response
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })