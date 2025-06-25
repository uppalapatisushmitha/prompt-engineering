from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


def evaluate_rouge(reference: str, prediction: str) -> dict:
    """
    Compute ROUGE scores between the reference and predicted text.
    Returns ROUGE-1, ROUGE-2, and ROUGE-L F1 scores.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, prediction)
    
    return {
        'ROUGE-1': round(scores['rouge1'].fmeasure, 4),
        'ROUGE-2': round(scores['rouge2'].fmeasure, 4),
        'ROUGE-L': round(scores['rougeL'].fmeasure, 4)
    }


def evaluate_bleu(reference: str, prediction: str) -> float:
    """
    Compute BLEU score between reference and predicted text.
    """
    reference_tokens = reference.split()
    prediction_tokens = prediction.split()
    smoothie = SmoothingFunction().method4

    score = sentence_bleu([reference_tokens], prediction_tokens, smoothing_function=smoothie)
    return round(score, 4)


# Example usage for testing
if __name__ == "__main__":
    reference = "The quick brown fox jumps over the lazy dog"
    prediction = "A quick brown fox jumps over a lazy dog"

    print("ROUGE:", evaluate_rouge(reference, prediction))
    print("BLEU:", evaluate_bleu(reference, prediction))