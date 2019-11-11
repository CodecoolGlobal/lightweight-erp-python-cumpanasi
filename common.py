""" Common module
implement commonly used functions here
"""
TABLE_KEY = 0
import random


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
    duplicate = False

    for sublist in range(len(table)):
        if generated == table[sublist][TABLE_KEY]:
            duplicate = True

    if duplicate == False:
        return generated

    elif duplicate == True:
        generate_random(table)


print(generate_random([['kH14Ju#&', '1', '21', '2016', 'in', '31']]))