#given a string, returns a list of word frequencies
#call as: wf=get_frequency(string)
#and normalize as: wf=normalize(wf)

def add(w1,w2):
    return dict( (n, wf1.get(n, 0)+wf2.get(n, 0)) for n in set(wf1)|set(wf2) )

def normalize(wf):
    total=0.
    for key in wf.keys():
	total+=wf[key]
    for key in wf.keys():
	wf[key]=wf[key]/total
    return wf


def get_frequency(input_string):
    from collections import Counter
    from collections import defaultdict
    #get rid of non char
    par_str=''.join(e for e in input_string if (e.isalpha() or e == " ")).lower()
    words=par_str.split()
    frequency = Counter(words).items()
    d=defaultdict(list)
    for k,v in frequency:
	d[k]=v
    return d

if __name__ == "__main__":
    inputstr="tHis7 is a \t\nlong 8    th6is string of Things tHIngs strinG this string long times and is blah;'. Some random This TIME;"
    print inputstr
    print get_frequency(inputstr)

