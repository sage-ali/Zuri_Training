import datetime # Module for getting date
import re
import random
import json
import os

script_dir = os.path.dirname(__file__)
db_path = os.path.join(script_dir, 'accountDB.json')

# Getting and printing date and time  
e = datetime.datetime.now()
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s" % (e.hour, e.minute))

current_user = {}
current_user_acct = ''
current_user_index = 0

# 4. Any other improvement you can think of (extra point)

print("===" * 24)
print("welcome to bankPHP, the coded bank\n")

def validate_userdetails(name, email, password):
    #logic to validate user details 
    if (re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email) and re.search(r"^[a-zA-Z]+(?:\s[a-zA-Z]+)+$", name) and re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$", password)):
        print("Valid details\n")
        return
    else:
        print("Enter valid details\n")
        register()
        
        
def generate_account_number():
    return random.randrange(1111111111,9999999999)

def validate_login_details(account_number, password):
    #authenticating user information for login purposes
    with open(db_path) as fi:
        user_datas = json.load(fi)
        for user in user_datas:
            if user.get(account_number, False) and user[account_number]['password'] == password:
                current_user.update(user)
                global current_user_acct 
                current_user_acct = str(account_number)
                global current_user_index
                current_user_index = user_datas.index(user)
                return True
    return False

def update_account(user):
    with open(db_path) as fi:
        user_datas = json.load(fi)
        user_datas[current_user_index] = user
    
    with open(db_path, mode='w') as f:
        f.write(json.dumps(user_datas, indent=4))

def withdraw(user):
    balance = float(user[current_user_acct]['account_balance'])
    withdraw_amount = float(input('How much will you like to withdraw: '))
    if withdraw_amount <= balance:
        print(f'Take your cash: {withdraw_amount}')
        user[current_user_acct]['account_balance'] = str(balance - withdraw_amount)
        update_account(user)
        logout()
    else:
        print('Insufficient funds')
        logout()
                
def deposit(user):
    balance = float(user[current_user_acct]['account_balance'])
    deposit_amount = float(input('How much will you like to deposit: '))
    user[current_user_acct]['account_balance'] = str(balance + deposit_amount)
    bal = user[current_user_acct]['account_balance']
    print(f'Your new account balance is {bal}\n')
    update_account(user)
    logout()
    
def complain(user):
    complaint = input('What will you like to report?\n')
    print('Thank you for contacting us\n')
    user[current_user_acct]['complaints'].append(complaint)
    update_account(user)
    logout()
    
def bank_operation(user):
    #Getting user name from the cache
    name = user[current_user_acct]['name']
    print(f'Welcome to bankPHP, {name}\n')
    print('What would you like to do?')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaints')
    
    selected_Option = int(input('Please select an option: '))
    while True:
        #Looping to ensure user enters a valid input
        if (selected_Option == 1):
            withdraw(user)
            break
        elif (selected_Option == 2):
            deposit(user)
            break
        elif (selected_Option == 3):
            complain(user)
            break
        else:
            print(f'Invalid option selected\n')
            print(f'Select a valid option\n')
            bank_operation(user)
            break
        

def login():
    while True:   
        print(f"Logging in...")
        #Asking for user details to check database for login
        account_number = input("What is your account number: ")
        password = input("Your password: ")
        if  validate_login_details(account_number, password):
            print("login successful\n")
            bank_operation(current_user)
            break
        else:
            print("Wrong Account Number or Password. Please try again\n")
            login()
            

def register():
    #taking user details
    name = input("What is your fullname: ")
    email = input("What is your email: ")
    password = input("Your password? \npassword must be at least 8 characters long, contain uppercase and lowercase, special character and a number\n")
    validate_userdetails(name, email, password)
    
    accountNumber = generate_account_number()
    print(f"Your account number is {accountNumber}. Write it down\n")
    user_details = {
    str(accountNumber) : {
        "name": name,
        "email": email,
        "password": password,
        "account_balance": 0,
        "complaints": []
    }
    }
    #uploading the document to the database
    
    with open(db_path) as fi:
        user_datas = json.load(fi)
        user_datas.append(user_details)
        
    with open(db_path, mode='w') as f:
        f.write(json.dumps(user_datas, indent=4))
        
    login()
    
def logout():
    while True:
        #checking if user wants to log out or perform another operation
        logout = int(input('will you like to perform another transaction. 1 for Yes, 2 for No: '))
        if logout == 1:
            login()
            break     
        elif logout == 2:
            print("Thank you for banking with us, do have a nice day")
            break
        else:
            print("Enter a valid number")
def init():
    while True:
        #checking if new user or existing user
        status = int(input("Enter 1 for Login or 2 for Register: "))
        if status == 1:
            login()
            break
        elif status == 2:
            register()
            break
        else:
            print("Select a valid option\n")
            
init()       





# def withdraw():
#     pass

# def deposit():
#     pass

# def complaint():
#     pass