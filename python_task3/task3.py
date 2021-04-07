import datetime # Module for getting date
import re

# Getting and printing date and time  
e = datetime.datetime.now()
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s" % (e.hour, e.minute))

allowed_Users = ['Seyi', 'Mike', 'John']
allowed_Password = ['passwordSeyi', 'passwordMike', 'passwordJohn']
account_balances = [15000,15000,15000]

# 2. Include register, and login

# 3. Generate Account Number

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
    pass
  
# def login():
#     # name = input("What is your name? \n")
#     # password = input("Your password? \n")
#     # bank_operation()
#     pass
  
def register():
    #checking if new user or existing user
    name = input("What is your fullname? \n")
    email = input("What is your email? \n")
    password = input("Your password? \n")
    validate_userdetails(name, email, password)
    
    #logic to update db
    
    #login()
    


while True:
    #checking if new user or existing user
    status = int(input("Enter 1 for Login or 2 for Register\n"))
    if status == 1:
        #login()
        break
    elif status == 2:
        register()
        break
    else:
        print("Select a valid option")
        


# def auth():
#     pass



# def generate_account_number():
#     pass

# def bank_operation():
#     pass

# def withdraw():
#     pass

# def deposit():
#     pass

# def complaint():
#     pass