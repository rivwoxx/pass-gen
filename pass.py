import string
import random

letters = string.ascii_letters
numbs = string.digits
special_c = string.punctuation

def gen_pass(length):
    '''
    
    '''
    # if type(length) != int:
    #     pswd="Length must be a Number"
        
    # elif length <= 8:
    #     pswd="Must be longer than 8"
    if length <= 8:
        pswd="Must be longer than 8"
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
            print('error')
    # try:
    #     length = int(length)
    #     return length
    # except ValueError: 
    #     return length
    # return length

pass_len = pass_length()
password = gen_pass(pass_len)
print(password)


