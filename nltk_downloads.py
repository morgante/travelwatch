import nltk

packages = ['maxent_ne_chunker', 'punkt', 'words', 'maxent_treebank_pos_tagger']

def init():
    for p in packages:
        nltk.download(p)

init()
#extract_entities("Hi I'm staying in a hotel in Abu Dhabi, in the United Arab Emirates, and my name is Bonnie")

