import random

word_list = ['python', 'hangman', 'programming', 'computer', 'challenge', 'knowledge', 'development', 'learning']
secret_word = random.choice(word_list)
guesses = ''
turns = 10

while True:
    while turns > 0:
        missed = 0
        for letter in secret_word:
            if letter in guesses:
                print(letter, end='')
            else:
                print('-', end='')
                missed += 1

        if missed == 0:
            print('\n Congrats! You Won!')
            ans = input("Play again Y/N?")
            if ans.upper() == 'Y':
                secret_word = random.choice(word_list)
                guesses = ''
                turns = 10
                break
            else:
                exit()

        guess = input('\n Guess a letter:')
        guesses += guess

        if guess not in secret_word:
            turns -= 1
            print('Try again!')
            print('You have', turns, 'more guesses')

        if turns == 0:
            print('Game over, your word was:', secret_word)
            ans = input("Play again Y/N?")
            if ans.upper() == 'Y':
                secret_word = random.choice(word_list)
                guesses = ''
                turns = 10
                break
            else:
                exit()
