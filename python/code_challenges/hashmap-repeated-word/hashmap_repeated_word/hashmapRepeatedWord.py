def splitWord(text):
    text = text.replace(','or ';' or '.', ' ')
            
    words = []
    wordList = text.split()
    for word in wordList:
        word = word.lower()
        words.append(word)
    return words

def repeatedWord(text):
    words = splitWord(text)
    for i in range(1,len(words)):
        # print(words[0:i])
        if words[i] in words[0:i]:
            # print(words[0:i])
            return words[i]

# text = "Once upon a time, there was a brave princess who..."

# print(splitWord(text))
# print(repeatedWord(text))