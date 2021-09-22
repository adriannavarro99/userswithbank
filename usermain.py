from user import user

from bank import bank


Adrian = user("Adrian")

Adrian.account['Account1'].deposit(100)
Adrian.display_user_balance()