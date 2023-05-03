#Terms and functions:
#
#1. tuple: A tuple is an immutable ordered sequence of elements. It is similar to a list, but its elements cannot be changed after creation. In Python, tuples are created using parentheses, e.g., my_tuple = ('apple', 'banana', 'orange').
#
#2. len(): The len() function is a built-in Python function that returns the number of elements in the given iterable (e.g., list, tuple, string, dictionary, set).
#
#3. enumerate(): The enumerate() function is a built-in Python function that allows you to iterate over an iterable (e.g., list, tuple, string) and return both the index and the element itself. The syntax for enumerate() is: `enumerate(iterable, start=0)`, where `iterable` is the sequence to enumerate, and `start` is an optional parameter to define the starting index.
#
#Functions from the code:
#
#1. load_data(filename): This function takes a filename as input, reads the data from the file, and returns the data in the form of a JSON object.
#
#2. display_intro(): This function displays the introduction message of the Business Tycoon game.
#
#3. get_valid_input(min_value, max_value, prompt_message): This function gets valid user input within a specific range (min_value, max_value) and displays a prompt message to the user.
#
#4. get_difficulty_level(): This function gets the user's choice of difficulty level and returns a multiplier based on that choice.
#
#5. get_player_name(): This function gets the player's name from user input.
#
#6. display_company_products(companies): This function displays the products of a selected company.
#
#7. add_new_product_to_company(companies, cash_balance): This function adds a new product to a selected company and adjusts the cash balance accordingly.
#
#8. remove_product_from_company(companies): This function removes a product from a selected company.
#
#9. display_player_info(player_name, cash_balance, companies, offshore_companies, months_passed): This function displays information about the player, including their name, cash balance, companies, offshore companies, and the number of months passed in the game.
#
#10. create_company(player_cash_balance, business_types): This function creates a new company and adjusts the player's cash balance.
#
#11. hire_management(companies, management_personnel): This function allows the player to hire management for a selected company.
#
#12. fire_management(companies): This function allows the player to fire management from a selected company.
#
#13. display_companies_list(companies): This function displays the list of companies owned by the player.
#
#14. company_action(companies, cash_balance, business_types): This function allows the player to perform an action on a selected company and adjusts the cash balance accordingly.
#
#15. create_offshore_company(cash_balance, offshore_locations): This function creates a new offshore company and adjusts the player's cash balance.
#
#16. add_company_to_offshore(offshore_companies, companies): This function adds a company to an offshore company.
#
#17. remove_company_from_offshore(offshore_companies, companies): This function removes a company from an offshore company.
#
#18. advance_month(cash_balance, companies, offshore_companies, difficulty_level): This function advances the game by one month and updates the player's cash balance.
#
#19. update_cash_balance(cash_balance, companies, offshore_companies, difficulty_level): This function updates the player's cash balance based on company revenues and offshore company tax rates.
#
#20. main_game_loop(player_name, cash_balance, companies, business_types, management_personnel, offshore_locations, difficulty_level): This function contains the main game loop, where the player can perform various actions to manage their companies and offshore companies.


import json

def load_data(filename):
    """
    This function loads data from a JSON file and returns it.
    
    :param filename: The filename parameter is a string that represents the name of the file that
    contains the data to be loaded
    :return: The function `load_data` returns the data loaded from a JSON file specified by the
    `filename` parameter.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def display_intro():
    """
    The function displays an introduction message for the Business Tycoon game.
    """
    print("Welcome to the Business Tycoon game!")
    print("In this game, you will start and manage various companies, set up offshore entities, and hire management.")
    print("Your goal is to become the ultimate business tycoon!")

def get_valid_input(min_value, max_value, prompt_message):
    """
    The function "get_valid_input" takes in a minimum value, maximum value, and prompt message, and
    prompts the user to input a number within the specified range, returning the valid input.
    
    :param min_value: The minimum value that the user input can be
    :param max_value: The maximum value that the user can input
    :param prompt_message: This is the message that will be displayed to the user to prompt them to
    enter a value
    :return: the user input if it is a valid integer between the minimum and maximum values specified.
    If the user input is not valid, the function continues to prompt the user until a valid input is
    provided.
    """
    while True:
        try:
            user_input = int(input(prompt_message))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please try again.")

def get_difficulty_level():
    """
    The function returns a difficulty multiplier based on the user's choice of difficulty level.
    :return: The function `get_difficulty_level()` returns a difficulty multiplier based on the user's
    choice of difficulty level. The difficulty multiplier is a float value between 0.25 and 1.0, with
    1.0 being the easiest difficulty level and 0.25 being the hardest difficulty level. The function
    prints a menu of difficulty levels and prompts the user to enter a number corresponding to their
    """
    print("1. Rare (Easiest)")
    print("2. Medium Rare")
    print("3. Medium Well")
    print("4. Well Done (Hardest)")

    choice = get_valid_input(1, 4, "Enter the number corresponding to your choice: ")
    
    difficulty_multipliers = {
        1: 1,
        2: 0.75,
        3: 0.5,
        4: 0.25
    }

    return difficulty_multipliers[choice]
    
def get_player_name():
    """
    This function prompts the user to enter their name and returns the input as a string.
    :return: the player's name as a string.
    """
    player_name = input("Please enter your name: ")
    return player_name

def display_company_products(companies):
    """
    This function displays the products of a selected company from a list of companies.
    
    :param companies: a list of dictionaries, where each dictionary represents a company and contains
    the following keys: 'name' (string), 'products' (list of dictionaries), where each dictionary
    represents a product and contains the following keys: 'name' (string) and 'investment' (float)
    """
    if len(companies) > 0:
        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to view Product(s) for: ")
        company = companies[company_choice - 1]
        if len(company['products']) == 0:
            print(f"{company['name']} has no Product(s).")
        else:
            print("\nProduct(s):")
            for i, product in enumerate(company['products'], 1):
                print(f"{i}. {product['name']} - Investment: ${product['investment']}")
    else:
        print("You don't have any companies to view Product(s) for. Create a company first.")
        
def add_new_product_to_company(companies, cash_balance):
    """
    This function allows the user to add a new product to a chosen company, with an investment amount
    and updates the company's revenue and profit accordingly.
    
    :param companies: A list of dictionaries representing companies, where each dictionary contains
    information about a company such as its name, revenue, profit margin, and products
    :param cash_balance: The amount of money available to invest in the new product
    :return: a tuple containing the updated list of companies and the updated cash balance.
    """
    if len(companies) > 0:
        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to add a product to: ")
        company = companies[company_choice - 1]

        product_name = input("Enter a name for your new product: ")
        investment = get_valid_input(0, float('inf'), "Enter the amount of money you want to invest in this product: ")

# The code is a Python script that takes an investment amount and a product name as input and
# adds the product to a company's product list. It then calculates the added revenue and profit from
# the investment and updates the company's revenue and profit margin accordingly. If the user's cash
# balance is not enough to make the investment, it prints an error message.
        if cash_balance >= investment:
            cash_balance -= investment
            profit_margin = 0.1
            added_revenue = investment * profit_margin
            added_profit = added_revenue * company['profit_margin']
            company['revenue'] += added_revenue
            company['profit_margin'] += (company['profit_margin'] * added_profit) / company['revenue']
            company['products'].append({'name': product_name, 'investment': investment, 'revenue': added_revenue})
            print(f"You have successfully added {product_name} to {company['name']} with an investment of ${investment}.")
            print(f"Company's revenue increased by ${added_revenue} and profit increased by ${added_profit}.")
        else:
            print("You don't have enough cash to invest in this Product(s). Please try again.")
    else:
        print("You don't have any companies to add a Product(s) to. Create a company first.")
    return companies, cash_balance

def remove_product_from_company(companies):
    """
    This function removes a product from a company and returns the updated list of companies.
    
    :param companies: a list of dictionaries representing companies, where each dictionary has keys
    'name' (string) and 'products' (list of dictionaries representing products, where each dictionary
    has keys 'name' (string) and 'investment' (float))
    :return: the updated list of companies after removing a product from a chosen company.
    """
    if len(companies) > 0:
        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to remove a Product(s) from: ")
        company = companies[company_choice - 1]

        if len(company['products']) == 0:
            print(f"{company['name']} has no Product(s) to remove.")
        else:
            print("Product(s):")
            for i, product in enumerate(company['products'], 1):
                print(f"{i}. {product['name']} - Investment: ${product['investment']}")
            product_choice = get_valid_input(1, len(company['products']), "Enter the number of the Product(s) you want to remove: ")

            removed_product = company['products'].pop(product_choice - 1)
            print(f"{removed_product['name']} has been removed from {company['name']}.")
    else:
        print("You don't have any companies to remove a Product(s) from. Create a company first.")
    return companies

def display_player_info(player_name, cash_balance, companies, offshore_companies, months_passed):
    """
    This function displays the player's information, including their name, cash balance, companies,
    offshore companies, and months passed.
    
    :param player_name: The name of the player (string)
    :param cash_balance: The amount of money the player currently has in their account
    :param companies: A list of dictionaries representing the companies owned by the player. Each
    dictionary contains information about the company such as its name, industry, revenue, capital,
    profit margin, and management (if any)
    :param offshore_companies: A list of dictionaries representing the offshore companies owned by the
    player. Each dictionary contains information about the company such as its name and location
    :param months_passed: The number of months that have passed in the game
    """
    print(f"\nMonths passed: {months_passed}")
    print("\nPlayer Information:")
    print(f"Name: {player_name}")
    print(f"Cash Balance: ${cash_balance}")
    print("Companies:")
    if len(companies) == 0:
        print("None")
    else:
        for i, company in enumerate(companies, 1):
            monthly_revenue = company['revenue'] * company['capital']
            monthly_profit = monthly_revenue * company['profit_margin'] * difficulty_level
            print(f"{i}. {company['name']} ({company['industry']}) - Management: {company['management']['name'] if 'management' in company else 'None'}, Monthly Revenue: ${monthly_revenue}, Monthly Profit: ${monthly_profit}")

    print("Offshore Companies:")
    if len(offshore_companies) == 0:
        print("None")
    else:
        for i, offshore_company in enumerate(offshore_companies, 1):
            print(f"{i}. {offshore_company['name']} ({offshore_company['location']})")

def create_company(player_cash_balance, business_types):
    """
    This function creates a new company with a chosen business type, name, and initial capital, and
    subtracts the capital from the player's cash balance if they have enough funds.
    
    :param player_cash_balance: The amount of cash the player has available to start a new business
    :param business_types: a list of dictionaries, where each dictionary represents a type of business
    and contains the following keys: 'name' (string), 'startup_capital' (float), 'revenue' (float), and
    'profit_margin' (float)
    :return: a tuple containing a dictionary representing the newly created company and the updated
    player cash balance. If the player does not have enough cash or capital to start the business, the
    function returns None for the company and the original player cash balance.
    """
    print("Available business types:")
    for i, business in enumerate(business_types, 1):
        print(f"{i}. {business['name']} (Startup Capital: ${business['startup_capital']})")
    business_choice = get_valid_input(1, len(business_types), "Choose a business type by entering the corresponding number: ")

    business = business_types[business_choice - 1]
    company_name = input("Enter a name for your new company: ")
    capital = get_valid_input(0, float('inf'), "Enter the initial capital for your company (in dollars): ")

    if capital >= business['startup_capital']:
        if player_cash_balance >= capital:
            player_cash_balance -= capital
            return {'name': company_name, 'industry': business['name'], 'capital': capital, 'offshore': False, 'revenue': business['revenue'], 'profit_margin': business['profit_margin'], 'products': []}, player_cash_balance
        else:
            print("You don't have enough cash to start this business. Please try again.")
            return None, player_cash_balance
    else:
        print("You don't have enough capital to start this business. Please try again.")
        return None, player_cash_balance
        
def hire_management(companies, management_personnel):
    """
    This function allows the user to hire a manager for a chosen company from a list of available
    managers, given that the company has no current manager and has enough monthly profit to pay the
    manager's salary.
    
    :param companies: a list of dictionaries representing companies, where each dictionary contains
    information about a single company such as its name, revenue, profit margin, and management (if any)
    :param management_personnel: A list of dictionaries representing potential managers for a company.
    Each dictionary contains the following keys:
    :return: either the updated company dictionary if a manager was successfully hired, or None if a
    manager was not hired.
    """
    if len(companies) > 0:
        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to hire management for: ")
        company = companies[company_choice - 1]
        if 'management' in company:
            print(f"{company['name']} already has a manager: {company['management']['name']}. Please fire the current manager before hiring a new one.")
            return
    else:
        print("You don't have any companies to hire management for. Create a company first.")
        return None

    print("Available managers:")
    for i, manager in enumerate(management_personnel, 1):
        print(f"{i}. {manager['name']} (Salary: ${manager['salary']}/month, Revenue Boost: {manager['revenue_boost'] * 100}%, Profit Margin Boost: {manager['profit_margin_boost'] * 100}%)")
    manager_choice = get_valid_input(1, len(management_personnel), "Choose a manager to hire by entering the corresponding number: ")

    manager = management_personnel[manager_choice - 1]
    monthly_revenue = company['revenue'] * company['capital']
    monthly_profit = monthly_revenue * company['profit_margin']
    if manager['salary'] <= monthly_profit:
        company['revenue'] *= (1 + manager['revenue_boost'])
        company['profit_margin'] += manager['profit_margin_boost']
        company['management'] = manager
        print(f"{manager['name']} has been hired as a manager for {company['name']} at a salary of ${manager['salary']}/month.")
        return company
    else:
        print("You don't have enough monthly profit to hire this manager. Please try again.")
        return None

def fire_management(companies):
    """
    The function allows the user to fire the management of a company and adjust the company's revenue
    and profit margin accordingly.
    
    :param companies: a list of dictionaries representing different companies, where each dictionary
    contains information about the company such as its name, revenue, profit margin, and management (if
    any)
    """
    if len(companies) > 0:
        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to fire management for: ")
        company = companies[company_choice - 1]
        if 'management' in company:
            print(f"{company['management']['name']} has been fired from {company['name']}.")
            company['revenue'] /= (1 + company['management']['revenue_boost'])
            company['profit_margin'] -= company['management']['profit_margin_boost']
            del company['management']
        else:
            print(f"{company['name']} does not have a manager to fire.")
    else:
        print("You don't have any companies to fire management for. Create a company first.")

def display_companies_list(companies):
    """
    The function takes a list of dictionaries representing companies and prints their names and
    industries in a numbered list format.
    
    :param companies: a list of dictionaries, where each dictionary represents a company and contains
    the keys 'name' and 'industry'
    """
    print("Companies:")
    for i, comp in enumerate(companies, 1):
        print(f"{i}. {comp['name']} ({comp['industry']})")

def company_action(companies, cash_balance, business_types):
    """
    The function allows the user to perform an action on a selected company, such as launching a new
    product or starting a building project, and updates the company's revenue and the user's cash
    balance accordingly.
    
    :param companies: a list of dictionaries representing the companies the user has created, with each
    dictionary containing information such as the company name, industry, and revenue
    :param cash_balance: The amount of cash available for the user to spend on company actions
    :param business_types: a list of dictionaries containing information about different types of
    businesses, including their name and profit margin
    :return: a tuple containing the updated list of companies and the updated cash balance.
    """
    if len(companies) == 0:
        print("You have no companies to perform an action on. Create a company first.")
    else:
        display_companies_list(companies)
        company_index = int(input("Enter the number of the company you want to perform an action on: "))
        if 0 < company_index <= len(companies):
            company = companies[company_index - 1]
            business_type = next((biz_type for biz_type in business_types if biz_type['name'] == company['industry']), None)
            
            if business_type is not None:
                if company['industry'] == "Dropshipping":
                    product_cost = get_valid_input(0, float('inf'), "Enter the cost of the product you want to launch (in dollars): ")
                    if cash_balance >= product_cost:
                        cash_balance -= product_cost
                        company['revenue'] += product_cost * business_type['profit_margin']
                        print(f"You have successfully launched a new product in your Dropshipping company. Your company's revenue has increased.")
                    else:
                        print("You don't have enough cash to launch this product. Please try again.")
                elif company['industry'] == "Construction":
                    project_cost = get_valid_input(0, float('inf'), "Enter the cost of the building project you want to start (in dollars): ")
                    if cash_balance >= project_cost:
                        cash_balance -= project_cost
                        company['revenue'] += project_cost * business_type['profit_margin']
                        print(f"You have successfully started a new building project in your Construction company. Your company's revenue has increased.")
                    else:
                        print("You don't have enough cash to start this project. Please try again.")
            else:
                print("Error: Business type not found.")
        else:
            print("Invalid company number. Please try again.")
    return companies, cash_balance

def create_offshore_company(cash_balance, offshore_locations):
    """
    This function creates an offshore company by taking in a cash balance and a list of offshore
    locations, allowing the user to choose a location and name for the company, and deducting the setup
    cost from the cash balance if there is enough money.
    
    :param cash_balance: The amount of cash available to set up the offshore company
    :param offshore_locations: a list of dictionaries containing information about different offshore
    locations, including their name, setup cost, and tax rate
    :return: A tuple containing a dictionary representing the newly created offshore company and the
    updated cash balance. If the creation of the offshore company is not successful, None is returned
    instead of the dictionary.
    """
    print("Offshore locations:")
    for i, location in enumerate(offshore_locations, 1):
        print(f"{i}. {location['name']} (Setup Cost: ${location['setup_cost']},Tax Rate: {location['tax_rate'] * 100}%)")
    location_choice = get_valid_input(1, len(offshore_locations), "Choose an offshore location by entering the corresponding number: ")

    if 0 < location_choice <= len(offshore_locations):
        location = offshore_locations[location_choice - 1]
        if cash_balance >= location['setup_cost']:
            cash_balance -= location['setup_cost']
            offshore_name = input("Enter a name for your new offshore company: ")
            return {'name': offshore_name, 'location': location['name'], 'tax_rate': location['tax_rate'], 'companies': []}, cash_balance
        else:
            print("You don't have enough cash to set up an offshore company in this location. Please try again.")
            return None, cash_balance
    else:
        print("Invalid offshore location. Please try again.")
        return None, cash_balance

def add_company_to_offshore(offshore_companies, companies):
    """
    This function adds a company to an offshore company and updates the lists of offshore companies and
    regular companies.
    
    :param offshore_companies: A list of dictionaries representing offshore companies. Each dictionary
    contains the keys 'name', 'location', and 'companies'. The 'companies' key has a value of a list of
    dictionaries representing companies that are part of the offshore company
    :param companies: A list of dictionaries representing regular companies, where each dictionary
    contains information about a single company such as its name, location, and whether it is part of an
    offshore company or not
    :return: a tuple containing the updated lists of offshore companies and regular companies.
    """
    if len(offshore_companies) > 0 and len(companies) > 0:
        print("Offshore Companies:")
        for i, offshore_company in enumerate(offshore_companies, 1):
            print(f"{i}. {offshore_company['name']} ({offshore_company['location']})")
        offshore_choice = get_valid_input(1, len(offshore_companies), "Enter the number of the offshore company you want to add a company to: ")
        offshore_company = offshore_companies[offshore_choice - 1]

        display_companies_list(companies)
        company_choice = get_valid_input(1, len(companies), "Enter the number of the company you want to add to the offshore company: ")
        company = companies[company_choice - 1]
        if company['offshore']:
            print(f"{company['name']} is already part of an offshore company. Please remove it from the current offshore company before adding it to a new one.")
            return offshore_companies, companies
        else:
            offshore_company['companies'].append(company)
            company['offshore'] = True
            print(f"{company['name']} has been added to {offshore_company['name']}.")
            return offshore_companies, companies
    else:
        print("You don't have any offshore companies or regular companies. Create them first.")
        return offshore_companies, companies

def remove_company_from_offshore(offshore_companies, companies):
    """
    This function removes a company from an offshore company and updates the company's offshore status.
    
    :param offshore_companies: A list of dictionaries representing offshore companies, where each
    dictionary has keys 'name', 'location', and 'companies'. 'companies' is a list of dictionaries
    representing companies that are part of the offshore company, where each dictionary has keys 'name',
    'industry', and 'offshore' (a boolean
    :param companies: A list of dictionaries representing regular companies, where each dictionary
    contains the keys 'name' (string), 'industry' (string), and 'offshore' (boolean)
    :return: a tuple containing the updated lists of offshore_companies and companies.
    """
    if len(offshore_companies) > 0 and len(companies) > 0:
        print("Offshore Companies:")
        for i, offshore_company in enumerate(offshore_companies, 1):
            print(f"{i}. {offshore_company['name']} ({offshore_company['location']})")
        offshore_choice = get_valid_input(1, len(offshore_companies), "Enter the number of the offshore company you want to remove a company from: ")
        offshore_company = offshore_companies[offshore_choice - 1]

        print("Companies in the offshore company:")
        for i, comp in enumerate(offshore_company['companies'], 1):
            print(f"{i}. {comp['name']} ({comp['industry']})")
        company_choice = get_valid_input(1, len(offshore_company['companies']), "Enter the number of the company you want to remove from the offshore company: ")
        company = offshore_company['companies'][company_choice - 1]
        offshore_company['companies'].remove(company)
        company['offshore'] = False
        print(f"{company['name']} has been removed from {offshore_company['name']}.")
        return offshore_companies, companies
    else:
        print("You don't have any offshore companies or regular companies. Create them first.")
        return offshore_companies, companies

def advance_month(cash_balance, companies, offshore_companies, difficulty_level):
    """
    The function advances the month by updating the cash balance based on the given parameters and
    returns the updated cash balance.
    
    :param cash_balance: The current amount of cash the player has in the game
    :param companies: a list of dictionaries representing the companies the player owns. Each dictionary
    contains the following keys: "name" (string), "revenue" (float), "expenses" (float), "price"
    (float), "shares" (int), "growth" (float)
    :param offshore_companies: A list of companies that the player can invest in outside of their home
    country. These companies may have different risks and rewards compared to the local companies
    :param difficulty_level: a variable that determines the level of difficulty in the game. It can
    affect the amount of money earned or lost during the game
    :return: the updated cash balance after calling the `update_cash_balance` function with the given
    parameters.
    """
    cash_balance = update_cash_balance(cash_balance, companies, offshore_companies, difficulty_level)
    return cash_balance

def update_cash_balance(cash_balance, companies, offshore_companies, difficulty_level):
    """
    The function updates the cash balance by calculating the taxed profit of each company, taking into
    account the operating cost and tax rate, and adding it to the current cash balance.
    
    :param cash_balance: The current balance of cash available
    :param companies: a list of dictionaries representing companies, with each dictionary containing
    information about a single company such as revenue, capital, and profit margin
    :param offshore_companies: a list of dictionaries representing offshore companies, where each
    dictionary contains the following keys: 'name' (string), 'tax_rate' (float), and 'companies' (list
    of dictionaries representing companies)
    :param difficulty_level: a numerical value representing the difficulty level of the game
    :return: the updated cash balance after calculating the taxed profit for each company in the list of
    companies.
    """
    for company in companies:
        profit = company['revenue'] * company['capital'] * company['profit_margin']
        operating_cost = company['capital'] * 0.05  # Added operating_cost (5% of capital)
        tax_rate = 0.15  # Updated default tax rate
        if company['offshore']:
            for offshore_company in offshore_companies:
                if company in offshore_company['companies']:
                    tax_rate = offshore_company['tax_rate']
                    break
        taxed_profit = ((profit * difficulty_level) - operating_cost) * (1 - tax_rate)  # Deduct operating_cost before taxes
        cash_balance += taxed_profit
    return cash_balance

def main_game_loop(player_name, cash_balance, companies, business_types, management_personnel, offshore_locations, difficulty_level):
    """
    This function contains the main game loop for a business tycoon game, allowing the player to make
    choices such as starting a new business, hiring and firing management, creating offshore companies,
    and advancing months.
    
    :param player_name: The name of the player who is playing the game
    :param cash_balance: The amount of money the player has to start with and use throughout the game
    :param companies: A list of dictionaries representing the player's owned companies, with each
    dictionary containing information such as the company name, type of business, revenue, and expenses
    :param business_types: A list of dictionaries containing information about different types of
    businesses that can be created in the game, such as their name, revenue, and profit margin
    :param management_personnel: A list of dictionaries representing the available management personnel
    that can be hired for the player's companies. Each dictionary contains information such as the name,
    salary, and skills of the management personnel
    :param offshore_locations: offshore_locations is a list of possible locations where the player can
    create an offshore company. These locations may have different tax laws or regulations that can
    affect the player's profits and cash balance
    :param difficulty_level: The difficulty level of the game, which affects the starting cash balance
    and the revenue and profit margin of the business types
    """
    months_passed = 0
    offshore_companies = []

    cash_balance *= 0.5  # Reduce the starting cash balance
    for business_type in business_types:
        business_type['revenue'] *= 0.5  # Reduce the revenue
        business_type['profit_margin'] *= 0.5  # Reduce the profit margin
                
    while True:
        display_player_info(player_name, cash_balance, companies, offshore_companies, months_passed)
        
        print("\n1. Start a new business")
        print("2. Hire management")
        print("3. Fire management")
        print("4. Create an offshore company")
        print("5. Add a company to an offshore company")
        print("6. Remove a company from an offshore company")
        print("7. Advance month")
        print("8. View Product(s)")
        print("9. Add a Product(s) to a company")
        print("10. Remove a Product(s) from a company")
        print("11. Quit game")
        
        choice = get_valid_input(1, 11, "Enter the number corresponding to your choice: ")
                        
        if choice == 1:
            new_company, cash_balance = create_company(cash_balance, business_types)
            if new_company is not None:
                companies.append(new_company)
        elif choice == 2:
            company = hire_management(companies, management_personnel)
        elif choice == 3:
            fire_management(companies)
        elif choice == 4:
            new_offshore_company, cash_balance = create_offshore_company(cash_balance, offshore_locations)
            if new_offshore_company is not None:
                offshore_companies.append(new_offshore_company)
        elif choice == 5:
            offshore_companies, companies = add_company_to_offshore(offshore_companies, companies)
        elif choice == 6:
            offshore_companies, companies = remove_company_from_offshore(offshore_companies, companies)
        elif choice == 7:
            cash_balance = advance_month(cash_balance, companies, offshore_companies, difficulty_level)
            months_passed += 1
        elif choice == 8:
            display_company_products(companies)
        elif choice == 9:
            companies, cash_balance = add_new_product_to_company(companies, cash_balance)
        elif choice == 10:
            companies = remove_product_from_company(companies)
        elif choice == 11:
            print("Thank you for playing Business Tycoon! Goodbye.")
            break
        else:
            print("Invalid input. Please try again.")
        
# The code is initializing variables and loading data for a business simulation game. It
# displays an introduction, gets the player's name, sets a starting cash balance, loads data for
# business types, management personnel, and offshore locations, and gets the difficulty level from the
# player.
display_intro()
player_name = get_player_name()
cash_balance = 10000  # Starting cash balance
companies = []
business_types = load_data('business_types.json')
management_personnel = load_data('management.json')
offshore_locations = load_data('offshore_locations.json')
difficulty_level = get_difficulty_level()

# The code is defining a function called `main_game_loop` that takes in several parameters
# including `player_name`, `cash_balance`, `companies`, `business_types`, `management_personnel`,
# `offshore_locations`, and `difficulty_level`. The purpose of the function is not clear without
# additional context, but it likely contains the main logic for a game or simulation involving
# managing companies and making financial decisions.
main_game_loop(player_name, cash_balance, companies, business_types, management_personnel, offshore_locations, difficulty_level)