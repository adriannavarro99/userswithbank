


from bank import bank


class user:


    def __init__ (self,name):
        self.name = name
        self.account = {
            "Account1" : bank(.02,5000),
            "Account2" : bank(.05,4500)

        }
    

    def withdrawal (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.balance}.")
            print(f"And you are trying to withdraw{amount}.")
        return self  


    def display_user_balance(self):
        print(f"User: {self.name}, Account1 Balance: {self.account['Account1'].display_account_info()}")
        print(f"User: {self.name}, Account2 Balance: {self.account['Account2'].display_account_info()}")
        return self
    



    def deposit (self, amount):
        self.balance+= amount
        return self


    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self



