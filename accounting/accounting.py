""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""
# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
MONTH = 1
DAY = 2
YEAR = 3
TYPE = 4
AMOUNT = 5
file_name = "accounting/items.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # you code
    table = data_manager.get_table_from_file(file_name)
    title = "\n\t Accounting manager"
    list_option = [
        "Show table",
        "Add",
        "Remove",
        "Update",
        "Show year with highest profit",
        "Average profit in given year"]
    exit_message = "Go back to the main menu"
    while True:
        ui.print_menu(title, list_option, exit_message)
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        if option == "2":
            add(table)
        if option == "3":
            remove(table)
        if option == "4":
            update(table,)
        if option == "5":
            which_year_max(table)
        if option == "6":
            avg_amount(table, ui.get_inputs(["Year"], ""))
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code
    profit_per_year = {}
    for row in table:
        if row[YEAR] not in profit_per_year:
            profit_per_year[row[YEAR]] = 0
        if row[TYPE] == "in":
            profit_per_year[row[YEAR]] += int(row[AMOUNT])
        else:  # out
            profit_per_year[row[YEAR]] -= int(row[AMOUNT])
    return ui.print_result([int(max(profit_per_year, key=profit_per_year.get))], "Highest profit year")


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
    count = 0
    profit = 0
    for row in table:
        if row[YEAR] == year[0]:
            if row[TYPE] == "in":
                profit += int(row[AMOUNT])
            else:
                profit -= int(row[AMOUNT])
            count += 1
    try:
        return ui.print_result([profit / count], "Average profit / year")
    except ZeroDivisionError:
        ui.print_error_message("HAHA... nu ai scris anul care trebuie")