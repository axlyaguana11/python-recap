class BankAccount():
   def __init__(self, account_number, owner, balance=0, log_file=None):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.log_file = log_file
        self._log_transaction('Created Account')
    
   def _log_transaction(self, message):
       if self.log_file:
           with open(self.log_file, "a") as f:
               f.write(f'{message}\n')

   def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._log_transaction(f'Deposited {amount} USD. New balance {self.__balance} USD.')
        else:
            print('You must deposit at least 1 USD.')
        return self.__balance
    
   def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                self._log_transaction(f'Withdrew {amount} USD. New balance {self.__balance} USD.')
            else:
                print(f'Insufficient funds.')
        else:
            print(f'You must withdraw at least 1 USD.')
        return self.__balance
   
   def transfer(self, amount, target):
       if self.__balance < amount:
           raise ValueError('Insufficient funds.')
       self.withdraw(amount)
       target.deposit(amount)

   def get_balance(self):
        self._log_transaction(f'Checked balance. Current balance {self.__balance}')
        return self.__balance