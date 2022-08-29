class CheckingAccount:
    balance = 0
    numberOfAccount = 0
    def __init__(self, balance = 0):
        CheckingAccount.balance = balance
        CheckingAccount.numberOfAccount += 1
    def __str__(self):
        return 'Account Balance: ' + str(CheckingAccount.balance)
class Account:
  def __init__(self, balance):
     self._balance = balance

  def getBalance(self):
     return self._balance


print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
