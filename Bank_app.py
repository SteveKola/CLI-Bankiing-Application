# This is a Bank application mockup 

default_acc_bal = 0.0

# we initialize the list of users dictionary with mock users for testing purposes
list_of_users = {
    'user1@gmail.com': {
        'password': '987654',
        'acc_bal': default_acc_bal
    },
    'user2@gmail.com': {
        'password': '123456',
        'acc_bal': default_acc_bal
    }
}

# at homepage, users can either create a new account or go straight to transactions
def homepage():
    user_input = input("Welcome to VGG Mobile Banking Platform!\
        \nPress 1 to create a new account.\nPress 2 to perform a transaction.\n==> ")

    if user_input == '1':
        create_account()
    elif user_input == '2':
        transaction()
    else:
        print("Invalid Input\nExiting...")
        return
    print("\nThank you for banking with us! ")

# New users create new account with unique email addresses,
# and their data get appended to the list of users dictionary
def create_account():
    email_add = input("...\nEnter an email address to sign up:\n==> ")
    if list_of_users.get(email_add):
        print("Your email address is already taken! Please use another email address.")
        create_account()

    list_of_users[email_add] = {}
    list_of_users[email_add]['password'] = input("Create a password:\n==> ")
    list_of_users[email_add]['acc_bal'] = default_acc_bal

    print("Account successfully registered!")
    transaction()


# Users sign in will only be successful with the correct email address and password input
def transaction():
    email_add = input("...\nEnter your registered email address:\n==> ")
    if not list_of_users.get(email_add):
        print("...\nYour email address is not registered! Sign up here.")
        return create_account()
    password = input("Enter your account password:\n==> ")
    
    if password != list_of_users[email_add]['password']:
        print("You're not authorized! Create an account here.")
        return create_account()
    
    # Once login is successsful, it redirects to transaction options selection
    print(f"\nWelcome back, {email_add[:-10]}! What would you like to do?")
    transaction_options(email_add)


def transaction_options(email_add):
    option = input("...\nPress 1: To check balance\nPress 2: To deposit\
        \nPress 3: For withdrawal\nPress 4: To make a bank transfer\n==> ")
    
    if option not in ['1', '2', '3', '4']:
        print("Invalid option! Please read the instructions and select again.")
        return transaction_options(email_add)

    if option == '2':
        deposit_amount = int(input("How much do you wish to deposit?\n==> "))
        deposit(deposit_amount, email_add) # redirects to the deposit function
        print("Deposit successful!\n...")

    elif option == '3':
        withdrawal_amount = int(input("How much do you wish to withdraw?\n==> "))
        withdrawal(withdrawal_amount, email_add)    # redirects to the withdrawal function
        print("Withdrawal Successful! Take your cash below!\n...")

    elif option == '4': 
        transfer(email_add) # redirects to the transfer function

    # there is a check balance function call at the end of all the various operations
    check_balance(email_add) 

    # ask if the users wants to perform another operation
    another_transaction = input("...\nDo you wish to perform another transaction?\
        \n Press 1: Yes\nPress 2: No\n==> ")
    if another_transaction == '1':
        transaction_options(email_add)


def check_balance(email_add):
    print(f"Your account balance is ₦{list_of_users[email_add]['acc_bal']}")


def deposit(amount, email_add):
    list_of_users[email_add]['acc_bal'] += amount


# it deducts the cash specified from the account balance
# if there is not enough money in the account, it redirects to the deposit function
def withdrawal(amount, email_add):
    if amount > list_of_users[email_add]['acc_bal']:
        print("...\nInsufficient Funds! Make a deposit instead.")
        deposit_amount = int(input("How much would you like to deposit?==> "))
        return deposit(deposit_amount, email_add)
    list_of_users[email_add]['acc_bal'] -= amount


# if there beneficiary email address is not valid (not in the users list),
# it asks for a retry. Then it redirects first to the withdrawal function
# then it redirects to the deposit function and add the amount to the beneficiary's account
def transfer(email_add):
    beneficiary = input("Enter the email address of the recipient:\n==> ")
    if beneficiary not in list_of_users:
        print("Invalid Username!")
        return transfer(email_add)

    amount = int(input("How much do you wish to transfer to the recipient?\n==> "))
    withdrawal(amount, email_add)
    return deposit(amount, beneficiary)


homepage()