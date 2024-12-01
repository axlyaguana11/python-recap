class BankAccount():
   def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        

   def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount} USD. New balance is {self.__balance} USD')
        else:
            print('You must deposit at least 1 USD.')
        return self.__balance
    
   def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f'Withdrew {amount} USD. New Balance is {self.__balance} USD.')
            else:
                print(f'Insufficient funds.')
        else:
            print(f'You must withdraw at least 1 USD.')
        return self.__balance

   def get_balance(self):
        return self.__balance