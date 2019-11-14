""" User Interface (UI) module """
import common

CHECK_NUMS = ['Year', 'Amount','Age']
FIRST_ELEM = 0
def print_table(table, title_list):
    """
    Prints table with data.

    Example:
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
    longest_elements = []
    longest_elements_sum = 0
    longest_element_in_one_pillar = 0
    index = 0
    while index < len(title_list):
        for game in table:
            if len(game[index]) > longest_element_in_one_pillar:
                longest_element_in_one_pillar = len(game[index])
        if len(title_list[index]) > longest_element_in_one_pillar:
            longest_element_in_one_pillar = len(title_list[index])
        longest_elements.append(longest_element_in_one_pillar)
        longest_element_in_one_pillar = 0
        index += 1
    for element in longest_elements:
        longest_elements_sum += element
    first_line_settlement = "/" +"{" + "0:-^" +str(longest_elements_sum+len(title_list)-2)+"}" + " \\"
    print(first_line_settlement.format(""))
    for titles in range(len(title_list)):
        title_line_settlement = "|" +"{" + "0:^" +str(longest_elements[titles])+"}"
        print(title_line_settlement.format(title_list[titles]),end = "")
    print("|")
    for elements in table:
        for element in range(len(elements)):
            empty_line_settlement = "|" +"{" + "0:-^" +str(longest_elements[element])+"}"
            print(empty_line_settlement.format(""),end = "")
        print("|")
        for element in range(len(elements)):
            element_line_settlement = "|" +"{" + "0:^" +str(longest_elements[element])+"}"
            print(element_line_settlement.format(elements[element]),end = "")
        print("|")
    last_line_settlement = "\\" +"{" + "0:-^" +str(longest_elements_sum+len(title_list)-2)+"}" + " /"
    print(last_line_settlement.format(""))



    


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    if label != '':
        print(label)
    if type(result) == list:
        if type(result[FIRST_ELEM]) == list:
            pass
        else:
            for elem in range(len(result)):
                if elem == len(result)-1:
                    print(result[elem], end = " ")
                else:
                    print(result[elem], end = ", ")  
    elif type(result) == dict:
        for key in result.keys():
            print('{}:{}'.format(key,result[key]))




    print('\n')  
    # your code


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
    print(f'\n\t{title}\n')
    for index, val in enumerate(list_options):
        print(f'({index + 1}) {val}')
    print(f'(0) {exit_message}')
    # your code


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

        else:
            possible_string = input('{} '.format(elem))
            while common.check_empty(possible_string) == False:
                print('This string can\'t be empty!')
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
    print(f'{message} !')
    # your code
