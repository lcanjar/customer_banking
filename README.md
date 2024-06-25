# Challenge 3, Customer Banking

# 1.  The assignment:
In this assignment, we use the Account class to create two functions.  These functions calculate interest earned and updates the account balance for both a savings and CD account.  Using a modular approach, the program decomposes into 4 files: Account.py, cd_account.py, customer_banking.py, and savings_account.py.

    - create_savings_account
        Args:
            balance (float): The initial savings account balance.
            interest_rate (float): The APR interest rate for the savings account.
            months (int): The length of months to determine the amount of interest.

        Returns:
            float: The updated savings account balance after adding the interest earned.
            And returns the interest earned.

    - create_cd_account
        Args:
            balance (float): The initial CD account balance.
            interest_rate (float): The APR interest rate for the CD account.
            months (int): The length of months for the CD.

        Returns:
            float: The updated CD account balance after adding the interest earned.
            And returns the interest earned.

# 2.  The Account class.
Within the Account class module, the Account class is created and accepts three parameters:  balance, interest, months.  Associated with this class, there are getter and setter methods to update and retrieve data from the Account object.

# 3.  The function modules.
As listed above, two functions were created that instantiate the classes (in each module), calculate intrest, and return account balance and interest.  These modules do so using the setter and getter methods of the Account class to update and return needed values in the main program.

# 4.  How the code is implemented.
Using the customer_banking.py module, the Account class is instantiated.  User input is gathered to get balance, interest rate, and maturity term.  Then this data is passed to the savings and CD objects and returns to the user a summary of balance and amount of interest earned based upon the Account class object and the aforementioned functions.
