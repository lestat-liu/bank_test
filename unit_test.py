# test_bank_account.py
import unittest
from banking_system import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = BankAccount("Alice", 1000)
        self.account2 = BankAccount("Bob")

    def test_deposit(self):
        self.account1.deposit(99)
        self.assertEqual(self.account1.balance, 1099, "Deposit failed")

    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500, "Withdraw failed")

    def test_overdraft_attempt(self):
        self.account1.withdraw(1500)
        captured_output = self.account1.balance  # 这里需要修改，unittest不直接支持捕获print输出
        self.assertEqual(captured_output, 500, "Overdraft should not be allowed")

    def test_transfer(self):
        self.account1.transfer(self.account2, 200)
        self.assertEqual(self.account1.balance, 800)
        self.assertEqual(self.account2.balance, 200)

    def test_negative_deposit(self):
        self.account1.deposit(-50)
        captured_output = self.account1.balance  # 同上，需要调整以正确测试打印信息
        self.assertEqual(captured_output, 300, "Negative deposit should not be allowed")

if __name__ == '__main__':
    unittest.main()
