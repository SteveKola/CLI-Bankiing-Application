# This is a Bank application mockup

default_acc_bal = 0.0

list_of_users = {
    'user1@gmail.com': {
        'password': 987654,
        'account_balance': default_acc_bal
    },
    'user2@gmail.com': {
        'password': 123456,
        'account_balance': default_acc_bal
    }
}


def homepage():
    user_input = input("Welcome to VGG Moblile Banking Platform!\
        \nPress 1 to create a new account.\nPress 2 to perform a transaction.\n==>")

    if user_input == '1':
        create_account()
    elif user_input == '2':
        transaction()
    else:
        print("Invalid Input\nExiting...")
        return
    print(list_of_users)
    print("Thank you for banking with us! ")


def create_account():
    email_add = input("Enter an email address to sign up:\n==>")
    if list_of_users.get(email_add):
        print("Your email address is already taken! Please use another email address.")
        create_account()
    list_of_users[email_add] = {}
    list_of_users[email_add]['password'] = input("Create a password:\n==>")
    list_of_users[email_add]['account_balance'] = default_acc_bal

    print("Account successfully registered!")
    transaction()



def transaction():
    user_input = input("Enter your registered email address:\n==>")
    if not list_of_users.get(user_input):
        print("Your email address is not registered! Sign up here.")
        return create_account()
    password = input("Enter your account password: ")
    
    if password != list_of_users[user_input]['password']:
        print("You're not authorized! Create an account here.")
        return create_account()
    
    print(f"Welcome back, {user_input[:-10]}! What would you like to do?")
    transaction_options()

def transaction_options():
    transaction_option = input("Press 1: To check balance\nPress 2: To deposit\
        \nPress 3: For withdrawal\nPress 3: To make a bank transfer\n==>")
    
    if transaction_option == '1':
        check_balance()
    elif transaction_option == '2':
        deposit()
    elif transaction_option == '3':
        withdrawal()
    elif transaction_option == 4:
        transfer()
    else: 
        print("You have select a wrong option! Please read the instructions and select again.")
        transaction_options()

def check_balance():
    pass

def deposit():
    pass 

def withdrawal():
    pass

def transfer():
    pass


homepage()