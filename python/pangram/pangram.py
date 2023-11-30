def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    abset = set()
    for element in enumerate(sentence):
        char = element[1]
        if char.lower() in alphabet:
            abset.add(char.lower())
    print(abset, len(abset))
    return len(abset) == 26
