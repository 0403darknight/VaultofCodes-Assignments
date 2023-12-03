def count(words):
    if words[-1] == '.':
        words = words[0:len(words) -1]
        if words in dict:
            dict[words] += 1
        else:
            dict.update({words: 1})
sentence = "After all this time always, good things can happen to you if you lower your expections"
dict = {}
lst = sentence.split()
for words in lst:
    count(words)
for allKeys in dict:
    print("Frequency of", allKeys, end = " ")
    print(":",end = " ")
    print(dict[allKeys],end = " ")
    print()


