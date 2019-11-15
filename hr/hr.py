""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FIRST_PROP = 0
KEY = 0
SECOND_PROP = 1
THIRD_PROP = 2
NAME = 1
AGE = 2

table = data_manager.get_table_from_file('hr/persons.csv')
titles = ['ID', 'Name', 'Birth Year']

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    title = "\nHuman Resources manager\n"
    list_option = ['Show Table', 'Add to table', 'Remove from Table via ID', 
    'Update record via ID', 'Get Oldest Person', 'Get closest to average']

    exit_message = "Go back to the main menu"
    while True:
        ui.print_menu(title, list_option, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            return_inputs = ui.get_inputs(['ID'],'Enter the key of the corresponding record you want removed.')
            remove(table,return_inputs[0])
        elif option == "4":
            return_inputs = ui.get_inputs(['ID'],'Enter the key of the corresponding record you want to update.')
            update(table,return_inputs[0])
        elif option == "5":
            print('\n')
            get_oldest_person(table)
        elif option == "6":
            print('\n')
            get_persons_closest_to_average(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code

    ui.print_table(table,titles)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    
    

    return_inputs = ui.get_inputs(['Name', 'Year'],"Please enter a new record.")
    key = str(common.generate_random(table))
    table.append([key,return_inputs[FIRST_PROP] , str(return_inputs[SECOND_PROP])])
    data_manager.write_table_to_file('hr/persons.csv', table)


    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    key = common.check_for_key(id_,table)

    if key == None:
         ui.print_error_message('Key does not exist')
    else:
        table.pop(key)
        data_manager.write_table_to_file('hr/persons.csv', table)    

    #print(table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    key = common.check_for_key(id_,table)
    if key == None:
         ui.print_error_message('Key does not exist')
    else:
        return_inputs = ui.get_inputs(['Name', 'Age'], 'Enter New Values')
        modif_index = key

        table[modif_index][NAME]  = return_inputs[FIRST_PROP]
        table[modif_index][AGE] = return_inputs[SECOND_PROP]
        data_manager.write_table_to_file('hr/persons.csv', table) 

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code

    oldest_age = int(table[FIRST_PROP][AGE])
    names = []
    for record in range(len(table)):
        if int(table[record][AGE]) < oldest_age:
            oldest_age = int(table[record][AGE])
    #print(oldest_age)
    for record in range(len(table)):
        if table[record][AGE] == str(oldest_age):
            names.append(table[record][NAME])

    return ui.print_result(names,'Oldest record(s):')
            
    



def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    sum_of_years = 0

    names = []
    for sublist in range(len(table)):
        sum_of_years += int(table[sublist][AGE])
        
    average_age = sum_of_years // len(table)

    small_difference = abs(int(table[FIRST_PROP][AGE]) -average_age)

    for sublist in range(len(table)):
        if small_difference > abs(int(table[sublist][AGE]) - average_age):
            small_difference = abs(int(table[sublist][AGE]) - average_age)
            #print(small_difference)


    for sublist in range(len(table)):
        if abs(int(table[sublist][AGE]) - average_age) == small_difference:
            names.append(table[sublist][NAME])

    return ui.print_result(names,'Closest to average:')        




