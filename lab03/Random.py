import random

def game(guess,number,name,guessNum):
    if guess==number:
        print(f'Good job, {name}! You guessed my number in {guessNum} guesses!')
        return True
    elif guess>number:
        print('Your guess is too high')
        return False
    else:
        print('Your guess is too low')
        return False
number=random.randint(1,20)
stop=False
name=input('Hello! What is your name?')
print(f'Well, {name}, I am thinking of a number between 1 and 20')
guess=int(input('Take a guess.'))
counter=0
while not stop:
    stop = game(guess, number, name, counter)  
    counter += 1 
    if stop:
        break
    guess = int(input('Take a guess.'))  