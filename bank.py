class bank:
    
    def __init__(self, int_rate, balance): 
        self.int_rate =int_rate
        self.balance=balance


    def deposit(self, amount):
        self.balance+= amount
        return self


    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("We cannot process your withdrawal.")
                print(f"You currently have {self.balance}.")
                print(f"And you are trying to withdraw{amount}.")
            return self  


    def display_account_info(self):
        print(f"Account balance:  {self.balance}.")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

        
        
        
    def display_account_info(self):
        return f"{self.balance}"