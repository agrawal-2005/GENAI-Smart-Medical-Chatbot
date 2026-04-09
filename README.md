# 🧠 RAG_GENAI_Medical_Docbot or Chatbot

A smart medical chatbot webapp that leverages **RAG (Retrieval-Augmented Generation)** techniques to deliver accurate, context-aware responses using a custom knowledge base and advanced language models.

---

## 🚀 Project Overview

This project is a **smart medical chatbot web application** built using the following technologies:

- **Langchain** for Retrieval-Augmented Generation (RAG) pipeline.
- **Context-aware embeddings** for building a vector database.
- **Quantized Llama-2 Large Language Model (LLM)** for efficient query answering.
- **Web interface** built with Python backend (Flask or FastAPI), HTML, CSS and served via a user-friendly UI.

The solution boosts response accuracy by up to **20%** using context-based document retrieval before generation.

---

## 📂 Project Structure

```
RAG_GENAI_DocBot/
├── data/                  # Contains datasets or documents used to build the knowledge base
├── model/                 # Pre-trained and quantized models (Llama-2 or others)
├── research/              # Notebooks or scripts for experiments and testing
├── src/                   # Source code for core logic (retrieval, embedding, RAG pipeline)
├── static/                # Static files (CSS, JS, images) for the frontend
├── templates/             # HTML templates for the web interface
├── .gitignore             # Files and folders to be ignored by Git
├── LICENSE                # License information
├── README.md              # Project overview and instructions
├── app.py                 # Main application (runs the web server)
├── requirements.txt       # Project dependencies
├── setup.py               # Setup script for packaging (optional for installation)
├── store_index.py         # Script to create/store vector embeddings and index
├── template.py            # Utility template Python file
```

---

## 🛠️ Key Features

- **Retrieval-Augmented Generation (RAG):** Retrieves relevant documents from a custom knowledge base before generating responses.
- **Context-aware Embeddings:** Ensures that responses are accurate and specific to the user's query.
- **Quantized Llama-2 LLM:** Efficient, lightweight model serving for quick responses.
- **Web Application Interface:** User-friendly interface for entering queries and viewing answers.

---

## 📌 Installation Instructions

### Prerequisites

- Python 3.8+
- Git
- Virtual Environment (optional but recommended)

### Clone the repository

```bash
git clone https://github.com/Aniketkumar121/RAG_GENAI_DocBot.git
cd RAG_GENAI_DocBot
```

### Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Running the Application

### 1️⃣ Build Vector Store (Optional if already generated)

```bash
python store_index.py
```

This will generate embeddings and store them in the vector database.

### 2️⃣ Run the web application

```bash
python app.py
```

This will start a local web server.  
Open your browser and visit:

```
http://127.0.0.1:5000
```

to interact with the chatbot UI.

---

## 🧠 How it works

1. **User inputs a query** via web interface.
2. **Query is embedded** and compared with pre-stored document embeddings in the vector database.
3. **Top-k relevant documents are retrieved.**
4. **LLM (Llama-2)** takes retrieved documents as context and generates an accurate response.
5. **Response is displayed** back to the user.

---

## 📌 Technologies Used

- **Langchain**
- **Pinecone VectorDB (vector database)**
- **Quantized Llama-2 LLM**
- **Flask (or FastAPI)** for serving webapp
- **HTML + CSS** for frontend

---

## 📈 Future Improvements

- Add user authentication.
- Track chat history.
- Improve vector store management.
- Deploy to cloud (AWS, GCP, Azure, etc.)

---
