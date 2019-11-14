""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
NAME = 1
MANUFACTURER = 2
PURCHASE_YEAR = 3
DURABILITY = 4
file_name = "inventory/inventory.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    table = data_manager.get_table_from_file(file_name)
    title = "\nINVENTORY MANAGER"
    list_options = [
        "Show Table",
        "Add to Table",
        "Remove from Table",
        "Update Table",
        "Get available items",
        "Get average durability by manufacturer"]
    exit_message = "Go back to main menu"
    while True:
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == '2':
            add(table)
        elif option == '3':
            id = ui.get_inputs(["Id"], "Please enter the ID to remove: ")[0]
            data_manager.write_table_to_file(file_name, remove(table, id))
        elif option == '4':
            id = ui.get_inputs(["Id"], "Please enter the ID to update: ")[0]
            data_manager.write_table_to_file(file_name, update(table, id))
        elif option == '5':
            year = ui.get_inputs(["Year"], "Please enter a year: ")[0]
            print(get_available_items(table, year)) #['kH34Ju#&', 'PlayStation 4', 'Sony', 2013, 4], ['jH34Ju#&', 'Xbox One', 'Microsoft', 2013, 4]
        elif option == '6':
            print(get_average_durability_by_manufacturers(table)) # {'Sony': 3.5, 'Microsoft': 4.0, 'Nintendo': 3.25}
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    

    # your code
    for x, val in enumerate(table):
        print(f"{x} {val}")


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    new_update = []
    new_update.append(common.generate_random(table))
    user_inputs = ui.get_inputs(["Name", "Manufacturer", "Purchase Year", "Durability"], "Please provide item information: ")
    for user_input in user_inputs:
        new_update.append(user_input)
    table.append(new_update)
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
    for row in table:
        if row[ID] == id_:
            table.remove(row)
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
    new_update = []
    user_inputs = ui.get_inputs(["Name", "Manufacturer", "Purchase Year", "Durability"], "Please provide inventory information: ")
    for i in range(len(table)):
        if table[i][ID] == id_:
            new_update.append(table[i][ID])
            for user_input in user_inputs:
                new_update.append(user_input)
            table[i] = new_update
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    for row in table:
        row[PURCHASE_YEAR] = int(row[PURCHASE_YEAR])
        row[DURABILITY] = int(row[DURABILITY])
    result = []
    for row in table:
        if (row[PURCHASE_YEAR] + row[DURABILITY]) > int(year):
            result.append(row)
    return result


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    average_durability = {}
    for row in table:
        if row[MANUFACTURER] not in average_durability:
            average_durability[row[MANUFACTURER]] = [0, 0]

        average_durability[row[MANUFACTURER]][0] += int(row[DURABILITY])
        average_durability[row[MANUFACTURER]][1] += 1

    for key in average_durability.keys():
        average_durability[key] = average_durability[key][0] / average_durability[key][1]

    return average_durability
