# agents/retrieval_agent.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.chunks = []

    def index_docs(self, full_text):
        self.chunks = [full_text[i:i + 500] for i in range(0, len(full_text), 500)]
        embeddings = self.model.encode(self.chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def retrieve(self, query, k=3):
        if not self.index or not self.chunks:
            return []

        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.chunks[i] for i in indices[0]]
