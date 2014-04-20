import string
def massielRatio(dataInput):
    words = 0 # All the words in the document
    la = 0 # 'la'

    punct = set(string.punctuation)
    for line in dataInput:
        if not line.startswith('#'):
            tk = line.lower().split()
            tk = [filter(lambda x : ''.join(ch for ch in x if ch not in punct),\
                         x) for x in tk]
            words += len(tk)
            la += sum(map(lambda x : x == "la", tk))
            # 'la' is sometimes also codified as 'lalala'
            la += 3 * sum(map(lambda x : x == "lalala", tk))

    return float(la)/float(words)
