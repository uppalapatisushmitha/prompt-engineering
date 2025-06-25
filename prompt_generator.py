# prompt_generator.py

def generate_prompt(context: str, question: str) -> str:
    """
    Format a general-purpose prompt using context and question.
    """
    return f"""Given the context below, answer the question:

Context:
{context}

Question:
{question}

Answer:"""
