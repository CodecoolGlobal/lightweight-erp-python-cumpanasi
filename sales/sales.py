""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_sales = 'sales/sales.csv'
table = data_manager.get_table_from_file(file_sales)
ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5
CUSTOMER_ID = 6
FIRST_PROP = 0
SECOND_PROP = 1
THIRD_PROP = 2
FOURTH_PROP = 3
FIFTH_PROP = 4
SIXTH_PROP = 5
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
                   'Get items sold between',
                   'Test_7',
                   'Test_8',
                   'Test_9',
                   'Test_10',
                   'Test_11',
                   'Get all customers ID',
                   'Get all Sales for all ID\'s',
                   'Get count of Sales per ID.']
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
            result = get_lowest_price_item_id(table)
            ui.print_result(result, "The lowest price ID: ")
        elif option == '6':
            date1 = ui.get_inputs(['Year', 'Month' , 'Day'],'Get Start Date')
            date2 = ui.get_inputs(['Year', 'Month' , 'Day'], 'Get End Date')

            if common.flip_dates(int(date1[FIRST_PROP]), int(date1[SECOND_PROP]), int(date1[THIRD_PROP]), int(date2[FIRST_PROP]), int(date2[SECOND_PROP]), int(date2[THIRD_PROP])) == True:
                print('Flipped Dates.')
                date1[FIRST_PROP],date2[FIRST_PROP] = date2[FIRST_PROP],date1[FIRST_PROP]
                date1[SECOND_PROP],date2[SECOND_PROP] = date2[SECOND_PROP],date1[SECOND_PROP]
                date1[THIRD_PROP],date2[THIRD_PROP] = date2[THIRD_PROP],date1[THIRD_PROP]
            
            year_from = int(date1[FIRST_PROP])
            year_to = int(date2[FIRST_PROP])
            month_from = int(date1[SECOND_PROP])
            month_to = int(date2[SECOND_PROP])
            day_from = int(date1[THIRD_PROP])
            day_to = int(date2[THIRD_PROP])
            
            print(year_from,month_from,day_from)
            print(year_to,month_to,day_to)
            result = get_items_sold_between(table,month_from, day_from, year_from, month_to, day_to, year_to)
            #print(result, type(result))
            ui.print_result(result, "Games in between: ")
        elif option == '12':
            get_all_customer_ids_from_table(table)
        elif option == '13':
            get_all_sales_ids_for_customer_ids_from_table(table)
        elif option == '14':
            get_num_of_sales_per_customer_ids_from_table(table)

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

    title_list = ['id', 'title', 'price', 'month', 'day', 'year', 'crm_id']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    return_inputs = ui.get_inputs(['Title', 'Price', 'Year', 'Month' , 'Day', 'Key From Customers'],"Please enter a new record.")
    key = str(common.generate_random(table))
    table.append([key,return_inputs[FIRST_PROP] ,str(return_inputs[SECOND_PROP]), str(return_inputs[FOURTH_PROP]), 
    str(return_inputs[FIFTH_PROP]) , str(return_inputs[THIRD_PROP]), return_inputs[SIXTH_PROP]])
    data_manager.write_table_to_file('sales/sales.csv', table)

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
        data_manager.write_table_to_file('sales/sales.csv', table)    

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

    key = common.check_for_key(id_,table)
    if key == None:
       ui.print_error_message('Key does not exist')
    else:
        return_inputs = ui.get_inputs(['Title', 'Price', 'Year', 'Month' , 'Day', 'Key From Customers'],"Please enter a new record.")
        modif_index = key

        table[modif_index][TITLE]  =  return_inputs[FIRST_PROP]
        table[modif_index][PRICE] = return_inputs[SECOND_PROP]
        table[modif_index][MONTH] = return_inputs[FOURTH_PROP]
        table[modif_index][DAY] = return_inputs[FIFTH_PROP]
        table[modif_index][YEAR] = return_inputs[THIRD_PROP]
        table[modif_index][CUSTOMER_ID] = return_inputs[SIXTH_PROP]
        data_manager.write_table_to_file('sales/sales.csv', table) 

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
    if common.check_empty_table(table) == True:
        ui.print_error_message('Table is empty')
    min_price = table[0][PRICE]
    names_ids_min = []
    names_alpha = []
    for record in range(len(table)):
        if int(min_price) > int(table[record][PRICE]):
            min_price = int(table[record][PRICE])
    
    for record in range(len(table)):
        if int(table[record][PRICE]) == int(min_price):
            names_ids_min.append([table[record][ID], table[record][TITLE]])
    for sublist in range(len(names_ids_min)):
        names_ids_min[sublist][SECOND_PROP] = names_ids_min[sublist][SECOND_PROP].lower()

    names_ids_min = common.sort_me(names_ids_min)
    #print(names_ids_min)

    for elem in range(len(names_ids_min)):
        names_alpha.append(names_ids_min[elem][FIRST_PROP])

    return names_alpha  
    

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
    games_sold_between = []
    #print(table)

    for element in range(len(table)):
        if common.date_in_between(int(table[element][YEAR]), int(table[element][MONTH]), int(table[element][DAY]), year_from, month_from, day_from, year_to, month_to, day_to) == True:
            games_sold_between.append(table[element])

    #print(games_sold_between)

    if len(games_sold_between) == 0:
        print('IS 0')
        return None
    else:
        return games_sold_between
        



# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code
    table = data_manager.get_table_from_file("sales/sales.csv")
    for x in table:
        if x[ID] == id:
            return x[TITLE]
    return None

def get_title_by_id_from_table(table, id): ## 7

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code
    for x in table:
        if x[ID] == id:
            return x[TITLE]
    return None


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    table = data_manager.get_table_from_file("sales/sales.csv")
    sold_dates = []

    for items in table:
        if len(items[MONTH]) == 1:
            items[MONTH] = "0" + items[MONTH]
        if len(items[DAY]) == 1:
            items[DAY] = "0" + items[DAY]
        dates = "".join(items[YEAR] + items[MONTH] + items[DAY])
        sold_dates.append(dates)
    
    last_sold = sold_dates[0]
    for x in sold_dates:
        if x > last_sold:
            last_sold = x

    last_sold_index = 0

    for i in range(len(sold_dates)):
        if sold_dates[i] == last_sold:
            last_sold_index = i
    return table[last_sold_index][ID]


def get_item_id_sold_last_from_table(table): ##8
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    sold_dates = []

    for items in table:
        if len(items[MONTH]) == 1:
            items[MONTH] = "0" + items[MONTH]
        if len(items[DAY]) == 1:
            items[DAY] = "0" + items[DAY]
        dates = "".join(items[YEAR] + items[MONTH] + items[DAY])
        sold_dates.append(dates)
    last_sold = sold_dates[0]
    for x in sold_dates:
        if x > last_sold:
            last_sold = x

    last_sold_index = 0

    for i in range(len(sold_dates)):
        if sold_dates[i] == last_sold:
            last_sold_index = i
    return table[last_sold_index][ID]


def get_item_title_sold_last_from_table(table): ##9
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code
    return get_title_by_id_from_table(table, get_item_id_sold_last_from_table(table))


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code
    table = data_manager.get_table_from_file(file_sales)
    sum_item_ids = 0
    for ids in item_ids:
        for item in table:
            if ids == item[ID]:
                sum_item_ids += int(item[PRICE])
    return sum_item_ids



def get_the_sum_of_prices_from_table(table, item_ids): ##10
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code
    sum_item_ids = 0
    for ids in item_ids:
        for item in table:
            if ids == item[ID]:
                sum_item_ids += int(item[PRICE])
    return sum_item_ids


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code
    table = data_manager.get_table_from_file(file_sales)
    for register in table:
        if register[ID] == sale_id:
            return register[CUSTOMER_ID]


def get_customer_id_by_sale_id_from_table(table, sale_id): ##11
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code
    for register in table:
        if register[ID] == sale_id:
            return register[CUSTOMER_ID]


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    file_sales = 'sales/sales.csv'
    table = data_manager.get_table_from_file(file_sales)

    CUSTOMER_ID = -1
    all_customers_id = []
    for sublist in range(len(table)):
        all_customers_id.append(table[sublist][CUSTOMER_ID])
    return all_customers_id


def get_all_customer_ids_from_table(table): ##12
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    all_customers = get_all_customer_ids()
    ui.print_result(all_customers, 'All customer ID\'s:')


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code
    file_sales = 'sales/sales.csv'
    table = data_manager.get_table_from_file(file_sales)
    customer_id_sales_id = {}
    for sublist in range(len(table)):
        if table[sublist][CUSTOMER_ID] not in customer_id_sales_id.keys():
            customer_id_sales_id[table[sublist][CUSTOMER_ID]] = []
            customer_id_sales_id[table[sublist][CUSTOMER_ID]].append(table[sublist][ID])
        else:
            customer_id_sales_id[table[sublist][CUSTOMER_ID]].append(table[sublist][ID])   
    
    return customer_id_sales_id        
    

def get_all_sales_ids_for_customer_ids_from_table(table): ##13
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code
    sales_by_id = get_all_sales_ids_for_customer_ids()
    ui.print_result(sales_by_id, 'Customer ID\'s and their associated purchases ID:')

def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    file_sales = 'sales/sales.csv'
    table = data_manager.get_table_from_file(file_sales)
    customer_id_sales_id_count = {}
    for sublist in range(len(table)):
        if table[sublist][CUSTOMER_ID] not in customer_id_sales_id_count.keys():
            customer_id_sales_id_count[table[sublist][CUSTOMER_ID]] = 1

        else:
            customer_id_sales_id_count[table[sublist][CUSTOMER_ID]] += 1 
    
    return customer_id_sales_id_count   


def get_num_of_sales_per_customer_ids_from_table(table): ##14
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    count_sales_per_id = get_num_of_sales_per_customer_ids()
    ui.print_result(count_sales_per_id,'Count of sales per Customer ID: ')