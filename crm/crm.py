""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FIRST_PROP = 0
SECOND_PROP = 1
THIRD_PROP = 2
FOURTH_PROP = 3

ID = 0
NAME = 1
MAIL = 2
SUBSCRIBED = 3




table = data_manager.get_table_from_file('crm/customers.csv')
def start_module():
    
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    title = "\nCustomer Relationship Management (CRM)\n"
    list_option = ['Show Table', 'Add to table', 'Remove from Table via ID', 
    'Update record via ID', 'Get Longest Name ID', 'Get subscribed emails']

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
            get_longest_name_id(table)
        elif option == "6":
            print('\n')
            get_subscribed_emails(table)
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
    titles = ['ID','Name', 'Email', 'Subscribed']
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

    return_inputs = ui.get_inputs(['Name', 'Mail', 'Subscribed'],"Please enter a new record.")
    key = str(common.generate_random(table))
    table.append([key,return_inputs[FIRST_PROP] ,return_inputs[SECOND_PROP], str(return_inputs[THIRD_PROP])])
    data_manager.write_table_to_file('crm/customers.csv', table)

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
        data_manager.write_table_to_file('crm/customers.csv', table)    

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
        return_inputs = ui.get_inputs(['Name', 'Mail', 'Subscribed'], 'Enter New Values')
        modif_index = key

        table[modif_index][NAME]  =  return_inputs[FIRST_PROP]
        table[modif_index][MAIL] = return_inputs[SECOND_PROP]
        table[modif_index][SUBSCRIBED] = return_inputs[THIRD_PROP]
        data_manager.write_table_to_file('crm/customers.csv', table) 

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    longest_name = -1

    for sublist in range(len(table)):
        if len(table[sublist][NAME]) > longest_name:
            longest_name = len(table[sublist][NAME])

    longest_names = []

    for sublist in range(len(table)):
        if len(table[sublist][NAME]) == longest_name:
            longest_names.append(table[sublist][ID])        
    

    return ui.print_result(longest_names,'ID record(s) for longest name(s):')

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """


    subscribed_mails = {}

    for sublist in range(len(table)):
        if table[sublist][SUBSCRIBED] == '1':
            subscribed_mails[table[sublist][NAME]] = table[sublist][MAIL]

    ui.print_result(subscribed_mails, 'Subscribed user(s):')        
    # your code


    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
