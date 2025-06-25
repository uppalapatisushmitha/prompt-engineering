from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def evaluate_scores(reference: str, generated: str) -> dict:
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge = scorer.score(reference, generated)

    smooth = SmoothingFunction().method1
    bleu = sentence_bleu([reference.split()], generated.split(), smoothing_function=smooth)

    return {
        "ROUGE-1": round(rouge['rouge1'].fmeasure, 4),
        "ROUGE-L": round(rouge['rougeL'].fmeasure, 4),
        "BLEU": round(bleu, 4)
    }