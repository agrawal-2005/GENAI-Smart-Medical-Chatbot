from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

from langchain_community.llms import CTransformers
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

app = Flask(__name__)

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
INDEX_NAME = "medical"

# Initialize embeddings and vector store
print("Initializing embeddings and vector store...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
docsearch = PineconeVectorStore.from_existing_index(INDEX_NAME, embeddings)
print("✅ Initialization complete.")

# Define the prompt template
prompt_template = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Initialize the LLM
# llm = CTransformers(
#     model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",  # Make sure this path is correct
#     model_type="llama",
#     config={'max_new_tokens': 512, 'temperature': 0.8}
# )
#Lower memory model for faster response
llm = CTransformers(
    model="/home/saggy/DocBot_RAG/model/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", # <-- NEW MODEL
    model_type="llama", # This can often stay as 'llama' for compatible models
    config={'max_new_tokens': 512, 'temperature': 0.7}
)

# Define the RAG chain using LCEL
retriever = docsearch.as_retriever(search_kwargs={'k': 2})

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    print(f"Received query: {input_text}")
    result = rag_chain.invoke(input_text)
    print(f"Response: {result}")
    return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)