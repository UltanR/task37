import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The old man the boat",
    "The horse raced past the barn fell",
    "The complex houses married and single soldiers and their families",
    "The man who hunts ducks out on weekends",
    "The Italian baker who makes great bread and pizza"
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Entities in '%s':" % sentence)
    for ent in doc.ents:
        print("  ", ent.text, ent.label_)


# In the first sentence, "The old man" was recognized as a person (PER).
# However, "the boat" was not recognized as an entity.
# In the second sentence, "the barn" was recognized as a location (LOC).
# However, "fell" was not recognized as an entity.

# All output:
'''Entities in 'The old man the boat':
   The old man PER
Entities in 'The horse raced past the barn fell':
   the barn LOC
Entities in 'The complex houses married and single soldiers and their families':
   married ORG
   single ORG
Entities in 'The man who hunts ducks out on weekends':
   The man PER
Entities in 'The Italian baker who makes great bread and pizza':
   Italian NORP'''
