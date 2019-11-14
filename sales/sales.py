""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_sales = 'sales/sales.csv'
def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    option_list = ['Show table',
                   'Add',
                   'Remove',
                   'Update',
                   'Get lowest price item id',
                   'Get items sold between']
    while True:
        ui.print_menu("Sales manager menu", option_list, "Back to Main Menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            show_table(data_manager.get_table_from_file(file_sales))
        elif option == '2':
            add(data_manager.get_table_from_file(file_sales))
        elif option == '3':
            ID = ui.get_inputs(['ID'], "Give me the ID: ")
            remove(data_manager.get_table_from_file(file_sales), ID[0])
        elif option == '4':
            ID = ui.get_inputs(['ID'], "Give me the ID: ")
            update(data_manager.get_table_from_file(file_sales), ID[0])
        elif option == '5':
            result = get_lowest_price_item_id(data_manager.get_table_from_file(file_sales))
            ui.print_result(result, "The lowest price ID: ")
        elif option == '6':
            dates = ui.get_inputs(['month from', 'day from', 'year from', 'month to', 'day to', 'year to'], "Give me the dates: ")
            result = get_items_sold_between(data_manager.get_table_from_file(file_sales), dates[0], dates[1], dates[2], dates[3], dates[4], dates[5],)
            ui.print_result(result, "Two dates: ")
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option!")
    


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'title', 'price', 'month', 'day', 'year']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_record = ui.get_inputs(['title', 'price', 'month', 'day', 'year'], "")
    new_record.insert(0, common.generate_random(table))
    table.append(new_record)
    data_manager.write_table_to_file(file_sales, table)
    modified_sales = data_manager.get_table_from_file(file_sales)
    return modified_sales


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

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
