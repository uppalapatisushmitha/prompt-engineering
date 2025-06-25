import google.generativeai as genai
from prompt_generator import generate_prompt


model = genai.GenerativeModel("gemini-1.5-flash")

def generate_code(prompt: str, language: str) -> str:
    full_prompt = (
        f"You are a coding assistant. Generate a single clean, working {language} code snippet "
        f"for the following requirement, without explanation or multiple options.\n\n"
        f"Requirement:\n{prompt}\n\n"
        f"Code only:"
    )
    try:
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f" ❌ Error: {str(e)}"
