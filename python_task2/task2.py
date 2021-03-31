import datetime # Module for getting date

# Getting and printing date and time  
e = datetime.datetime.now()
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s" % (e.hour, e.minute))

allowed_Users = ['Seyi', 'Mike', 'John']
allowed_Password = ['passwordSeyi', 'passwordMike', 'passwordJohn']
account_balances = [15000,15000,15000]

name = input('What is your name? \n')

if(name in allowed_Users):
    userID = allowed_Users.index(name)
    password = input('Your password? \n')
    
    if(password == allowed_Password[userID]):
        
        print(f'Welcome {name}')
        print('What do you want to do?')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaints')
        
        selected_Option = int(input('Please select an option \n'))
        if (selected_Option == 1):
            
            withdraw_amount = float(input('How much will you like to withdraw \n'))
            if withdraw_amount <= account_balances[userID]:
                print('Take your cash')
                account_balances[userID] = account_balances[userID] - withdraw_amount
            else:
                print('Insufficient funds')   
            
        elif (selected_Option == 2):
            deposit_amount = float(input('How much will you like to deposit \n'))
            account_balances[userID] = account_balances[userID] + deposit_amount
            print(f'Your new account balance is {account_balances[userID]}')
            
        elif (selected_Option == 3):
            complaint = input('What will you like to report\n')
            print('Thank you for contacting us')
            
        else:
            print(f'Invalid option selected')
    else:
        print('Password is incorrect, please try again')

else:
    print('Incorrect name, please try again')