import datetime # Module for getting date

# Getting and printing date and time  
e = datetime.datetime.now()
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s" % (e.hour, e.minute))

allowed_Users = ['Seyi', 'Mike', 'John']
allowed_Password = ['PasswordSeyi', 'passwordMike', 'passwordJohn']

name = input('what is your name? \n')

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
            print(f'you selected Withdrawal')
        elif (selected_Option == 1):
            print(f'you selected Cash Deposit')
        elif (selected_Option == 1):
            print(f'you selected Complaints')
        else:
            print(f'invalid option selected')
    else:
        print('Password is incorrect, please try again')

else:
    print('Incorrect name, please try again')