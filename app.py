# app.py

import streamlit as st
from agents import ingestion_agent, retrieval_agent, llm_response_agent
from utils.mcp import create_message
import uuid
import tempfile

st.set_page_config(page_title="Document QA Chatbot", layout="wide")
st.title("Document Question-Answering Chatbot")

# Upload section
uploaded_files = st.file_uploader("Upload one or more documents", type=["pdf", "docx", "pptx", "csv", "txt", "md"], accept_multiple_files=True)
query = st.text_input("Enter your question")

if uploaded_files and query:
    st.divider()
    st.subheader("Parsing uploaded documents")

    full_text = ""
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.name) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        text = ingestion_agent.parse_text(tmp_path)
        full_text += text + "\n"

    st.markdown("Preview of parsed content:")
    if full_text.strip():
        st.text(full_text[:1000])
    else:
        st.warning("No text could be extracted from the documents.")

    # Run retrieval and QA
    if full_text.strip():
        st.subheader("Retrieving relevant information")
        retriever = retrieval_agent.RetrievalAgent()
        retriever.index_docs(full_text)
        top_chunks = retriever.retrieve(query)

        st.markdown("Top retrieved chunks:")
        for idx, chunk in enumerate(top_chunks):
            st.code(f"Chunk {idx + 1}:\n{chunk[:500]}", language="markdown")

        st.subheader("Generating answer")
        mcp_msg = create_message(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            msg_type="CONTEXT_RESPONSE",
            payload={
                "top_chunks": top_chunks,
                "query": query
            },
            trace_id=str(uuid.uuid4())
        )

        response = llm_response_agent.generate_response(
            mcp_msg['payload']['top_chunks'],
            mcp_msg['payload']['query']
        )

        st.markdown("Answer:")
        if response.strip():
            st.success(response)
        else:
            st.info("No answer could be generated from the content.")
