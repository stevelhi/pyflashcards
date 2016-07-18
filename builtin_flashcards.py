import os
import random


def return_dirs(func):
    varlist = dir(func)
    errors = [i for i in varlist if i.endswith('Error')]
    builtins = [i for i in varlist if i.islower() and not i.startswith('__')]
    privates = [i for i in varlist if i.startswith('__')]
    specials = [i for i in varlist if i.istitle() and not i.startswith('__')]
    return errors, builtins, privates, specials


errors, builtins, privates, specials = return_dirs(__builtins__)

switcher = {
    1: (errors, 'errors'),
    2: (builtins, 'builtins'),
    3: (privates, 'privates'),
    4: (specials, 'specials')
}

i = 5
for b in builtins:
    print(b)
    __, methods, __, __, = return_dirs(eval(b))
    if methods:
        switcher[i] = ([b + '.' +  m for m in methods], str(b))
        print(methods)
    i +=1


print("which flashcard set would you like?")
for k, v in switcher.items():
    print("input %d for the '%s' flashcard set" % (k, v[1]))
usertext = int(input('enter selection and press Enter:\n'))

cards = switcher[usertext][0]
    
while True:
    os.system('clear')
    i = random.randint(0, len(cards)-1)
    print(cards[i], '\n')
    usertext = input('What is the definition? press Enter to continue')
    print('\n', eval(cards[i]).__doc__, '\n\n')
    usertext = input('press Enter to continue')
