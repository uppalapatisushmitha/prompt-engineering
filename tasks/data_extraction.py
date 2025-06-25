# tasks/data_extraction.py

import google.generativeai as genai
from file_reader import extract_text


genai.configure(api_key="AIzaSyCriSDR538wjeZnLjuNudJ55x6n8BmA-cI")  # Replace with env var in production

model = genai.GenerativeModel("gemini-1.5-flash")

def extract_full_text(file) -> str:
    """
    Extract raw text from the uploaded file using file_reader.
    """
    return extract_text(file)

def extract_answer_from_text(full_text: str, question: str) -> str:
    """
    Given full extracted text and a question, return an answer using Gemini.
    """
    prompt = f"""Given the following content, answer the question:

Content:
{full_text}

Question: {question}

Answer:"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌  Gemini Error: {str(e)}"
