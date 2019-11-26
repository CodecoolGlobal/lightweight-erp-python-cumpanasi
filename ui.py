""" User Interface (UI) module """
import common

CHECK_NUMS = ['Year', 'Amount','Age']
CHECK_EMAIL = ['Mail']
BINARY_FIELDS = ['Subscribed']
FIRST_ELEM = 0


def print_table(table, title_list):
    """
    Prints table with data.

    Example:git
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    cols = len(title_list)

    

    table.insert(0,title_list)

    for sublist in range(len(table)):
        if cols != len(table[sublist]):
            print('dataset does not match number of cols')
            quit()

    max_lenghts = []
    maxi = -1
    for sub_elem in range(cols):  
        maxi = -1  
        for sublist in range(len(table)):
            if len(table[sublist][sub_elem]) > maxi:
                maxi = len(table[sublist][sub_elem])
        max_lenghts.append(maxi)
    

    

    sub_elem = 0
    
    for sublist in range(len(table)):
        if sublist == 0:
            while sub_elem < len(table[0]):
                
                if sub_elem == len(table[0])- 1:
                    print('\033[1;37;41m| {:^25} |'.format(table[sublist][sub_elem]), end ="")
                else:
                    print('\033[1;37;41m| {:^25} '.format(table[sublist][sub_elem]), end ="")
                sub_elem += 1
        
            print('\033[0;32;48m\n') 
            sub_elem = 0 
        else:
            while sub_elem < len(table[0]):
                
                if sub_elem == len(table[0])- 1:
                    print('\033[0;37;44m| {:^25} |'.format(table[sublist][sub_elem]), end ="")
                else:
                    print('\033[0;37;44m| {:^25} '.format(table[sublist][sub_elem]), end ="")
                sub_elem += 1
            
            print('\033[0;32;48m\n') 
            sub_elem = 0          
    print('\033[0;37;48m\n')
    table.pop(0)


def print_result_inventory(result, label):
    print(f"{result} {label}")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    if label != '':
        print(label)
    if type(result) == list:
        if type(result[FIRST_ELEM]) == list:
            pass
        else:
            for elem in range(len(result)):
                if elem == len(result)-1:
                    print(result[elem], end=" ")
                else:
                    print(result[elem], end=", ")  
    elif type(result) == dict:
        for key in result.keys():
            if type(result[key]) == list:
                print('{key}: '.format(key = key), end = '')
                for elem in range(len(result[key])):
                    if elem == len(result[key])-1:
                        print(result[key][elem], end=" ")
                    else:
                        print(result[key][elem], end=", ")
                print('\n')        
            else:
                print('{}:{}'.format(key, result[key]))
    print('\n')



def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(f'\n\t{title}\n')
    for index, val in enumerate(list_options):
        print(f'({index + 1}) {val}')
    print(f'(0) {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    if len(title) > 0:
        print(title)
    for elem in list_labels:

        if elem in CHECK_NUMS:
            possible_int = input('{} '.format(elem))
            while common.check_empty(possible_int) == False or common.check_age(possible_int) == False:
                print('value {} for {} is not a valid number type.'.format(possible_int, elem.lower()))
                possible_int = input('{} '.format(elem))
            inputs.append(possible_int)   

        elif elem in CHECK_EMAIL:
            possible_mail = input('{} '.format(elem))
            while common.check_empty(possible_mail) == False or common.check_email(possible_mail) == False:
                print_error_message('Not a valid mail')
                possible_mail = input('{} '.format(elem))
            inputs.append(possible_mail)

        elif elem in BINARY_FIELDS:
            possible_binary = input('{} '.format(elem))
            while common.check_empty(possible_binary) == False or common.check_binary(possible_binary) == False:
                print_error_message('Not a valid binary field')
                possible_binary = input('{} '.format(elem))
            inputs.append(possible_binary)

        else:
            possible_string = input('{} '.format(elem))
            while common.check_empty(possible_string) == False:
                print_error_message('This string can\'t be empty')
                possible_string = input('{} '.format(elem))
            inputs.append(possible_string)

    return inputs

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(f'{message} !')
