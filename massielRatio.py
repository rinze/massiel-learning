def massielRatio(dataInput):
    words = 0 # All the words in the document
    la = 0 # 'la'

    for line in dataInput:
        if not line.startswith('#'):
            tk = line.lower().split()
            tk = [filter(str.isalpha, x) for x in tk]
            words += len(tk)
            la += sum(map(lambda x : x == "la", tk))
            # 'la' is sometimes also codified as 'lalala'
            la += 3 * sum(map(lambda x : x == "lalala", tk))

    return [words, la]
