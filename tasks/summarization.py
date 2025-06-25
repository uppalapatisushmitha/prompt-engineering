# tasks/summarization.py

import google.generativeai as genai
from prompt_generator import generate_prompt


model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_text(text: str) -> str:
    prompt = generate_prompt(text, "Summarize this text.")
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
