from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate(
    template="""
You are an intelligent AI assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
""",

    input_variables=["context", "question"]
)