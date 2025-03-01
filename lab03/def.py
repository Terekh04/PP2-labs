def palindrome(word):
    word=word.lower()
    if word==word[::-1]:
        print('Your word is a palindrome')
        return
    else:
        print('Your word is not a palindrome')
        return

word=input('Input your word')
palindrome(word)