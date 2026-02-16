from datetime import datetime

class BankAccount:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance
        self.history = []
        self._log_transaction("Account Created", balance)

    def _log_transaction(self, category, amount):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": category,
            "amount": amount,
            "current_balance": self.balance
        }
        self.history.append(entry)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction("Deposit", amount)
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._log_transaction("Withdrawal", amount)
            return True
        else:
            print("Withdrawal failed: Insufficient funds or invalid amount.")
            return False

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            self.history[-1]["type"] = f"Transfer to {target_account.name}"
            print(f"Transferred {amount} to {target_account.name}")
        else:
            print("Transfer canceled.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"ID: {self.number} | Owner: {self.name} | Balance: {self.balance:.2f}"

acc1 = BankAccount("1001", "John", 1000)
acc2 = BankAccount("1002", "Tom", 500)

print(f"Initial State:")
print(acc1)
print(acc2)
print("-" * 30)

acc1.deposit(500) # Pass
acc2.withdraw(100) # Pass

acc2.withdraw(1000) #Fail

print("\nInitiating Transfer...")
acc1.transfer(300, acc2)

print("\nFinal State:")
print(acc1)
print(acc2)

print("\nJohn's Transaction History:")
for entry in acc1.history:
    print(entry)

print("\nTom's Transaction History:")
for entry in acc2.history:
    print(entry)
