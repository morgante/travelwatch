#given a string, returns a list of word frequencies

def get_frequency(input_string):
    from collections import Counter
    #get rid of non char
    par_str=''.join(e for e in input_string if (e.isalpha() or e == " ")).lower()
    words=par_str.split()
    frequency = Counter(words).items()
    return frequency

if __init__ == "__main__":
    inputstr="tHis7 is a \t\nlong 8    string of Things tHIngs strinG this string long times and is blah;'. Some random This TIME;"
    print inputstr
    print get_frequency(inputstr)

