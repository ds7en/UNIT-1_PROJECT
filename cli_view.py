import os

def commandLine(message: str):
    os.system('clear')
    print(f"\n\t\t{message}\n")
    the_output = input(' > ')
    return the_output