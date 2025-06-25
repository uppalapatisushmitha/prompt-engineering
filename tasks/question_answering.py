import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import google.generativeai as genai
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from file_reader import extract_text


genai.configure(api_key="AIzaSyCriSDR538wjeZnLjuNudJ55x6n8BmA-cI")
model = genai.GenerativeModel("gemini-1.5-flash")

def answer_question(file_content, question):
    content = file_content  # file is already the raw text
    prompt = f"Answer the following question based on the content below.\n\nContent:\n{content}\n\nQuestion: {question}\nAnswer:"
    response = model.generate_content(prompt)
    return response.text.strip()


def evaluate_output(generated):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    rouge_l = scorer.score(generated, generated)['rougeL'].fmeasure  # Self-comparison
    smoothie = SmoothingFunction().method4
    bleu = sentence_bleu([generated.split()], generated.split(), smoothing_function=smoothie)
    return round(rouge_l, 4), round(bleu, 4)