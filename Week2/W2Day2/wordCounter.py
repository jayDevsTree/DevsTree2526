def wordCounter():
    sentence = input("Enter a Sentence:")
    wordCount= {}
    
    if sentence == "".strip():
        return
    else:
        for word in sentence.split():
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
        print(wordCount)
wordCounter()