import re

def estimate_level_grammar(text: str) -> str:
    text_lower = text.lower()

    score = 0

    # Nebensätze
    if re.search(r"\b(dass|weil|obwohl|während|wenn)\b", text_lower):
        score += 2

    # Relativsätze
    if re.search(r"\b(der|die|das|welche|welcher)\b", text_lower):
        score += 2

    # Passiv
    if re.search(r"\b(wird|wurden|worden)\b", text_lower):
        score += 2

    # C1-Konnektoren
    if re.search(r"\b(dennoch|hingegen|somit|folglich)\b", text_lower):
        score += 3

    # Satzlänge
    if len(text.split()) > 20:
        score += 1

    if score <= 2:
        return "B1"
    elif score <= 5:
        return "B2"
    else:
        return "C1"

