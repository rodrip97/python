# just random exercises from the book and re reading some sections for practice
""" print('What is your name?')
myName = input()
print('Hello,', myName)
print('Your name is:',len(myName), 'characters long') """


# While Statement example. Condition is input == your name
""" name = ""
while name != 'your name':
    print('Please type your name')
    name = input()
print('Took you a while to figure it out uh dumbass') """

#loops

""" for i in range(5):
    print('Count:', i + 1)

i = 0
while (i < 5):
    print('Count 2:', i + 1)
    i = i + 1 
total = 0 

for num in range(101):
    total = total + num
print(total)"""
""" import random

for i in range(5):
    print(random.randint(1, 10)) """

# guess the number exercise

""" import random

guess_number = random.randint(1, 10)
guess = ''

print('Try to guess the number between 1 and 10:')
while True:
    guess = int(input())  

    if guess < guess_number:
        print('Try Again. Your guess is too low.')
    elif guess > guess_number:
        print('Try Again. Your guess is too high.')
    else:
        print('You got it!!')
        break  """

""" import time, sys
indent = 0

indentIncreasing = True 
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.3)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit() """


""" data = ['1','2','3','4','5','6','7']

for i in data:
    print(i)
 """

""" catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  
print('The cat names are:')
for name in catNames:
    print('  ' + name) """


#supplies = ['pens', 'pencils','scissors','rubber','flamethrower','dildo',]

""" for i in range(len(supplies)):
    print('Item: ' + str(i + 1 ) + ' in supplies is: ' + supplies[i]) """
# same thing but using enumerate rather than range

""" for index, item in enumerate(supplies):
    print('Item #' + str(index+1) + ' in supplies is: ' + item) """

""" import random
supplies = ['pens', 'pencils','scissors','rubber','flamethrower','dildo',]

for i in range(3):
    print(random.choice(supplies)) """

# magic ball game

""" import random

messages = [
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(messages[random.randint(0, len(messages)-1)]) """
""" 
list1 = ['items', 'dildos']
list2 = list1
list2[1] = "spam"

print(list1)
print(list2)

 """


""" ### Roman Numerals
def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for symbol in s:
        current_value = roman_dict[symbol]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    
    return total


print(romanToInt("I"))
print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("VIII"))
print(romanToInt("XIII"))

 """

###################################################################################
#################### Pattern Matching With Regular Expressions ####################
###################################################################################
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
        
    return True


print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))