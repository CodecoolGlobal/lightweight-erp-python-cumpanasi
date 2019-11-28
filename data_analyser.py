"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code
    sales_id_dict = sales.get_all_sales_ids_for_customer_ids()
    list_of_tuples = []
    for key in sales_id_dict.keys():
        sum_per_id  = sales.get_the_sum_of_prices(sales_id_dict[key])
        list_of_tuples.append((key, sum_per_id))

    maxi = list_of_tuples[0][1]

    returnable_list = []
    for elem in list_of_tuples:
        if elem[1] > maxi:
            maxi = elem[1]
    for elem in list_of_tuples:
        if elem[1] == maxi:
            returnable_list.append((crm.get_name_by_id(elem[0]), elem[1]))
    ui.print_result(returnable_list,'Most frequent buyer(s) Name(s).')        

def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code
    sales_id_dict = sales.get_all_sales_ids_for_customer_ids()
    list_of_tuples = []
    for key in sales_id_dict.keys():
        sum_per_id  = sales.get_the_sum_of_prices(sales_id_dict[key])
        list_of_tuples.append((key, sum_per_id))

    maxi = list_of_tuples[0][1]

    returnable_list = []
    for elem in list_of_tuples:
        if elem[1] > maxi:
            maxi = elem[1]
    for elem in list_of_tuples:
        if elem[1] == maxi:
            returnable_list.append((elem))
    ui.print_result(returnable_list,'Most frequent buyer(s) ID.')        




def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code


get_the_buyer_name_spent_most_and_the_money_spent()
get_the_buyer_id_spent_most_and_the_money_spent()