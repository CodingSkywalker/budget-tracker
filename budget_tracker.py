# =================================
# BUDGET TRACKING APPLICATION
# =================================
# this program allows the user to track income and expenses
# all transactions are stored permanently using a local SQL database
# the user can add new transactions and view past ones using a menu

# ---------------------------------
# import required libraries
# ---------------------------------

import sqlite3
# sqlite3 allows Python to create and interact with a small database file
# this database will store all budget transactions safely on the computer

import datetime
# datetime is used to get the current date and time
# this helps us automatically timestamp each transaction


# ---------------------------------
# database setup function
# ---------------------------------

def create_database():
    # connect to the database file named "budget_tracker.db"
    conn = sqlite3.connect('budget_tracker.db')

    # create a cursor object
    # the cursor is used to send SQL commands to the database
    c = conn.cursor()

    # create a table called "transactions" if it does not already exist
    # a table is like an Excel sheet with columns and rows
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,   -- unique number for each transaction
            date TEXT,                -- date and time when the transaction was added
            type TEXT,                -- tells whether the transaction is income or expense
            amount REAL,              -- the money value of the transaction
            description TEXT          -- a short note explaining the transaction
        )
    ''')

    # save (commit) the changes to the database
    # without this, the table would not actually be created
    conn.commit()

    # close the database connection
    # this is important to free resources and avoid database issues
    conn.close()


# ---------------------------------
#  add a new transaction
# ---------------------------------

def add_transaction():
    # ask the user whether this transaction is income or expense
    transaction_type = input("Enter transaction type (income/expense): ")

    # ask the user for the transaction amount
    # float is used to allow decimal values (example: 12.50)
    amount = float(input("Enter amount: "))

    # ask the user for a short description of the transaction
    description = input("Enter a short description: ")

    # get the current date and time
    # we need to turn it into a strftime so it can be turn into a readable string
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # connect to the database
    conn = sqlite3.connect('budget_tracker.db')

    # create a cursor to execute SQL commands
    c = conn.cursor()

    # insert the transaction data into the transactions table
    # question marks (?) are placeholders for user to put data
    c.execute('''
        INSERT INTO transactions (date, type, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, transaction_type, amount, description))

    # save the new transaction to the database
    conn.commit()

    # close the database connection
    conn.close()

    # inform the user that the transaction was saved successfully
    print("Transaction added successfully!")


# ---------------------------------
#  view all transactions
# ---------------------------------

def view_transactions():
    # connect to the database
    conn = sqlite3.connect('budget_tracker.db')

    # create a cursor to run SQL queries
    c = conn.cursor()

    # select all rows and columns from the transactions table
    # this retrieves every saved transaction
    c.execute('SELECT * FROM transactions')

    # get all results from the query
    # each transaction is returned as a tuple
    transactions = c.fetchall()

    # loop through each transaction and print it
    # this displays all saved data to the user
    for transaction in transactions:
        print(transaction)

    # close the database connection
    conn.close()


# ---------------------------------
# main program 
# ---------------------------------

def main():
    # ensure the database and table exist before the program starts
    create_database()

    # run the menu continuously until the user chooses to exit
    while True:
        # display menu options to the user
        print("\nBudget Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        # ask the user to choose an option
        choice = input("Choose an option: ")

        # if the user chooses option 1, add a new transaction
        if choice == '1':
            add_transaction()

        # if the user chooses option 2, display all transactions
        elif choice == '2':
            view_transactions()

        # if the user chooses option 3, exit the program
        elif choice == '3':
            print("Exiting Budget Tracker. Goodbye!")
            break

        # handle invalid input
        else:
            print("Invalid choice. Please try again.")


# ---------------------------------
# start the program
# ---------------------------------

if __name__ == "__main__":
 # this line starts the program by calling the main function
    main()
