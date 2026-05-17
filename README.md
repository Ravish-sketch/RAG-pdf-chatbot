# 📄 AI PDF Chatbot (RAG + Gemini)

An AI-powered PDF chatbot built using:

- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Google Gemini API

This chatbot allows users to upload PDF files and ask questions about the content using Retrieval-Augmented Generation (RAG).

---

# 🚀 Features

✅ Upload PDF files  
✅ Chat-style interface  
✅ Chat history  
✅ Semantic search with FAISS  
✅ Gemini-powered responses  
✅ Modular project structure  
✅ Fast document retrieval  
✅ Streamlit UI  

---

# 🧠 Tech Stack

| Technology | Usage |
|---|---|
| Streamlit | Frontend UI |
| LangChain | RAG pipeline |
| FAISS | Vector database |
| HuggingFace | Embeddings |
| Gemini API | LLM responses |

---

# 📂 Project Structure

```bash
pdf-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── qa_chain.py
│   └── prompt.py
│
├── data/
├── assets/
├── faiss_index/
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone repository

```bash
git clone https://github.com/Ravish-sketch/RAG-pdf-chatbot.git
```

---

## 2️⃣ Open folder

```bash
cd RAG-pdf-chatbot
```

---

## 3️⃣ Create virtual environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate venv

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5️⃣ Install requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Gemini API Key

Create `.env`

```env
GOOGLE_API_KEY=your_api_key
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

---

# 📸 Demo

Upload PDF → Ask Questions → Get AI Answers

---

# 🔥 Future Improvements

- Multi PDF support
- Streaming responses
- Voice input
- Source citations
- Authentication
- Cloud deployment

---

# 👨‍💻 Author

Ravish Kumar

---

# ⭐ If you like this project

Give it a star on GitHub ⭐