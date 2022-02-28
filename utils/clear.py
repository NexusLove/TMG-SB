import os

def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return