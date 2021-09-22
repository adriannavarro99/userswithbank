
from bank import bank



Account1= bank(2,500)
Account2= bank(4,8000)





Account1.deposit(500).deposit(700).deposit(400).withdraw(200).display_account_info()

Account2.deposit(100).deposit(200).withdraw(100).withdraw(2000).withdraw(200).withdraw(500).display_account_info()