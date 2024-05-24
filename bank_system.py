import csv


class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} Deposited {amount}. New balance: {self.balance}")
        else:
            print(f"{self.name}  Deposit amount must be positive.")

    def  withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"{self.name} Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"{self.name}  Insufficient balance.")

    def transfer(self, to_account, amount):
        if amount <= self.balance and amount > 0:
            self.withdraw(amount)
            to_account.deposit(amount)
            print(f"{self.name} Transferred {amount} to {to_account.name}.")
        else:
            print(f"{self.name} Insufficient balance for transfer.")



def save_to_csv(accounts, filename="bank_accounts.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Balance"])
        for account in accounts:
            writer.writerow([account.name, account.balance])


def load_from_csv(filename="bank_accounts.csv"):
    accounts = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, balance = row
            accounts.append(BankAccount(name, int(balance)))
    return accounts


# 创建两个银行账户
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob")

# 操作示例
account1.deposit(500)
account1.transfer(account2, 300)
account2.withdraw(200)
save_to_csv([account1, account2])
