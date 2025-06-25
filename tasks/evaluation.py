from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def evaluate_rouge_bleu(input_text, generated_text):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    rouge_l = scorer.score(input_text, generated_text)['rougeL'].fmeasure
    smoothie = SmoothingFunction().method4
    reference_tokens = [input_text.split()]
    generated_tokens = generated_text.split()
    bleu = sentence_bleu(reference_tokens, generated_tokens, smoothing_function=smoothie)
    return round(rouge_l, 4), round(bleu, 4)