import random

while True:
    input('> ')
    a = random.randint(1, 6)
    print('\n - Disparado - \n')
    if a == 4:
        print('\n - morte - \n')
        break
    else:
        print('\n - ufa - \n')