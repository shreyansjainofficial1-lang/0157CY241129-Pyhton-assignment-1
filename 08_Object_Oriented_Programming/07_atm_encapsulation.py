class ATM:
    def __init__(self, pin, balance=0):
        self.__pin = str(pin)
        self.__balance = float(balance)

    def verify_pin(self, entered_pin):
        return self.__pin == str(entered_pin)

    def check_balance(self, entered_pin):
        if not self.verify_pin(entered_pin):
            raise PermissionError("Incorrect PIN.")
        return self.__balance

    def deposit(self, entered_pin, amount):
        if not self.verify_pin(entered_pin):
            raise PermissionError("Incorrect PIN.")
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, entered_pin, amount):
        if not self.verify_pin(entered_pin):
            raise PermissionError("Incorrect PIN.")
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount

atm = ATM("1234", 5000)
pin = input("Enter PIN: ")

try:
    print("1. Check balance  2. Deposit  3. Withdraw")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance: Rs.", atm.check_balance(pin))
    elif choice == "2":
        atm.deposit(pin, float(input("Deposit amount: ")))
        print("Updated balance: Rs.", atm.check_balance(pin))
    elif choice == "3":
        atm.withdraw(pin, float(input("Withdrawal amount: ")))
        print("Updated balance: Rs.", atm.check_balance(pin))
    else:
        print("Invalid choice.")
except (PermissionError, ValueError) as error:
    print("Transaction failed:", error)
