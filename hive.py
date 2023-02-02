from beem.account import Account

account = Account("buritica")
# print(f'Balance {account.balances["available"][0]}  {account.balances["available"][1]} \nReward pending {account.balances["rewards"][0]} {account.balances["rewards"][1]}')
print(account.balances)