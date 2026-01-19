def token_features(token, part_of_speech):
  if token.isdigit();
  yield "numeric"
else: 
yield "token={}". format(token.lower())
yield"token, pos={},{}". format(token,part_of_speech)
if token[0].isupper():
  yield "all_uppercase"
  yield "all_uppercase"
  yield "pos={}".format(part_of_speech)

raw_X = (token_features(tok, pos_tagger(tok)) for tok in corpus) 
hasher = FeatureHasher(input_type='string')
x = hasher.transform(raw_x)

#Document 1 : "Ich lerne Deutsch"
#Dokument 2 : "Ich lerne NLP" 

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectoriter()

documents = [
  "Ich lerne Deutsch", 
  "Ich lerne NLP"
]
x = vectorizer.fit_tranform(documents)

