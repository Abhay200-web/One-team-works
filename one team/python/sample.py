class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder   # protected
        self._balance = balance                 # protected

    def show_balance(self):
        print(f"Account Holder: {self._account_holder}, Balance: ₹{self._balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        print(f"Interest added: ₹{interest:.2f}")

    def display(self):
        print(f"Account Holder: {self._account_holder}")
        print(f"Current Balance: ₹{self._balance:.2f}")
        print(f"Interest Rate: {self.interest_rate}%")

# Create a savings account object
savings = SavingsAccount("Abhay", 5000, 5)

savings.display()
savings.add_interest()
savings.display()

# Accessing protected data directly (not recommended)
print("Accessing balance directly (not recommended):", savings._balance)
