from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load model only once
model_name = "prithivida/grammar_error_correcter_v1"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def correct_grammar(text: str) -> str:
    """Corrects grammar of a given sentence or paragraph."""
    if not text.strip():
        return ""

    input_text = "gec: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(
        inputs,
        max_length=512,
        num_beams=5,
        early_stopping=True
    )

    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text
