# Agentic RAG Chatbot (Multi-Format + MCP Protocol)

A Retrieval-Augmented Generation (RAG) chatbot powered by **agent-based architecture** and **Model Context Protocol (MCP)**. It lets users upload documents (PDF, DOCX, PPTX, TXT, CSV), ask questions, and get LLM-powered answers with cited sources.

##  Features

-  **Multi-Format Document Uploads**: Supports PDF, PPTX, DOCX, CSV, TXT/Markdown
-  **Agent-Based Architecture**:
  - `IngestionAgent`: Parses + chunks files
  - `RetrievalAgent`: Uses Hugging Face + FAISS for retrieval
  - `LLMResponseAgent`: Generates answers with context
  - `CoordinatorAgent`: Controls the workflow
-  **MCP Protocol**: Structured in-memory messaging between agents
-  **Semantic Search**: Hugging Face SentenceTransformer + FAISS
-  **Interactive Chat UI**: Built with Streamlit

---

## ⚙️ Tech Stack

| Component      | Tool/Library                         |
|----------------|--------------------------------------|
| UI             | Streamlit                            |
| Embeddings     | SentenceTransformer (`all-MiniLM-L6-v2`) |
| Vector Store   | FAISS                                |
| Document Parsing | PyPDF2, python-docx, python-pptx   |
| Agent Protocol | Model Context Protocol (MCP - custom)|
| Language Model |  HuggingFace         |

---

###Getting Started

### 1. Clone the Repo

bash
git clone https://github.com/your-username/agentic_rag_bot.git
cd agentic_rag_bot
###2. Create a virtual Environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
###3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
###4. Run
Run the App
bash
Copy
Edit
streamlit run app/streamlit_app.py

### Structure

agentic_rag_bot/
├── app/
│   ├── agents/
│   │   ├── ingestion_agent.py
│   │   ├── retrieval_agent.py
│   │   ├── llm_response_agent.py
│   │   └── coordinator_agent.py
│   ├── mcp/
│   │   └── protocol.py
│   ├── utils/
│   │   └── parsers.py
│   ├── store/
│   │   └── vector_store.py
│   └── streamlit_app.py
├── requirements.txt
└── README.md
