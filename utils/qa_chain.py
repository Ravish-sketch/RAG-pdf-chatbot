from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from utils.prompt import custom_prompt

def build_chain(db):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.3
    )

    retriever = db.as_retriever(search_kwargs={"k": 4})

    document_chain = create_stuff_documents_chain(
        llm,
        custom_prompt
    )

    return create_retrieval_chain(
        retriever,
        document_chain
    )