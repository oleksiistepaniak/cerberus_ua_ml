import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^а-яА-ЯёЁa-zA-Zїієґ']", " ", text)
    return text.strip()
