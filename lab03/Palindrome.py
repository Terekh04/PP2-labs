import re
def palOrNot(word):
    word1=re.sub(fr'[^a-zA-z]','', word)
    word1=word1.lower()
    if word1==word1[::-1]:
        print(f'Yes, "{word}" is palindrome')
        return
    else:
        print(f'No, "{word}" is not a palindrome')
        return
palOrNot('Was it a Cat I Saw?')
#r for regular expression