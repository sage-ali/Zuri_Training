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

def auth(account_number, password):
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

    
    
    
def bank_operation(user):
    name = user[current_user_acct]['name']
    balance = float(user[current_user_acct]['account_balance'])
    print(f'Welcome to bankPHP, {name}\n')
    print('What would you like to do?')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaints')
    
    selected_Option = int(input('Please select an option \n'))
    if (selected_Option == 1):
        
        withdraw_amount = float(input('How much will you like to withdraw \n'))
        if withdraw_amount <= balance:
            print(f'Take your cash: {withdraw_amount}')
            user[current_user_acct]['account_balance'] = str(balance - withdraw_amount)
            update_account(user)
            logout()
        else:
            print('Insufficient funds')
            logout()   
            
    elif (selected_Option == 2):
        deposit_amount = float(input('How much will you like to deposit \n'))
        user[current_user_acct]['account_balance'] = str(balance + deposit_amount)
        bal = user[current_user_acct]['account_balance']
        print(f'Your new account balance is {bal}\n')
        update_account(user)
        logout()
    elif (selected_Option == 3):
        complaint = input('What will you like to report\n')
        print('Thank you for contacting us\n')
        user[current_user_acct]['complaints'].append(complaint)
        update_account(user)
        logout()
    else:
        print(f'Invalid option selected\n')
        

def login():
    while True:   
        print(f"Logging in...")
        account_number = input("What is your account number? \n")
        password = input("Your password? \n")
        if  auth(account_number, password):
            print("login successful\n")
            bank_operation(current_user)
            break
        else:
            print("Wrong Account Number or Password. Please try again\n")
            login()

def register():
    #checking if new user or existing user
    name = input("What is your fullname? \n")
    email = input("What is your email? \n")
    password = input("Your password? \n")
    validate_userdetails(name, email, password)
    
    accountNumber = generate_account_number()
    print(f"Your account number is {accountNumber}. Copy it down\n")
    user_details = {
    str(accountNumber) : {
        "name": name,
        "email": email,
        "password": password,
        "account_balance": 0,
        "complaints": []
    }
    }
    #logic to check and update db
    
    with open(db_path) as fi:
        user_datas = json.load(fi)
        user_datas.append(user_details)
        
    with open(db_path, mode='w') as f:
        f.write(json.dumps(user_datas, indent=4))
        
    login()
    
def logout():
    while True:
        logout = int(input('will you like to perform another transaction. 1 for Yes, 2 for No\n'))
        if logout == 1:
            login()     
        elif logout == 2:
            print("Thank you for banking with us, do have a nice day")
            break
        else:
            print("Enter a valid number")

while True:
    #checking if new user or existing user
    status = int(input("Enter 1 for Login or 2 for Register\n"))
    if status == 1:
        login()
        break
    elif status == 2:
        register()
        break
    else:
        print("Select a valid option\n")
        





# def withdraw():
#     pass

# def deposit():
#     pass

# def complaint():
#     pass