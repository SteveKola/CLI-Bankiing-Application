# CLI-Banking-Application
A command-line banking application mockup with the following functionalities:

The application starts with a prompt to the user with the following options:
Press 1: create account.
Press 2: transaction.

## Create account: 
This should prompt you to enter an email address, and then a password. It checks if the email address is unique before creating the new account.
## Transaction: 
It uthenticates the user by prompting for a password, if the password is correct, user is authenticated and show the following options:
    Press 1: check balance
    Press 2: deposit
    Press 3: withdraw
    Press 4: transfer
If the password is incorrect, it tells the user that they are not authorized and it redirects to the 'create account' option.
### Check Balance: 
It queries the data structure to check the balance of the authenticated user.
### Deposit: 
It prompt the user to enter an amount, then add the amount to the users balance.
### withdraw: 
It prompt the user to enter an amount. If the user does not have sufficient funds in their account, it tells them to deposit and redirects to the deposit prompt. If the user has sufficient funds, print out the amount withdrawn and the available balance.
### Transfer: 
It prompts the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, and then add the amount to the beneficiaries account.
