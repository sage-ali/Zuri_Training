class Budget:
    
    def __init__(self, category):
        self.category = category
        self.amount = 0
    
    def withdraw(self, amount):
        if amount <= self.amount and amount > 0:
            self.amount -= amount
            print(f"You've withdrawn {amount} from the {self.category} category")
            print(self.check_balance())
        else:
            print(f"Insufficient balance in {self.category} category(or you tried to withdraw 0)\n")    
            
    def deposit(self, amount):
        self.amount += amount
        print(f"You've successfully deposited {amount} to the {self.category} category")
        print(self.check_balance())
        
    def transfer(self, destination, amount):
        if amount <= self.amount and amount > 0:
            self.amount -= amount
            destination.amount += amount
            print(f"You've successfully transferred {amount} from the {self.category} category to {destination.category} category")
            print(f"The current balance of the {self.category} category is {self.amount} while that of {destination.category} is {destination.amount}\n")
        else:
            print(f"Insufficient balance in {self.category} category, can not complete transfer(or you tried to transfer 0)\n")
    
    def check_balance(self):
        return f"The current balance of the {self.category} category is {self.amount}\n"



#Tests
#----------------------------------------------------------------
# food_budget = Budget("food")
# clothings_budget = Budget("clothings")
# entertainment_budget = Budget("entertainment")

# food_budget.deposit(2000)
# clothings_budget.deposit(5000)
# entertainment_budget.deposit(1000)

# food_budget.withdraw(500)
# clothings_budget.deposit(250)
# entertainment_budget.transfer(food_budget, 200)
# print(entertainment_budget.check_balance())

#clothings_budget.withdraw(0)

#Results
#----------------------------------------------------------------
# clothings_budget.withdraw(25000)
# entertainment_budget.transfer(food_budget, 20000)

# You've successfully deposited 2000 to the food category
# The current balance of the food category is 2000

# You've successfully deposited 5000 to the clothings category    
# The current balance of the clothings category is 5000

# You've successfully deposited 1000 to the entertainment category
# The current balance of the entertainment category is 1000       

# You've withdrawn 500 from the food category
# The current balance of the food category is 1500

# You've successfully deposited 250 to the clothings category
# The current balance of the clothings category is 5250

# You've successfully transferred 200 from the entertainment category to food category
# The current balance of the entertainment category is 800 while that of food is 1700

# The current balance of the entertainment category is 800

# Insufficient balance in clothings category

# Insufficient balance in entertainment category, can not complete transfer

#Insufficient balance in clothings category(or you tried to withdraw 0)