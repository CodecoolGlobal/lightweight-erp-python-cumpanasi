""" Common module
implement commonly used functions here
"""

import random
TABLE_KEY = 0
FIRST_CHAR = 0

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    def generate_based_on_pattern():
        digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lower_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        final_symbols = '#&'

        return lower_list[random.randint(0,len(lower_list)-1)] + upper_list[random.randint(0,len(upper_list)-1)] +  digit_list[random.randint(0,len(digit_list)-1)] +  digit_list[random.randint(0,len(digit_list)-1)] + upper_list[random.randint(0,len(upper_list)-1)] + lower_list[random.randint(0,len(lower_list)-1)] + final_symbols

    generated = generate_based_on_pattern()

    #generated = ['kH34Ju#&', 'sG79Ti#&'] #, 'fC47Pb#&', 'rM49Oh#&']

    #generated = generated[random.randint(0,len(generated)-1)]
    duplicate = False

    for sublist in range(len(table)):
        if generated == table[sublist][TABLE_KEY]:
            #print('duplicate')
            duplicate = True

    if duplicate == False:
        return generated

    elif duplicate == True:
        return generate_random(table)


print(generate_random([['kH14Ju#&', '1', '21', '2016', 'in', '31']]))


def check_age(string):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    if string[FIRST_CHAR] == '0':
        return False
    for char in string:
        if char not in digits:
            return False
    return int(string) 

def sort_me (lst, order = 'asc'):

    if len(order) > 0:
        if order not in ['asc','desc']:
            order = 'asc'
    
    for i in range(len(lst)):

        min_index = i 

        for j in range(i+1, len(lst)):
            if order == 'asc':
                if lst[j] < lst[min_index]:
                    min_index = j
            elif order == 'desc':
                if lst[j] > lst[min_index]:
                    min_index = j        
        lst[i],lst[min_index] = lst[min_index],lst[i] 
    return lst


def check_for_key(key,table):

    for record in range(len(table)):
        if str(key) == str(table[record][TABLE_KEY]):
            return record
    return None        


def check_empty(value):
    
    if value == '':
        return False
    return True     

    # your code

    return generated
