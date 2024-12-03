import unittest, os
from testing.src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.account = BankAccount('1234567890', 'Axel', balance=10000, log_file='transaction_log.txt')
        self.target = BankAccount('9876543210', 'Messi', balance=20000)
    
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())

    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 10500)
    
    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(500), 9500)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 10000)
    
    def test_transfer(self):
        self.account.transfer(3000, self.target)
        self.assertEqual(self.account.get_balance(), 7000)
        self.assertEqual(self.target.get_balance(), 23000)

    def test_log_transaction(self):
        self.account.deposit(500)
        #self.assertTrue(os.path.exists('transaction_log.txt'))
        assert os.path.exists("transaction_log.txt")


    def test_count_transactions(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)