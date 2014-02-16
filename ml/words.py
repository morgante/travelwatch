from collections import Counter
from collections import defaultdict

word_list = ['murder', 'violent', 'crime','murder and nonnegligent manslaughter','forcible rape','robbery','aggravated assault','property crime','burglary','larceny/theft','motor vehicle theft']

def frequencies(text):

	keywords = {word: 0 for word in word_list}

	par_str=''.join(e for e in text if (e.isalpha() or e == " ")).lower()
	words=par_str.split()

	frequencies = Counter(words).items()

	for (word, freq) in frequencies:
		if (word in keywords):
			keywords[word] += freq

	return keywords

def all():
	return list