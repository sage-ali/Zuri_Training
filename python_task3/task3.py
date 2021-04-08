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

# 4. Any other improvement you can think of (extra point)

print("===" * 24)
print("welcome to bankPHP, the coded bank")

def validate_userdetails(name, email, password):
    #logic to validate user details 
    if (re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email) and re.search(r"^[a-zA-Z]+(?:\s[a-zA-Z]+)+$", name) and re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$", password)):
        print("Valid details")
        return
    else:
        print("Enter valid details")
        register()
        
        
def generate_account_number():
    return random.randrange(1111111111,9999999999)

def auth(account_number, password):
    with open(db_path) as fi:
        user_datas = json.load(fi)
        for user in user_datas:
            if user.get(account_number, False) and user[account_number]['password'] == password:
                current_user.update(user)
                return True
    return False

def bank_operation(user):
    pass

def login():
    while True:   
        account_number = input("What is your account number? \n")
        password = input("Your password? \n")
        if  auth(account_number, password):
            print("login successful")
            bank_operation(current_user)
            break
        else:
            print("Wrong Account Number or Password. Please try again")
            login()

def register():
    #checking if new user or existing user
    name = input("What is your fullname? \n")
    email = input("What is your email? \n")
    password = input("Your password? \n")
    validate_userdetails(name, email, password)
    
    accountNumber = generate_account_number()
    
    user_details = {
    str(accountNumber) : {
        "name": name,
        "email": email,
        "password": password
        "account_balance": 0
    }
    }
    #logic to check and update db
    
    with open(db_path) as fi:
        user_datas = json.load(fi)
        user_datas.append(user_details)
        
    with open(db_path, mode='w') as f:
        f.write(json.dumps(user_datas, indent=4))
        
    
    
    #login()
    


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
        print("Select a valid option")
        





# def withdraw():
#     pass

# def deposit():
#     pass

# def complaint():
#     pass