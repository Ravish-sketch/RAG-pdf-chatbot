from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate(
    template="""
    Answer based on context only.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """,
    input_variables=["context", "input"]
)