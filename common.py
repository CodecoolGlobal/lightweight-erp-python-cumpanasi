""" Common module
implement commonly used functions here
"""

import random
import data_manager
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
                if lst[j][1] < lst[min_index][1]:
                    min_index = j
            elif order == 'desc':
                if lst[j][1] > lst[min_index][1]:
                    min_index = j        
        lst[i],lst[min_index] = lst[min_index],lst[i] 
    return lst


def check_for_key(key, table):

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

def check_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False  


def check_month(possible_month):
    if check_empty(possible_month) == False:
        print('Input can\'t be empty')
        return False
    else:
        if check_age(possible_month) == False:
            print('Unparsable Datatype!')
            return False
        else:
            month_number = check_age(possible_month)
            if month_number > 12 or month_number < 1:
                print('Month Value is out of bounds.')
                return False
            else:
                return True              

def check_day(possible_day, months, month):
    if check_empty(possible_day) == False:
        print('Input can\'t be empty')
        return False
    else:
        if check_age(possible_day) == False:
            print('Unparsable Datatype!')
            return False
        else:
            day_number = check_age(possible_day) 
            if day_number > months[month] or day_number > months[month]:
                print('Day value is out of bounds. PLease insert a value in the range 1 - {}.'.format(months[month]))
                return False
            else:
                return True        


def return_table(filename):
    table = data_manager.get_table_from_file(filename)

    return table

def check_empty_table(table):
    if len(table) == 0:
        return True
    else:
        return False    


def flip_dates(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return True
    elif year1 == year2:
        if month1 > month2:
            return True
        elif month1 == month2:
            if day1 > day2:
                return True
            else:
                return False
        else:
            return False                       
    else:
        return False      
    return None 

def date_in_between(year, month, day, year1, month1, day1, year2, month2, day2):
    if year > year1 and year < year2:
        return True
    elif year == year1 and year1 == year2:
        if month > month1 and month < month2:
            return True
        elif month == month1:
            if day >= day1:
                return True
            else:
                return False
        elif month == month2:
            if day <= day2:
                return True
            else:
                return False
        elif month1 == month2:
            if day >= day1 and day <= day2:
                return True
            else:
                return False
        elif month < month1 or month > month2:
            return False
    elif year == year1 and year1 != year2:
        if month > month1:
            return True
        elif month == month1:
            if day >= day1:
                return True
            else:
                return False    
        else:
            return False
    elif year == year2 and year1 != year2:
        if month < month2:
            return True
        elif month == month2:
            if day <= day2:
                return True 
            else: 
                return False
        else:
            return False                                                  
    else:
        return False                  


'''
year1 = 2004
month1 = 4
day1 = 27

year2 = 2004
month2 = 6
day2 = 5


print(date_in_between(2004, 5, 10,year1,month1,day1,year2,month2,day2))
print(date_in_between(2040, 5, 10,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,4,28,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,6,4,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,8,4,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,2,4,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,4,23,year1,month1,day1,year2,month2,day2))
print(date_in_between(2004,6,7,year1,month1,day1,year2,month2,day2))

year1 = 2002
month1 = 4
day1 = 27

year2 = 2007
month2 = 4
day2 = 27


print('\n'*3)
print(date_in_between(2004, 5, 10,year1,month1,day1,year2,month2,day2))


year1 = 2004
month1 = 4
day1 = 27

year2 = 2007
month2 = 4
day2 = 27

print(date_in_between(2004, 5, 10,year1,month1,day1,year2,month2,day2))
print(date_in_between(2007, 5, 27,year1,month1,day1,year2,month2,day2))
'''


def print_list_in_list(result):
    for elem in range(len(result)):
        if elem == len(result)-1:
            print(result[elem], end=" ")
        else:
            print(result[elem], end=", ")


def patriotism():
    RESET = '\033[0m'

    len = 27
    j = 0
    while j < 4:
        for i in range(27):
            if i < 9:
                print('\033[1;31;41m ', end ='')
            elif i >= 9 and i < 18:
                print('\033[1;33;43m ', end = '')
            elif i >= 18 and i < 27:
                print('\033[1;34;44m ', end = '')
        print(RESET)        
        j += 1
    print('\033[1;31;40mLa', end = ' ')
    print('\033[1;33;40mmulti', end = ' ')
    print('\033[1;34;40mani,', end = ' ')  
    print('\033[1;31;40mRO', end = '')
    print('\033[1;33;40mMAN', end = '')
    print('\033[1;34;40mIA!', end = '')   
    print(RESET)