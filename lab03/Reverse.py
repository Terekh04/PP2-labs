def reversedSentence(sentence):
    reversed=[]
    ans=""
    for i in sentence.split():
        reversed.append(i)
    for i in reversed[::-1]:
        ans+=i
        ans+=" "
    print(ans)
    return