#histogram function
def histogram(list1):
    for i in list1:
        print('*'*i)
    return
histogram([4,9,5])
print()
#****
#*********
#*****
histogram([10,5,7,1,24,3])
print()
#**********
#*****
#*******
#*
#************************
#***
histogram([1,11,111])
#*
#***********
#***************************************************************************************************************



#spy function
def spy_game(nums):
    num=''
    for i in nums:
        if i==0 or i==7:
            num+=str(i)
    if '007' in num:
        print('True')
        return
    else:
        print('False')
        return

spy_game([8,12,0,12,23,0,3235,980,90,8765,678,98,7654,7,56,7890]) #True



#reverse function
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
reversedSentence('I like mangos') #mangos like I
reversedSentence('Je ne parle pas français') #français pas parle ne Je
reversedSentence('Съешь ещё этих мягких французских булок, да выпей чаю') #чаю выпей да булок, французских мягких этих ещё Съешь
