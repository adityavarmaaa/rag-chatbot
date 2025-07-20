# agents/llm_response_agent.py

from transformers import pipeline

# Load a lightweight question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def generate_response(context_chunks, query):
    if not context_chunks:
        return "No relevant context was found in the documents."

    # Combine retrieved chunks into a single context block
    context = "\n".join(context_chunks)

    # Debug logs (optional)
    print("[Debug] Context snippet:")
    print(context[:1000])
    print("[Debug] Query:", query)

    # Attempt QA with the model
    result = qa_pipeline({
        'question': query,
        'context': context
    })

    print("[Debug] Raw QA model output:", result)

    # Use score threshold to handle uncertain answers
    if result['score'] < 0.3:
        # Attempt rule-based fallback for structured documents like certificates
        lines = context.strip().splitlines()
        if len(lines) >= 2:
            probable_title = lines[1].strip()
            return f"Based on document structure, the certificate appears to be in: {probable_title}"
        return "The system could not confidently determine an answer from the available information."

    # Return the model-generated answer
    return result.get('answer', 'No answer could be extracted.')
