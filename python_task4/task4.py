class Budget:
    
    def __init__(self, category):
        self.category = category
        self.amount = 0
    
    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            print(f"You've withdrawn {amount} from the {self.category} category")
            print(self.check_balance())
        else:
            print(f"Insufficient balance in {self.category} category")    
            
    def deposit(self, amount):
        self.amount += amount
        print(f"You've successfully deposited {amount} to the {self.category} category")
        print(self.check_balance())
        
    def transfer(self, destination, amount):
        if amount <= self.amount:
            self.amount -= amount
            destination.amount += amount
            print(f"You've successfully transferred {amount} from the {self.category} category to {destination.category} category")
            print(f"{self.check_balance()} while that of {destination.category} is {destination.amount}")
        else:
            print(f"Insufficient balance in {self.category} category, can not complete transfer")
    
    def check_balance(self):
        return f"The current balance of the {self.category} category is {self.amount}"
    
    