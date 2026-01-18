    
from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        model_name = "Helsinki-NLP/opus-mt-en-de"
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        output = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return output


translator = Translator()

def translate(text):
    return translator.translate(text)
