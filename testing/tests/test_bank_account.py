import unittest
from testing.src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount('1234567890', 'Axel', balance=10000)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 10500)
    
    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(500), 9500)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 10000)