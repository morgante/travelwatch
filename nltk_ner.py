import nltk, string

def extract_entities(text):
    good_types = ['GPE', 'LOCATION']
    locs = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node') and string.upper(chunk.node) in good_types:
                loc_name = ' '.join(c[0] for c in chunk.leaves())
                print loc_name
                locs.append(loc_name)

