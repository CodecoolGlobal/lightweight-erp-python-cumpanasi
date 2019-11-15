""" Common module
implement commonly used functions here
"""

import random
TABLE_KEY = 0
FIRST_CHAR = 0

FIRST_HALF = 0
SECOND_HALF = 1


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
   



    # your code

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


#print(generate_random([['kH14Ju#&', '1', '21', '2016', 'in', '31']]))


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


def check_email(mail):

    prohibited = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-','/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
    domains = ['.com', '.co.uk', '.tv' , '.ro', '.hu']
    dot = '.'
    dot2 = '..'
    double_underline = '__'



    count_at = 0
    



    for char in mail:
        if char == '@':
            count_at += 1


    if count_at != 1:
        return False 

    elif count_at == 1:
        mail_half = mail.split('@')

    mail_half[FIRST_HALF] = mail_half[FIRST_HALF].replace(" ",'')
    mail_half[SECOND_HALF] = mail_half[SECOND_HALF].replace(' ', '')    

    for symbol in prohibited:
        if symbol in mail_half[FIRST_HALF]:
          return  False

    if mail_half[FIRST_HALF].find(dot2) != -1:
       return False

    if mail_half[FIRST_HALF].find(double_underline) != -1:
       return False

    if mail_half[FIRST_HALF].startswith(dot) != False or mail_half[FIRST_HALF].endswith(dot) != False:
        return False


    found_domain = False
    for domain in domains:
        if mail_half[SECOND_HALF].endswith(domain):
            domain_start = mail_half[SECOND_HALF].find(domain)
            found_domain = True

    if found_domain == False:
       return False

    provider = mail_half[SECOND_HALF][0:domain_start+1]

    if provider.startswith(dot) != False:
        return False

    for symbol in prohibited:
        if symbol in provider:
            return False

    if mail_half[SECOND_HALF].find(dot2) != -1:
       return False

    if mail_half[SECOND_HALF].find(dot2) != -1:
       return False

    return mail_half[FIRST_HALF] + '@' + mail_half[SECOND_HALF]   



def check_binary(number):

    if number != '0' and number !='1':
        return False
    return True    

