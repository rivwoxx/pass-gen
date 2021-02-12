import string
import random

letters = string.ascii_letters
numbs = string.digits
special_c = string.punctuation

def gen_pass(length):
    '''
    
    '''
    if length <= 8:
        pswd="Lenght must be longer than 8"
    else:
        strg = f'{letters}{numbs}{special_c}'

        strg = list(strg)       #convert string into list then shuffle
        random.shuffle(strg)

        pswd = random.choices(strg, k=length)
        pswd = ''.join(pswd)
    return pswd

def pass_length():
    ''' 
    Get the length of the password we want to create.
    '''
    while True:
        try:
            length = int(input("Password Length: "))
            return length
        except ValueError:
            print('Password Lenght must be a number! ')

password = gen_pass(pass_length())
print(password)


