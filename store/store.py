""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_game = 'store/games.csv'

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options_list = ["Show table",
                    "Add",
                    "Remove",
                    "Update",
                    "Get counts by manufacturers",
                    "Get avarage by manufacturers"]
    
    while True:
        ui.print_menu("Store manager menu", options_list, "Back to Main Menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(data_manager.get_table_from_file(file_game))
        elif option == "2":
            add(data_manager.get_table_from_file(file_game))
        elif option == "3":
            ID = ui.get_inputs(["ID"], "give me the ID: ")
            remove(data_manager.get_table_from_file(file_game ),ID[0])
        elif option =="4":
            ID = ui.get_inputs(["ID"], "give me the ID: ")
            update(data_manager.get_table_from_file(file_game ),ID[0])
        elif option =="5":
            result = get_counts_by_manufacturers(data_manager.get_table_from_file(file_game ))
            ui.print_result(result,"The manufacturers are")
        elif option == "6":
            manufacturer = ui.get_inputs(["manufacturer"], "Give me the manufacturer")
            result = get_average_by_manufacturer(data_manager.get_table_from_file(file_game),manufacturer[0])
            ui.print_result(result,"The average amount of games in stock is")
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["id","title","manufacturer","price","in_stock"]
    ui.print_table(table, title_list)
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    new_record = ui.get_inputs(["title", "manufacturer", "price", "in_stock"], "")
    new_record.insert(0, common.generate_random(table))
    table.append(new_record)
    data_manager.write_table_to_file(file_game, table)
    modiefied_games = data_manager.get_table_from_file(file_game)
    return modiefied_games


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
    for game in table:
        if game[0] == id_:
            table.remove(game)
    data_manager.write_table_to_file(file_game, table)
    modiefied_games = data_manager.get_table_from_file(file_game)
    return modiefied_games

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    new_data = ui.get_inputs(["title", "manufacturer", "price", "in_stock"],"please give me the details")
    new_data.insert(0, id_)
    for game in range(len(table)):
        if table[game][0] == id_:
            table[game] = new_data
    data_manager.write_table_to_file(file_game, table)
    modified_games = data_manager.get_table_from_file(file_game)
    return modified_games

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    manufacturers = {}
    for game in table:
        manufacturers[game[2]] = manufacturers.get(game[2],0)+1
    return manufacturers
    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    average = []
    sum_sales = 0
    one_manufacture_occurance = 0
    for game in table:
        if game[2].lower() == manufacturer.lower():
            one_manufacture_occurance += 1
            sum_sales += int(game[4])
    average.append(sum_sales / one_manufacture_occurance)

    return average

    # your code
