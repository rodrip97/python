import random


word_list = ['python', 'hangman', 'programming', 'computer', 'challenge', 'knowledge', 'development', 'learning']
secret_word = random.choice(word_list)
guesses = ''
turns = 10


while turns > 0 :
    missed = 0
    for letter in secret_word:
        if letter in guesses:
            print(letter, end='')
        else: 
            print('-', end='')
            missed += 1
    
    if missed == 0:
        print('\n Congrats! You Won!')
        break
    
    guess = input('\n Guess a letter:')
    guesses += guess

    if guess not in secret_word:
        turns -= 1
        print('Try again!')
    if turns == 0:
        print('Game over, your word was:', secret_word)

