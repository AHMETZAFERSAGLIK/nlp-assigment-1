import spacy

# Implement linguistic analyses using spacy
# Run them on data/preprocessed/train/sentences.txt
f = open("intro2nlp_assignment1_code/data/preprocessed/test/sentences.txt","r")
context=f.read()
nlp = spacy.load("en_core_web_sm")
number_of_token=len(nlp(context))
print("number of token is = ",number_of_token)

number_of_types=nlp.get_pipe("ner").labels
print(len(number_of_types))