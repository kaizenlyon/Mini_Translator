import spacy

nlp = spacy.load("en_core_web_sm")

def explain(source: str, translation: str) -> str:
    doc = nlp(source)
    explanation = []

    # 1) Present Perfect
    for token in doc:
        if token.tag_ in ["VBN"] and any([t.lemma_ == "have" for t in token.head.lefts]):
            explanation.append(
                "Present Perfect im Englischen wird im Deutschen oft mit Präsens + 'seit' ausgedrückt."
            )
            break

    # 2) since / for
    if "since" in source.lower():
        explanation.append("„since“ wird im Deutschen meistens mit „seit“ übersetzt (Dauer seit einem Zeitpunkt).")
    if "for" in source.lower():
        explanation.append("„for“ wird im Deutschen oft mit „seit“ oder „für“ übersetzt (Dauer).")

    # 3) Modalverben
    if any(token.tag_ == "MD" for token in doc):
        explanation.append("Modalverben (can, must, should) werden im Deutschen meist als Modalverb + Infinitiv übersetzt.")

    # 4) Passiv (simple heuristic)
    if any(token.dep_ == "auxpass" for token in doc):
        explanation.append("Passiv wird im Deutschen oft mit 'werden' + Partizip II gebildet.")

    # Default explanation
    if not explanation:
        explanation.append("Dies ist eine allgemeine Übersetzung. Bei Bedarf kann ich spezifische Grammatik erklären.")

    return "\n".join(explanation)
